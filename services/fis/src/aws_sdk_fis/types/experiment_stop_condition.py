"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentStopCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.stop_condition_source
    import aws_sdk_fis.types.stop_condition_value


class ExperimentStopCondition(TypedDict, closed=True):
    source: NotRequired["aws_sdk_fis.types.stop_condition_source.StopConditionSource"]
    """<p>The source for the stop condition.</p>"""
    value: NotRequired["aws_sdk_fis.types.stop_condition_value.StopConditionValue"]
    """<p>The Amazon Resource Name (ARN) of the CloudWatch alarm, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentStopCondition) -> dict:
    out: dict = {}
    if "source" in value:
        out["source"] = value["source"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ExperimentStopCondition:
    out: ExperimentStopCondition = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    if "value" in data:
        out["value"] = data["value"]
    return out
