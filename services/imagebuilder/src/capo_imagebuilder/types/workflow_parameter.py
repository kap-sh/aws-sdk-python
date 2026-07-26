"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.workflow_parameter_name
    import capo_imagebuilder.types.workflow_parameter_value_list


class WorkflowParameter(TypedDict, closed=True):
    name: "capo_imagebuilder.types.workflow_parameter_name.WorkflowParameterName"
    """<p>The name of the workflow parameter to set.</p>"""
    value: "capo_imagebuilder.types.workflow_parameter_value_list.WorkflowParameterValueList"
    """<p>Sets the value for the named workflow parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowParameter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_imagebuilder.types.workflow_parameter_value_list

    out["value"] = capo_imagebuilder.types.workflow_parameter_value_list.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> WorkflowParameter:
    out: WorkflowParameter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("WorkflowParameter.name required")
    if "value" in data:
        import capo_imagebuilder.types.workflow_parameter_value_list

        out["value"] = (
            capo_imagebuilder.types.workflow_parameter_value_list.deserialize_json(
                data["value"]
            )
        )
    else:
        raise DeserializationError("WorkflowParameter.value required")
    return out
