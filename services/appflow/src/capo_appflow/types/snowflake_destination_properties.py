"""Generated from Smithy shape ``com.amazonaws.appflow#SnowflakeDestinationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.bucket_name
    import capo_appflow.types.bucket_prefix
    import capo_appflow.types.error_handling_config
    import capo_appflow.types.object


class SnowflakeDestinationProperties(TypedDict, closed=True):
    object: "capo_appflow.types.object.Object"
    """<p> The object specified in the Snowflake flow destination. </p>"""
    intermediate_bucket_name: "capo_appflow.types.bucket_name.BucketName"
    """<p> The intermediate bucket that Amazon AppFlow uses when moving data into Snowflake. </p>"""
    bucket_prefix: NotRequired["capo_appflow.types.bucket_prefix.BucketPrefix"]
    """<p> The object key for the destination bucket in which Amazon AppFlow places the files. </p>"""
    error_handling_config: NotRequired[
        "capo_appflow.types.error_handling_config.ErrorHandlingConfig"
    ]
    """<p> The settings that determine how Amazon AppFlow handles an error when placing data in the Snowflake destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. <code>ErrorHandlingConfig</code> is a part of the destination connector details. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnowflakeDestinationProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
    out["intermediateBucketName"] = value["intermediate_bucket_name"]
    if "bucket_prefix" in value:
        out["bucketPrefix"] = value["bucket_prefix"]
    if "error_handling_config" in value:
        import capo_appflow.types.error_handling_config

        out["errorHandlingConfig"] = (
            capo_appflow.types.error_handling_config.serialize_json(
                value["error_handling_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> SnowflakeDestinationProperties:
    out: SnowflakeDestinationProperties = {}  # type: ignore[typeddict-item]
    if "object" in data:
        out["object"] = data["object"]
    else:
        raise DeserializationError("SnowflakeDestinationProperties.object required")
    if "intermediateBucketName" in data:
        out["intermediate_bucket_name"] = data["intermediateBucketName"]
    else:
        raise DeserializationError(
            "SnowflakeDestinationProperties.intermediate_bucket_name required"
        )
    if "bucketPrefix" in data:
        out["bucket_prefix"] = data["bucketPrefix"]
    if "errorHandlingConfig" in data:
        import capo_appflow.types.error_handling_config

        out["error_handling_config"] = (
            capo_appflow.types.error_handling_config.deserialize_json(
                data["errorHandlingConfig"]
            )
        )
    return out
