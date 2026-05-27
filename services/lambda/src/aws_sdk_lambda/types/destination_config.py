"""Generated from Smithy shape ``com.amazonaws.lambda#DestinationConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.on_failure
    import aws_sdk_lambda.types.on_success


class DestinationConfig(TypedDict):
    on_success: NotRequired["aws_sdk_lambda.types.on_success.OnSuccess"]
    """<p>The destination configuration for successful invocations. Not supported in <code>CreateEventSourceMapping</code> or <code>UpdateEventSourceMapping</code>.</p>"""
    on_failure: NotRequired["aws_sdk_lambda.types.on_failure.OnFailure"]
    """<p>The destination configuration for failed invocations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationConfig) -> dict:
    out: dict = {}
    if "on_success" in value:
        import aws_sdk_lambda.types.on_success

        out["OnSuccess"] = aws_sdk_lambda.types.on_success.serialize_json(
            value["on_success"]
        )
    if "on_failure" in value:
        import aws_sdk_lambda.types.on_failure

        out["OnFailure"] = aws_sdk_lambda.types.on_failure.serialize_json(
            value["on_failure"]
        )
    return out


def deserialize_json(data: dict) -> DestinationConfig:
    out: DestinationConfig = {}  # type: ignore[typeddict-item]
    if "OnSuccess" in data:
        import aws_sdk_lambda.types.on_success

        out["on_success"] = aws_sdk_lambda.types.on_success.deserialize_json(
            data["OnSuccess"]
        )
    if "OnFailure" in data:
        import aws_sdk_lambda.types.on_failure

        out["on_failure"] = aws_sdk_lambda.types.on_failure.deserialize_json(
            data["OnFailure"]
        )
    return out
