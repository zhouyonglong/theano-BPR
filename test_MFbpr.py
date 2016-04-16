'''
Created on Apr 15, 2016

@author: he8819197
'''
from dataloader import LoadRatingFile_HoldKOut
from MFbpr import MFbpr

if __name__ == '__main__':
    
    # Load data
    dataset = "data/yelp.rating"
    splitter = "\t"
    hold_k_out = 1
    train, test, num_user, num_item, num_ratings = LoadRatingFile_HoldKOut(dataset, splitter, hold_k_out)
    print("Load data (%s) done." %(dataset))
    print("#users: %d, #items: %d, #ratings: %d" %(num_user, num_item, num_ratings))
    
    # MFbpr parameters
    factors = 10
    learning_rate = 0.05
    reg = 0.01
    init_mean = 0
    init_stdev = 0.01
    maxIter = 1000
    num_thread = 4
    
    # Run model
    bpr = MFbpr(train, test, num_user, num_item, 
                factors, learning_rate, reg, init_mean, init_stdev)
    bpr.build_model(maxIter, num_thread)