"""Generated from Smithy shape ``com.amazonaws.quicksight#S3BucketConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.non_empty_string


class S3BucketConfiguration(TypedDict, closed=True):
    bucket_name: "capo_quicksight.types.non_empty_string.NonEmptyString"
    """<p>The name of an existing Amazon S3 bucket where the generated snapshot artifacts are sent.</p>"""
    bucket_prefix: "capo_quicksight.types.non_empty_string.NonEmptyString"
    """<p>The prefix of the Amazon S3 bucket that the generated snapshots are stored in.</p>"""
    bucket_region: "capo_quicksight.types.non_empty_string.NonEmptyString"
    """<p>The region that the Amazon S3 bucket is located in. The bucket must be located in the same region that the <code>StartDashboardSnapshotJob</code> API call is made.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketConfiguration) -> dict:
    out: dict = {}
    out["BucketName"] = value["bucket_name"]
    out["BucketPrefix"] = value["bucket_prefix"]
    out["BucketRegion"] = value["bucket_region"]
    return out


def deserialize_json(data: dict) -> S3BucketConfiguration:
    out: S3BucketConfiguration = {}  # type: ignore[typeddict-item]
    if "BucketName" in data:
        out["bucket_name"] = data["BucketName"]
    else:
        raise DeserializationError("S3BucketConfiguration.bucket_name required")
    if "BucketPrefix" in data:
        out["bucket_prefix"] = data["BucketPrefix"]
    else:
        raise DeserializationError("S3BucketConfiguration.bucket_prefix required")
    if "BucketRegion" in data:
        out["bucket_region"] = data["BucketRegion"]
    else:
        raise DeserializationError("S3BucketConfiguration.bucket_region required")
    return out
