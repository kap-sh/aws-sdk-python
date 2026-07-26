"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#S3ExpressDirectoryBucketConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.s3_express_directory_access_point_configurations_map
    import capo_accessanalyzer.types.s3_express_directory_bucket_policy


class S3ExpressDirectoryBucketConfiguration(TypedDict, closed=True):
    bucket_policy: NotRequired[
        "capo_accessanalyzer.types.s3_express_directory_bucket_policy.S3ExpressDirectoryBucketPolicy"
    ]
    """<p>The proposed bucket policy for the Amazon S3 directory bucket.</p>"""
    access_points: NotRequired[
        "capo_accessanalyzer.types.s3_express_directory_access_point_configurations_map.S3ExpressDirectoryAccessPointConfigurationsMap"
    ]
    """<p>The proposed access points for the Amazon S3 directory bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ExpressDirectoryBucketConfiguration) -> dict:
    out: dict = {}
    if "bucket_policy" in value:
        out["bucketPolicy"] = value["bucket_policy"]
    if "access_points" in value:
        import capo_accessanalyzer.types.s3_express_directory_access_point_configurations_map

        out["accessPoints"] = (
            capo_accessanalyzer.types.s3_express_directory_access_point_configurations_map.serialize_json(
                value["access_points"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3ExpressDirectoryBucketConfiguration:
    out: S3ExpressDirectoryBucketConfiguration = {}  # type: ignore[typeddict-item]
    if "bucketPolicy" in data:
        out["bucket_policy"] = data["bucketPolicy"]
    if "accessPoints" in data:
        import capo_accessanalyzer.types.s3_express_directory_access_point_configurations_map

        out["access_points"] = (
            capo_accessanalyzer.types.s3_express_directory_access_point_configurations_map.deserialize_json(
                data["accessPoints"]
            )
        )
    return out
