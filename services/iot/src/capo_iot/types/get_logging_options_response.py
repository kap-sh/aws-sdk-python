"""Generated from Smithy shape ``com.amazonaws.iot#GetLoggingOptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.log_level


class GetLoggingOptionsResponse(TypedDict, closed=True):
    role_arn: NotRequired["capo_iot.types.aws_arn.AwsArn"]
    """<p>The ARN of the IAM role that grants access.</p>"""
    log_level: NotRequired["capo_iot.types.log_level.LogLevel"]
    """<p>The logging level.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLoggingOptionsResponse) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "log_level" in value:
        import capo_iot.types.log_level

        out["logLevel"] = capo_iot.types.log_level.serialize_json(value["log_level"])
    return out


def deserialize_json(data: dict) -> GetLoggingOptionsResponse:
    out: GetLoggingOptionsResponse = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "logLevel" in data:
        import capo_iot.types.log_level

        out["log_level"] = capo_iot.types.log_level.deserialize_json(data["logLevel"])
    return out
