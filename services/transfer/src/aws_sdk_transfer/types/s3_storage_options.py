"""Generated from Smithy shape ``com.amazonaws.transfer#S3StorageOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transfer.types.directory_listing_optimization


class S3StorageOptions(TypedDict):
    directory_listing_optimization: NotRequired[
        "aws_sdk_transfer.types.directory_listing_optimization.DirectoryListingOptimization"
    ]
    """<p>Specifies whether or not performance for your Amazon S3 directories is optimized.</p> <ul> <li> <p>If using the console, this is enabled by default.</p> </li> <li> <p>If using the API or CLI, this is disabled by default.</p> </li> </ul> <p>By default, home directory mappings have a <code>TYPE</code> of <code>DIRECTORY</code>. If you enable this option, you would then need to explicitly set the <code>HomeDirectoryMapEntry</code> <code>Type</code> to <code>FILE</code> if you want a mapping to have a file target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3StorageOptions) -> dict:
    out: dict = {}
    if "directory_listing_optimization" in value:
        import aws_sdk_transfer.types.directory_listing_optimization

        out["DirectoryListingOptimization"] = (
            aws_sdk_transfer.types.directory_listing_optimization.serialize_aws_json_1_1(
                value["directory_listing_optimization"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3StorageOptions:
    out: S3StorageOptions = {}  # type: ignore[typeddict-item]
    if "DirectoryListingOptimization" in data:
        import aws_sdk_transfer.types.directory_listing_optimization

        out["directory_listing_optimization"] = (
            aws_sdk_transfer.types.directory_listing_optimization.deserialize_aws_json_1_1(
                data["DirectoryListingOptimization"]
            )
        )
    return out
