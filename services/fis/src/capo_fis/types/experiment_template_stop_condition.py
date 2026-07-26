"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateStopCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.stop_condition_source
    import capo_fis.types.stop_condition_value


class ExperimentTemplateStopCondition(TypedDict, closed=True):
    source: NotRequired["capo_fis.types.stop_condition_source.StopConditionSource"]
    """<p>The source for the stop condition.</p>"""
    value: NotRequired["capo_fis.types.stop_condition_value.StopConditionValue"]
    """<p>The Amazon Resource Name (ARN) of the CloudWatch alarm, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTemplateStopCondition) -> dict:
    out: dict = {}
    if "source" in value:
        out["source"] = value["source"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ExperimentTemplateStopCondition:
    out: ExperimentTemplateStopCondition = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    if "value" in data:
        out["value"] = data["value"]
    return out
