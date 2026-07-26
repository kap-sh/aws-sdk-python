"""Generated from Smithy shape ``com.amazonaws.fsx#FileCacheDataRepositoryAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.archive_path
    import capo_fsx.types.file_cache_nfs_configuration
    import capo_fsx.types.namespace
    import capo_fsx.types.sub_directories_paths


class FileCacheDataRepositoryAssociation(TypedDict, closed=True):
    file_cache_path: NotRequired["capo_fsx.types.namespace.Namespace"]
    """<p>A path on the cache that points to a high-level directory (such as <code>/ns1/</code>) or subdirectory (such as <code>/ns1/subdir/</code>) that will be mapped 1-1 with <code>DataRepositoryPath</code>. The leading forward slash in the name is required. Two data repository associations cannot have overlapping cache paths. For example, if a data repository is associated with cache path <code>/ns1/</code>, then you cannot link another data repository with cache path <code>/ns1/ns2</code>.</p> <p>This path specifies where in your cache files will be exported from. This cache directory can be linked to only one data repository, and no data repository other can be linked to the directory.</p> <note> <p>The cache path can only be set to root (/) on an NFS DRA when <code>DataRepositorySubdirectories</code> is specified. If you specify root (/) as the cache path, you can create only one DRA on the cache.</p> <p>The cache path cannot be set to root (/) for an S3 DRA.</p> </note>"""
    data_repository_path: NotRequired["capo_fsx.types.archive_path.ArchivePath"]
    """<p>The path to the S3 or NFS data repository that links to the cache. You must provide one of the following paths:</p> <ul> <li> <p>The path can be an NFS data repository that links to the cache. The path can be in one of two formats:</p> <ul> <li> <p>If you are not using the <code>DataRepositorySubdirectories</code> parameter, the path is to an NFS Export directory (or one of its subdirectories) in the format <code>nfs://nfs-domain-name/exportpath</code>. You can therefore link a single NFS Export to a single data repository association.</p> </li> <li> <p>If you are using the <code>DataRepositorySubdirectories</code> parameter, the path is the domain name of the NFS file system in the format <code>nfs://filer-domain-name</code>, which indicates the root of the subdirectories specified with the <code>DataRepositorySubdirectories</code> parameter.</p> </li> </ul> </li> <li> <p>The path can be an S3 bucket or prefix in the format <code>s3://bucket-name/prefix/</code> (where <code>prefix</code> is optional).</p> </li> </ul>"""
    data_repository_subdirectories: NotRequired[
        "capo_fsx.types.sub_directories_paths.SubDirectoriesPaths"
    ]
    """<p>A list of NFS Exports that will be linked with this data repository association. The Export paths are in the format <code>/exportpath1</code>. To use this parameter, you must configure <code>DataRepositoryPath</code> as the domain name of the NFS file system. The NFS file system domain name in effect is the root of the subdirectories. Note that <code>DataRepositorySubdirectories</code> is not supported for S3 data repositories.</p>"""
    nfs: NotRequired[
        "capo_fsx.types.file_cache_nfs_configuration.FileCacheNFSConfiguration"
    ]
    """<p>The configuration for a data repository association that links an Amazon File Cache resource to an NFS data repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileCacheDataRepositoryAssociation) -> dict:
    out: dict = {}
    if "file_cache_path" in value:
        out["FileCachePath"] = value["file_cache_path"]
    if "data_repository_path" in value:
        out["DataRepositoryPath"] = value["data_repository_path"]
    if "data_repository_subdirectories" in value:
        import capo_fsx.types.sub_directories_paths

        out["DataRepositorySubdirectories"] = (
            capo_fsx.types.sub_directories_paths.serialize_aws_json_1_1(
                value["data_repository_subdirectories"]
            )
        )
    if "nfs" in value:
        import capo_fsx.types.file_cache_nfs_configuration

        out["NFS"] = capo_fsx.types.file_cache_nfs_configuration.serialize_aws_json_1_1(
            value["nfs"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FileCacheDataRepositoryAssociation:
    out: FileCacheDataRepositoryAssociation = {}  # type: ignore[typeddict-item]
    if "FileCachePath" in data:
        out["file_cache_path"] = data["FileCachePath"]
    if "DataRepositoryPath" in data:
        out["data_repository_path"] = data["DataRepositoryPath"]
    if "DataRepositorySubdirectories" in data:
        import capo_fsx.types.sub_directories_paths

        out["data_repository_subdirectories"] = (
            capo_fsx.types.sub_directories_paths.deserialize_aws_json_1_1(
                data["DataRepositorySubdirectories"]
            )
        )
    if "NFS" in data:
        import capo_fsx.types.file_cache_nfs_configuration

        out["nfs"] = (
            capo_fsx.types.file_cache_nfs_configuration.deserialize_aws_json_1_1(
                data["NFS"]
            )
        )
    return out
