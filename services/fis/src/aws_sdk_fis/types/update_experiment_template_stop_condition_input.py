"""Generated from Smithy shape ``com.amazonaws.fis#UpdateExperimentTemplateStopConditionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_fis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_fis.types.stop_condition_source
    import aws_sdk_fis.types.stop_condition_value


class UpdateExperimentTemplateStopConditionInput(TypedDict, closed=True):
    source: "aws_sdk_fis.types.stop_condition_source.StopConditionSource"
    """<p>The source for the stop condition. Specify <code>aws:cloudwatch:alarm</code> if the stop condition is defined by a CloudWatch alarm. Specify <code>none</code> if there is no stop condition.</p>"""
    value: NotRequired["aws_sdk_fis.types.stop_condition_value.StopConditionValue"]
    """<p>The Amazon Resource Name (ARN) of the CloudWatch alarm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateExperimentTemplateStopConditionInput) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> UpdateExperimentTemplateStopConditionInput:
    out: UpdateExperimentTemplateStopConditionInput = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError(
            "UpdateExperimentTemplateStopConditionInput.source required"
        )
    if "value" in data:
        out["value"] = data["value"]
    return out
