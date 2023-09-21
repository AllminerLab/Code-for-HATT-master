import argparse

def dataset_number(dataset):
    if dataset == 'testdata':
        train_user_num = 30
        test_user_num = 11
        community_num = 5
        attribute_num = 11
        day_point_num = 2
    elif dataset == "1101_1108":
        train_user_num = 7771
        test_user_num = 671
        community_num = 453
        attribute_num = 94
        day_point_num = 8
    elif dataset == '3':
        train_user_num=3811
        test_user_num=6255
        attribute_num = 0
        community_num=289
        day_point_num=549
    elif dataset == '4':
        train_user_num=3811
        test_user_num=6255
        attribute_num = 0
        community_num=289
        day_point_num=549
    return  train_user_num, test_user_num, attribute_num, community_num, day_point_num

def parse():
    p = argparse.ArgumentParser("HATT", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--dataset',type=str, default='1101_1108',help=' the name of the dataset')
    p.add_argument('--model_name', type=str, default='HATT')
    p.add_argument('--input_dim',type=int,default=64,help='  the  Dimensions of initial features')
    p.add_argument('--nhid', type=int, default=256,help='number of hidden features, note that actually it\'s #nhid x #nhead')
    p.add_argument('--out_dim',type=int, default=64,help='number of output node  features, note that actually it\'s #nhid x #nhead' )
    p.add_argument('--nhead', type=int, default=7, help='number of conv heads in first layer ')
    p.add_argument('--out_nhead', type=int, default=7, help='number of conv heads in second layer')
    p.add_argument('--dropout', type=float, default=0, help='dropout ratio')
    p.add_argument('--negative_K', type=int, default=10, help='negative_K')
    p.add_argument('--cuda', type=str, default='0', help='gpu id to use')
    p.add_argument('--lam_1', type=int, default=1, help='lam_1')
    p.add_argument('--lam_2', type=int, default=1, help='lam_2')
    p.add_argument('--lam_3', type=int, default=0, help='lam_3')
    p.add_argument('--activation', type=str, default='relu', help='activation')
    p.add_argument('--lr', type=float, default=1e-5, help='learning rate')
    p.add_argument('--wd', type=float, default=1e-2, help='weight decay')
    p.add_argument('--epochs', type=int, default=1000, help='number of epochs to train')
    p.add_argument('--ssl_reg', type=int, default=1e-2, help='null')
    p.add_argument('--ssl_temp', type=int, default=0.2, help='null')
    p.add_argument('--ssl2_reg', type=int, default=1e-3, help='null')
    p.add_argument('--ssl2_temp', type=int, default=1.0, help='null')
    p.add_argument('--seed', type=int, default=1, help='seed for randomness')

    args =p.parse_args(args=[])
    train_user_number, test_user_number, attribute_number, community_number, day_point_number=dataset_number(args.dataset)
    args.train_user_number=train_user_number
    args.test_user_number=test_user_number
    args.user_number=args.train_user_number + args.test_user_number
    args.attribute_number=attribute_number
    args.community_number=community_number
    args.day_point_number=day_point_number

    return args
