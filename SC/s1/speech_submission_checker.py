import pandas as pd
import sys

def check_speech_submission_format(pred_path, sample_path='sample_submission_sc.csv'):
    pred_df = pd.read_csv(pred_path, header=None)
    samp_df = pd.read_csv(sample_path, header=None)
    
    assert len(pred_df) == len(samp_df), f'Required No. of Predictions: {len(samp_df)}, Yours: {len(pred_df)}'
    assert len(pred_df.columns) == len(samp_df.columns), f'Required No. of Columns: {len(samp_df.columns)}, Yours: {len(pred_df.columns)}'
    assert (pred_df[0] == samp_df[0]).all(), 'Please check that your submission is sorted by file name, and all file names are correct'

    print('Submission OK!')
    
    return pred_df

if __name__ == '__main__':

    check_speech_submission_format(sys.argv[1], sys.argv[2])
