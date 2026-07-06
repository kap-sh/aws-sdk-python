"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#RejectedEntityInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.entity_rejection_error_type


class RejectedEntityInfo(TypedDict, closed=True):
    error_type: "aws_sdk_cloudwatch_logs.types.entity_rejection_error_type.EntityRejectionErrorType"
    """<p>The type of error that caused the rejection of the entity when calling <code>PutLogEvents</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RejectedEntityInfo) -> dict:
    out: dict = {}
    import aws_sdk_cloudwatch_logs.types.entity_rejection_error_type

    out["errorType"] = (
        aws_sdk_cloudwatch_logs.types.entity_rejection_error_type.serialize_aws_json_1_1(
            value["error_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RejectedEntityInfo:
    out: RejectedEntityInfo = {}  # type: ignore[typeddict-item]
    if "errorType" in data:
        import aws_sdk_cloudwatch_logs.types.entity_rejection_error_type

        out["error_type"] = (
            aws_sdk_cloudwatch_logs.types.entity_rejection_error_type.deserialize_aws_json_1_1(
                data["errorType"]
            )
        )
    else:
        raise DeserializationError("RejectedEntityInfo.error_type required")
    return out
