"""Generated from Smithy shape ``com.amazonaws.opensearch#AutoTuneOptionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.auto_tune_state
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.string


class AutoTuneOptionsOutput(TypedDict, closed=True):
    state: NotRequired["aws_sdk_opensearch.types.auto_tune_state.AutoTuneState"]
    """<p>The current state of Auto-Tune on the domain.</p>"""
    error_message: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>Any errors that occurred while enabling or disabling Auto-Tune.</p>"""
    use_off_peak_window: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Whether the domain's off-peak window will be used to deploy Auto-Tune changes rather than a maintenance schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneOptionsOutput) -> dict:
    out: dict = {}
    if "state" in value:
        import aws_sdk_opensearch.types.auto_tune_state

        out["State"] = aws_sdk_opensearch.types.auto_tune_state.serialize_json(
            value["state"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "use_off_peak_window" in value:
        out["UseOffPeakWindow"] = value["use_off_peak_window"]
    return out


def deserialize_json(data: dict) -> AutoTuneOptionsOutput:
    out: AutoTuneOptionsOutput = {}  # type: ignore[typeddict-item]
    if "State" in data:
        import aws_sdk_opensearch.types.auto_tune_state

        out["state"] = aws_sdk_opensearch.types.auto_tune_state.deserialize_json(
            data["State"]
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "UseOffPeakWindow" in data:
        out["use_off_peak_window"] = data["UseOffPeakWindow"]
    return out
