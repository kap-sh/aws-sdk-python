"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#PutTransformerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_group_identifier
    import aws_sdk_cloudwatch_logs.types.processors


class PutTransformerRequest(TypedDict, closed=True):
    log_group_identifier: (
        "aws_sdk_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    )
    """<p>Specify either the name or ARN of the log group to create the transformer for. </p>"""
    transformer_config: "aws_sdk_cloudwatch_logs.types.processors.Processors"
    """<p>This structure contains the configuration of this log transformer. A log transformer is an array of processors, where each processor applies one type of transformation to the log events that are ingested.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutTransformerRequest) -> dict:
    out: dict = {}
    out["logGroupIdentifier"] = value["log_group_identifier"]
    import aws_sdk_cloudwatch_logs.types.processors

    out["transformerConfig"] = (
        aws_sdk_cloudwatch_logs.types.processors.serialize_aws_json_1_1(
            value["transformer_config"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutTransformerRequest:
    out: PutTransformerRequest = {}  # type: ignore[typeddict-item]
    if "logGroupIdentifier" in data:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    else:
        raise DeserializationError(
            "PutTransformerRequest.log_group_identifier required"
        )
    if "transformerConfig" in data:
        import aws_sdk_cloudwatch_logs.types.processors

        out["transformer_config"] = (
            aws_sdk_cloudwatch_logs.types.processors.deserialize_aws_json_1_1(
                data["transformerConfig"]
            )
        )
    else:
        raise DeserializationError("PutTransformerRequest.transformer_config required")
    return out
