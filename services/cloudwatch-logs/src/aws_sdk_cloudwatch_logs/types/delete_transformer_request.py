"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteTransformerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.log_group_identifier


class DeleteTransformerRequest(TypedDict):
    log_group_identifier: (
        "aws_sdk_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
    )
    """<p>Specify either the name or ARN of the log group to delete the transformer for. If the log group is in a source account and you are using a monitoring account, you must use the log group ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTransformerRequest) -> dict:
    out: dict = {}
    out["logGroupIdentifier"] = value["log_group_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTransformerRequest:
    out: DeleteTransformerRequest = {}  # type: ignore[typeddict-item]
    if "logGroupIdentifier" in data:
        out["log_group_identifier"] = data["logGroupIdentifier"]
    else:
        raise DeserializationError(
            "DeleteTransformerRequest.log_group_identifier required"
        )
    return out
