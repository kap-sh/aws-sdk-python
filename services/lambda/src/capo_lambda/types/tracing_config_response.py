"""Generated from Smithy shape ``com.amazonaws.lambda#TracingConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.tracing_mode


class TracingConfigResponse(TypedDict, closed=True):
    mode: NotRequired["capo_lambda.types.tracing_mode.TracingMode"]
    """<p>The tracing mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TracingConfigResponse) -> dict:
    out: dict = {}
    if "mode" in value:
        import capo_lambda.types.tracing_mode

        out["Mode"] = capo_lambda.types.tracing_mode.serialize_json(value["mode"])
    return out


def deserialize_json(data: dict) -> TracingConfigResponse:
    out: TracingConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("Mode") is not None:
        import capo_lambda.types.tracing_mode

        out["mode"] = capo_lambda.types.tracing_mode.deserialize_json(data["Mode"])
    return out
