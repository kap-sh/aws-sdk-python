"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ErrorInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.error_string


class ErrorInfo(TypedDict, closed=True):
    error_string: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.error_string.ErrorString"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ErrorInfo) -> dict:
    out: dict = {}
    if "error_string" in value:
        out["ErrorString"] = value["error_string"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ErrorInfo:
    out: ErrorInfo = {}  # type: ignore[typeddict-item]
    if "ErrorString" in data:
        out["error_string"] = data["ErrorString"]
    return out
