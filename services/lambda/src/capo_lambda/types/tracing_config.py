"""Generated from Smithy shape ``com.amazonaws.lambda#TracingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.tracing_mode


class TracingConfig(TypedDict, closed=True):
    mode: NotRequired["capo_lambda.types.tracing_mode.TracingMode"]
    """<p>The tracing mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TracingConfig) -> dict:
    out: dict = {}
    if "mode" in value:
        import capo_lambda.types.tracing_mode

        out["Mode"] = capo_lambda.types.tracing_mode.serialize_json(value["mode"])
    return out


def deserialize_json(data: dict) -> TracingConfig:
    out: TracingConfig = {}  # type: ignore[typeddict-item]
    if data.get("Mode") is not None:
        import capo_lambda.types.tracing_mode

        out["mode"] = capo_lambda.types.tracing_mode.deserialize_json(data["Mode"])
    return out
