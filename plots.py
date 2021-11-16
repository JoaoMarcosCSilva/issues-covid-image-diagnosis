import seaborn as sns
import sklearn.metrics
import matplotlib.pyplot as plt
import math
import wandb

def confusion_matrix(dataset, y_test_pred, title, classnames):
    sns.heatmap(sklearn.metrics.confusion_matrix(dataset.y_test[0:y_test_pred.shape[0],].argmax(1), y_test_pred.argmax(1), normalize = 'true'),
                annot = True,
                xticklabels = classnames,
                yticklabels = classnames).set(title = title)
    plt.show()

def heatmatrix(matrix, title, classnames):
    sns.heatmap(matrix,
                annot = True,
                xticklabels = classnames,
                yticklabels = classnames).set(title = title)
    plt.show()

def wandb_log_img(wandb_run, title, show=True, fig=None):
    if wandb_run is not None:    
        wandb_run.log({
            title: wandb.Image(plt.gcf()) if fig is None else wandb.Image(fig)
        })

    if show:
        if fig is None:
            plt.show()
        else:
            fig.show()

def compare_images(images_a, images_b, rows):
    fig = plt.figure(figsize=(32, 12))

    columns = 10

    for i in range(int(rows * columns / 2)):
        if i >= images_a.shape[0]:
            return

        fig.add_subplot(rows, columns, i*2+1)
        plt.imshow(images_a[i,])
        plt.axis('off')

        fig.add_subplot(rows, columns, i*2+2)
        plt.imshow(images_b[i,])
        plt.axis('off')

def compare_n_images(images_tuples, rows):
    fig = plt.figure(figsize=(16, 30))

    columns = 10
    k = 1

    for i in range(len(images_tuples)):
        for img in images_tuples[i]:
            if k >= rows*columns:
                return

            fig.add_subplot(rows, columns, k)
            plt.title("dups " + str(i), color=img["color"])
            plt.imshow(img["img"])
            plt.axis('off')
            k += 1
    plt.show()
