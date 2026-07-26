"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#TemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.data_type
    import capo_migrationhuborchestrator.types.template_input_name


class TemplateInput(TypedDict, closed=True):
    input_name: NotRequired[
        "capo_migrationhuborchestrator.types.template_input_name.TemplateInputName"
    ]
    """<p>The name of the template.</p>"""
    data_type: NotRequired["capo_migrationhuborchestrator.types.data_type.DataType"]
    """<p>The data type of the template input.</p>"""
    required: NotRequired["bool"]
    """<p>Determine if an input is required from the template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateInput) -> dict:
    out: dict = {}
    if "input_name" in value:
        out["inputName"] = value["input_name"]
    if "data_type" in value:
        out["dataType"] = value["data_type"]
    if "required" in value:
        out["required"] = value["required"]
    return out


def deserialize_json(data: dict) -> TemplateInput:
    out: TemplateInput = {}  # type: ignore[typeddict-item]
    if "inputName" in data:
        out["input_name"] = data["inputName"]
    if "dataType" in data:
        out["data_type"] = data["dataType"]
    if "required" in data:
        out["required"] = data["required"]
    return out
