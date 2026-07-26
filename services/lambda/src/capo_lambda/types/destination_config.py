"""Generated from Smithy shape ``com.amazonaws.lambda#DestinationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.on_failure
    import capo_lambda.types.on_success


class DestinationConfig(TypedDict, closed=True):
    on_success: NotRequired["capo_lambda.types.on_success.OnSuccess"]
    """<p>The destination configuration for successful invocations. Not supported in <code>CreateEventSourceMapping</code> or <code>UpdateEventSourceMapping</code>.</p>"""
    on_failure: NotRequired["capo_lambda.types.on_failure.OnFailure"]
    """<p>The destination configuration for failed invocations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationConfig) -> dict:
    out: dict = {}
    if "on_success" in value:
        import capo_lambda.types.on_success

        out["OnSuccess"] = capo_lambda.types.on_success.serialize_json(
            value["on_success"]
        )
    if "on_failure" in value:
        import capo_lambda.types.on_failure

        out["OnFailure"] = capo_lambda.types.on_failure.serialize_json(
            value["on_failure"]
        )
    return out


def deserialize_json(data: dict) -> DestinationConfig:
    out: DestinationConfig = {}  # type: ignore[typeddict-item]
    if "OnSuccess" in data:
        import capo_lambda.types.on_success

        out["on_success"] = capo_lambda.types.on_success.deserialize_json(
            data["OnSuccess"]
        )
    if "OnFailure" in data:
        import capo_lambda.types.on_failure

        out["on_failure"] = capo_lambda.types.on_failure.deserialize_json(
            data["OnFailure"]
        )
    return out
