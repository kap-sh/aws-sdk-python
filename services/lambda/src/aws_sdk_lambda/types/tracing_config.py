"""Generated from Smithy shape ``com.amazonaws.lambda#TracingConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.tracing_mode


class TracingConfig(TypedDict):
    mode: NotRequired["aws_sdk_lambda.types.tracing_mode.TracingMode"]
    """<p>The tracing mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TracingConfig) -> dict:
    out: dict = {}
    if "mode" in value:
        import aws_sdk_lambda.types.tracing_mode

        out["Mode"] = aws_sdk_lambda.types.tracing_mode.serialize_json(value["mode"])
    return out


def deserialize_json(data: dict) -> TracingConfig:
    out: TracingConfig = {}  # type: ignore[typeddict-item]
    if "Mode" in data:
        import aws_sdk_lambda.types.tracing_mode

        out["mode"] = aws_sdk_lambda.types.tracing_mode.deserialize_json(data["Mode"])
    return out
