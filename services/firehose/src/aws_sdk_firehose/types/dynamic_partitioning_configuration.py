"""Generated from Smithy shape ``com.amazonaws.firehose#DynamicPartitioningConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.boolean_object
    import aws_sdk_firehose.types.retry_options


class DynamicPartitioningConfiguration(TypedDict):
    retry_options: NotRequired["aws_sdk_firehose.types.retry_options.RetryOptions"]
    """<p>The retry behavior in case Firehose is unable to deliver data to an Amazon S3 prefix.</p>"""
    enabled: NotRequired["aws_sdk_firehose.types.boolean_object.BooleanObject"]
    """<p>Specifies that the dynamic partitioning is enabled for this Firehose stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DynamicPartitioningConfiguration) -> dict:
    out: dict = {}
    if "retry_options" in value:
        import aws_sdk_firehose.types.retry_options

        out["RetryOptions"] = (
            aws_sdk_firehose.types.retry_options.serialize_aws_json_1_1(
                value["retry_options"]
            )
        )
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DynamicPartitioningConfiguration:
    out: DynamicPartitioningConfiguration = {}  # type: ignore[typeddict-item]
    if "RetryOptions" in data:
        import aws_sdk_firehose.types.retry_options

        out["retry_options"] = (
            aws_sdk_firehose.types.retry_options.deserialize_aws_json_1_1(
                data["RetryOptions"]
            )
        )
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
