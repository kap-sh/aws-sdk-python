"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSReadCacheConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.open_zfs_read_cache_sizing_mode
    import capo_fsx.types.storage_capacity


class OpenZFSReadCacheConfiguration(TypedDict, closed=True):
    sizing_mode: NotRequired[
        "capo_fsx.types.open_zfs_read_cache_sizing_mode.OpenZFSReadCacheSizingMode"
    ]
    """<p> Specifies how the provisioned SSD read cache is sized, as follows: </p> <ul> <li> <p>Set to <code>NO_CACHE</code> if you do not want to use an SSD read cache with your Intelligent-Tiering file system.</p> </li> <li> <p>Set to <code>USER_PROVISIONED</code> to specify the exact size of your SSD read cache.</p> </li> <li> <p>Set to <code>PROPORTIONAL_TO_THROUGHPUT_CAPACITY</code> to have your SSD read cache automatically sized based on your throughput capacity.</p> </li> </ul>"""
    size_gi_b: NotRequired["capo_fsx.types.storage_capacity.StorageCapacity"]
    """<p> Required if <code>SizingMode</code> is set to <code>USER_PROVISIONED</code>. Specifies the size of the file system's SSD read cache, in gibibytes (GiB). </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpenZFSReadCacheConfiguration) -> dict:
    out: dict = {}
    if "sizing_mode" in value:
        import capo_fsx.types.open_zfs_read_cache_sizing_mode

        out["SizingMode"] = (
            capo_fsx.types.open_zfs_read_cache_sizing_mode.serialize_aws_json_1_1(
                value["sizing_mode"]
            )
        )
    if "size_gi_b" in value:
        out["SizeGiB"] = value["size_gi_b"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OpenZFSReadCacheConfiguration:
    out: OpenZFSReadCacheConfiguration = {}  # type: ignore[typeddict-item]
    if "SizingMode" in data:
        import capo_fsx.types.open_zfs_read_cache_sizing_mode

        out["sizing_mode"] = (
            capo_fsx.types.open_zfs_read_cache_sizing_mode.deserialize_aws_json_1_1(
                data["SizingMode"]
            )
        )
    if "SizeGiB" in data:
        out["size_gi_b"] = data["SizeGiB"]
    return out
