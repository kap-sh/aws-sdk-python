"""Generated from Smithy shape ``com.amazonaws.omics#WorkflowParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.workflow_parameter_description


class WorkflowParameter(TypedDict, closed=True):
    description: NotRequired[
        "aws_sdk_omics.types.workflow_parameter_description.WorkflowParameterDescription"
    ]
    """<p>The parameter's description.</p>"""
    optional: NotRequired["bool"]
    """<p>Whether the parameter is optional.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowParameter) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "optional" in value:
        out["optional"] = value["optional"]
    return out


def deserialize_json(data: dict) -> WorkflowParameter:
    out: WorkflowParameter = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "optional" in data:
        out["optional"] = data["optional"]
    return out
