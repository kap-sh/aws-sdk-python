"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#GetTransformerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_group_identifier
    import aws_sdk_cloudwatch_logs.types.processors
    import aws_sdk_cloudwatch_logs.types.timestamp


class GetTransformerResponse(TypedDict, closed=True):
    log_group_identifier: NotRequired[
        "aws_sdk_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    ]
    """<p>The ARN of the log group that you specified in your request.</p>"""
    creation_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The creation time of the transformer, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.</p>"""
    last_modified_time: NotRequired["aws_sdk_cloudwatch_logs.types.timestamp.Timestamp"]
    """<p>The date and time when this transformer was most recently modified, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.</p>"""
    transformer_config: NotRequired[
        "aws_sdk_cloudwatch_logs.types.processors.Processors"
    ]
    """<p>This sructure contains the configuration of the requested transformer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTransformerResponse) -> dict:
    out: dict = {}
    if "log_group_identifier" in value:
        out["logGroupIdentifier"] = value["log_group_identifier"]
    if "creation_time" in value:
        out["creationTime"] = value["creation_time"]
    if "last_modified_time" in value:
        out["lastModifiedTime"] = value["last_modified_time"]
    if "transformer_config" in value:
        import aws_sdk_cloudwatch_logs.types.processors

        out["transformerConfig"] = (
            aws_sdk_cloudwatch_logs.types.processors.serialize_aws_json_1_1(
                value["transformer_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTransformerResponse:
    out: GetTransformerResponse = {}  # type: ignore[typeddict-item]
    if "logGroupIdentifier" in data:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    if "creationTime" in data:
        out["creation_time"] = data["creationTime"]
    if "lastModifiedTime" in data:
        out["last_modified_time"] = data["lastModifiedTime"]
    if "transformerConfig" in data:
        import aws_sdk_cloudwatch_logs.types.processors

        out["transformer_config"] = (
            aws_sdk_cloudwatch_logs.types.processors.deserialize_aws_json_1_1(
                data["transformerConfig"]
            )
        )
    return out
