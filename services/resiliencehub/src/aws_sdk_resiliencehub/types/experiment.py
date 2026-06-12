"""Generated from Smithy shape ``com.amazonaws.resiliencehub#Experiment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.string255


class Experiment(TypedDict):
    experiment_arn: NotRequired["aws_sdk_resiliencehub.types.string255.String255"]
    """<p>Amazon Resource Name (ARN) of the FIS experiment.</p>"""
    experiment_template_id: NotRequired[
        "aws_sdk_resiliencehub.types.string255.String255"
    ]
    """<p>Identifier of the FIS experiment template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Experiment) -> dict:
    out: dict = {}
    if "experiment_arn" in value:
        out["experimentArn"] = value["experiment_arn"]
    if "experiment_template_id" in value:
        out["experimentTemplateId"] = value["experiment_template_id"]
    return out


def deserialize_json(data: dict) -> Experiment:
    out: Experiment = {}  # type: ignore[typeddict-item]
    if "experimentArn" in data:
        out["experiment_arn"] = data["experimentArn"]
    if "experimentTemplateId" in data:
        out["experiment_template_id"] = data["experimentTemplateId"]
    return out
