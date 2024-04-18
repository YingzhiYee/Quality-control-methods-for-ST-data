import Barcode as Barcode
import Gene as Gene
import gene as gene
import rpy2
from django.contrib.sessions.backends import file
from jinja2 import meta
from rpy2.robjects import NULL
from rpy2.robjects.constants import FALSE
from rpy2.robjects.packages import importr

spotclean = importr('spotclean')


def function(count_dir, row_name, meta):
    pass


def getwd():
    pass


def colnames(meta):
    pass


def readMM(CountMat):
    pass


def R_get10x(out, gene_list='NULL', read10xRaw=None, count_dir=None, fname=None, countmat=None):
    # ' @name read10xRaw
    # '
    # ' @title Read 10x Space Ranger output data
    # '
    # ' @description \code{read10xRaw()} is a one-line handy function for reading
    # ' the raw expression data from 10x Space Ranger outputs and producing a count
    # ' matrix as an R object.
    # '
    # ' \code{read10xRawH5()} is for reading 10x Space Ranger
    # ' output HDF5 file (ended with .h5).
    # '
    # ' \code{read10xSlide()} is for reading slide
    # ' information (e.g. spot positions) and the tissue image from 10x
    # ' Space Ranger outputs. This function is developed based on 10x's secondary
    # ' analysis pipeline
    # ' https://support.10xgenomics.com/spatial-gene-expression/software/pipelines/latest/rkit.
    # '
    # ' @param count_dir (chr) The directory of 10x output matrix data.
    # ' The directory should include
    # ' three files: barcodes.tsv.gz, features.tsv.gz, matrix.mtx.gz.
    # '
    # ' @param h5_file (chr) The path of 10x output matrix HDF5 file
    # ' (ended with .h5).
    # '
    # ' @param tissue_csv_file (chr) The path of 10x output CSV file of
    # ' spot positions, usually named \code{tissue_positions_list.csv} for
    # ' Space Ranger V1 and \code{tissue_positions.csv} for Space Ranger V2.
    # '
    # ' @param tissue_img_file (chr) The path of the 10x output low resolution
    # ' tissue image in PNG format,
    # ' usually named \code{tissue_lowres_image.png}. If \code{NULL},
    # ' the returned slide data does not contain image
    # ' information. Please do provide this file if you could find it.
    # ' Default: \code{NULL}
    # '
    # ' @param scale_factor_file (chr) The path of the 10x output scale factor
    # ' file in json format, usually named \code{scalefactors_json.json}.
    # ' If \code{NULL}, spot positions in image will
    # ' not be corrected by the scale factor. Please do provide this file
    # ' if you could find it. Default: \code{NULL}
    # '
    # ' @param row_name (chr) Specify either using gene symbols
    # ' (\code{row_name = "symbol"}) or gene Ensembl IDs (\code{row_name = "id"})
    # ' as row names of the count matrix.
    # ' Default: \code{row_name = "symbol"}
    # '
    # ' @param meta (logical) If \code{TRUE}, \code{read10xRaw} or
    # ' \code{read10xRawH5} returns a list containing both the
    # ' count matrix and metadata of genes (features). Metadata includes feature
    # ' names, IDs and other additional information depending on Space Ranger
    # ' output. If \code{FALSE}, only returns the count matrix.
    # ' Default: \code{FALSE}
    # '
    # ' @return If \code{meta = TRUE}, \code{read10xRaw()} or \code{read10xRawH5()}
    # ' returns a list of two elements: a
    # ' "dgCMatrix" sparse matrix containing expression counts and a data
    # ' frame containing metadata of genes (features). For the count matrix,
    # ' each row is a gene (feature) and each column is a spot barcode. If
    # ' \code{meta = FALSE}, only returns the count matrix.
    # '
    # ' \code{read10xSlide()} returns a list of two objects. The first object, slide,
    # ' is a data.frame where each row corresponds to a spot
    # ' and each column corresponds to slide information such as row and column
    # ' positions on the slide. The second object, grob, is a Grid Graphical Object
    # ' of the tissue image when specifying \code{tissue_img_file}.
    # '
    # ' @examples
    # '
    # ' # simulate 10x output files of count matrix
    # ' data(mbrain_raw)
    # ' data_dir <- file.path(tempdir(),"sim_example")
    # ' dir.create(data_dir)
    # ' matrix_dir <- file.path(data_dir,"matrix.mtx")
    # ' barcode_dir <- gzfile(file.path(data_dir, "barcodes.tsv.gz"), open="wb")
    # ' gene_dir <- gzfile(file.path(data_dir, "features.tsv.gz"), open="wb")
    # '
    # ' # For simplicity, use gene names to generate gene IDs to fit the format.
    # ' gene_name <- rownames(mbrain_raw)
    # ' gene_id <- paste0("ENSG_fake_",gene_name)
    # ' barcode_id <- colnames(mbrain_raw)
    # '
    # ' Matrix::writeMM(mbrain_raw,file = matrix_dir)
    # ' write(barcode_id,file = barcode_dir)
    # ' write.table(cbind(gene_id,gene_name,"type"),file = gene_dir,
    # '     sep = "\t", quote = FALSE, col.names = FALSE, row.names = FALSE)
    # ' R.utils::gzip(matrix_dir)
    # ' close(barcode_dir)
    # ' close(gene_dir)
    # '
    # '
    # ' # read expression count matrix
    # ' list.files(data_dir)
    # ' mbrain_raw_new <- read10xRaw(data_dir)
    # ' str(mbrain_raw_new)
    # ' identical(mbrain_raw, mbrain_raw_new)
    # '
    # ' # read slide metadata
    # ' spatial_dir <- system.file(file.path("extdata",
    # '                                      "V1_Adult_Mouse_Brain_spatial"),
    # '                            package = "SpotClean")
    # ' list.files(spatial_dir)
    # ' mbrain_slide_info <- read10xSlide(tissue_csv_file=file.path(spatial_dir,
    # '                                        "tissue_positions_list.csv"),
    # '              tissue_img_file = file.path(spatial_dir,
    # '                                        "tissue_lowres_image.png"),
    # '              scale_factor_file = file.path(spatial_dir,
    # '                                        "scalefactors_json.json"))
    # ' str(mbrain_slide_info)

    # ' @rdname Read10x
    # ' @importFrom utils read.delim
    # ' @importFrom Matrix readMM
    # ' @importFrom Matrix sparseMatrix
    # '
    # '
    # ' @export
    read10xRaw <- function(count_dir=NULL,
                            row_name="symbol",
                            meta=FALSE)
    fname < - list.files(count_dir)

    Barcode < - file.path(count_dir, "barcodes.tsv.gz")
    Gene < - file.path(count_dir, "features.tsv.gz")
    # CountMat < - file.path(count_dir, "matrix.mtx.gz")

    # Read gene and barcode info
    # barcode < - readLines(Barcode)
    # gene.meta < - read.delim(Gene, header=FALSE, colClasses="character")
    # colnames(gene.meta) < - c("id", "symbol", "type")

    # Read count matrix
    #
    # countmat < - as (readMM(CountMat), "CsparseMatrix")
    # colnames(countmat) < - barcode
    # rownames(countmat) < - make.unique(gene)

    # return a list including count matrix and gene metadata
    return (list(CountMatrix=countmat, Metadata=gene.meta))

# ' @rdname Read10x
# ' @importFrom rhdf5 h5ls
# ' @importFrom rhdf5 h5read
# '
# ' @export

read10xRawH5 < - function(h5_file,
                          row_name="symbol",
                          meta=FALSE)

# ' @rdname Read10x
# ' @importFrom utils read.csv
# ' @importFrom readbitmap read.bitmap
# ' @import grid
# ' @importFrom rjson fromJSON
# ' @importFrom methods as
# '
# ' @export

read10xSlide < - function(tissue_csv_file,
                          tissue_img_file=NULL,
                          scale_factor_file=NULL)

    # Load tissue information
    # slide < - read.csv(tissue_csv_file,
    # col.names = c("barcode", "tissue", "row", "col", "imagerow", "imagecol"),
    #                  header = FALSE)


grob < - NULL
# Load tissue image
    if (1):
        # Load downsampled image
        tissue_img_file < - read.bitmap(tissue_img_file)
        grob < - rasterGrob(tissue_img_file, width=unit(1, "npc"), height=unit(1, "npc"))
        slide$height < - nrow(tissue_img_file)
        slide$width < - ncol(tissue_img_file)

    # # Load scale factor
    # if (1):
    #     scales < - rjson::fromJSON(file=scale_factor_file)
    #     slide$imagerow < - slide$imagerow * scales$tissue_lowres_scalef
    #     slide$imagecol < - slide$imagecol * scales$tissue_lowres_scalef
    #
