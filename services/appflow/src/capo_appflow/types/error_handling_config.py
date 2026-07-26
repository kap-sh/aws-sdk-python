"""Generated from Smithy shape ``com.amazonaws.appflow#ErrorHandlingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.boolean
    import capo_appflow.types.bucket_name
    import capo_appflow.types.bucket_prefix


class ErrorHandlingConfig(TypedDict, closed=True):
    fail_on_first_destination_error: "capo_appflow.types.boolean.Boolean"
    """<p> Specifies if the flow should fail after the first instance of a failure when attempting to place data in the destination. </p>"""
    bucket_prefix: NotRequired["capo_appflow.types.bucket_prefix.BucketPrefix"]
    """<p> Specifies the Amazon S3 bucket prefix. </p>"""
    bucket_name: NotRequired["capo_appflow.types.bucket_name.BucketName"]
    """<p> Specifies the name of the Amazon S3 bucket. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorHandlingConfig) -> dict:
    out: dict = {}
    out["failOnFirstDestinationError"] = value.get(
        "fail_on_first_destination_error", False
    )
    if "bucket_prefix" in value:
        out["bucketPrefix"] = value["bucket_prefix"]
    if "bucket_name" in value:
        out["bucketName"] = value["bucket_name"]
    return out


def deserialize_json(data: dict) -> ErrorHandlingConfig:
    out: ErrorHandlingConfig = {}  # type: ignore[typeddict-item]
    if "failOnFirstDestinationError" in data:
        out["fail_on_first_destination_error"] = data["failOnFirstDestinationError"]
    else:
        out["fail_on_first_destination_error"] = False
    if "bucketPrefix" in data:
        out["bucket_prefix"] = data["bucketPrefix"]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    return out
