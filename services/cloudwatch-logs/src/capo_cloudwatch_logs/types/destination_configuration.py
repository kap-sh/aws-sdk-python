"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.s3_configuration


class DestinationConfiguration(TypedDict, closed=True):
    s3_configuration: "capo_cloudwatch_logs.types.s3_configuration.S3Configuration"
    """<p>Configuration for delivering query results to Amazon S3.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DestinationConfiguration) -> dict:
    out: dict = {}
    import capo_cloudwatch_logs.types.s3_configuration

    out["s3Configuration"] = (
        capo_cloudwatch_logs.types.s3_configuration.serialize_aws_json_1_1(
            value["s3_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DestinationConfiguration:
    out: DestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("s3Configuration") is not None:
        import capo_cloudwatch_logs.types.s3_configuration

        out["s3_configuration"] = (
            capo_cloudwatch_logs.types.s3_configuration.deserialize_aws_json_1_1(
                data["s3Configuration"]
            )
        )
    else:
        raise DeserializationError("DestinationConfiguration.s3_configuration required")
    return out
