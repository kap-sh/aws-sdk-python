"""Generated from Smithy shape ``com.amazonaws.omics#RunLogLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.engine_log_stream
    import capo_omics.types.run_log_stream


class RunLogLocation(TypedDict, closed=True):
    engine_log_stream: NotRequired["capo_omics.types.engine_log_stream.EngineLogStream"]
    """<p>The log stream ARN for the engine log.</p>"""
    run_log_stream: NotRequired["capo_omics.types.run_log_stream.RunLogStream"]
    """<p>The log stream ARN for the run log.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RunLogLocation) -> dict:
    out: dict = {}
    if "engine_log_stream" in value:
        out["engineLogStream"] = value["engine_log_stream"]
    if "run_log_stream" in value:
        out["runLogStream"] = value["run_log_stream"]
    return out


def deserialize_json(data: dict) -> RunLogLocation:
    out: RunLogLocation = {}  # type: ignore[typeddict-item]
    if "engineLogStream" in data:
        out["engine_log_stream"] = data["engineLogStream"]
    if "runLogStream" in data:
        out["run_log_stream"] = data["runLogStream"]
    return out
