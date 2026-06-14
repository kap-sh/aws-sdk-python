"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowParameterDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.workflow_parameter_description
    import aws_sdk_imagebuilder.types.workflow_parameter_name
    import aws_sdk_imagebuilder.types.workflow_parameter_type
    import aws_sdk_imagebuilder.types.workflow_parameter_value_list


class WorkflowParameterDetail(TypedDict):
    name: "aws_sdk_imagebuilder.types.workflow_parameter_name.WorkflowParameterName"
    """<p>The name of this input parameter.</p>"""
    type: "aws_sdk_imagebuilder.types.workflow_parameter_type.WorkflowParameterType"
    r"""<p>The type of input this parameter provides. The currently supported value is \"string\".</p>"""
    default_value: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_parameter_value_list.WorkflowParameterValueList"
    ]
    """<p>The default value of this parameter if no input is provided.</p>"""
    description: NotRequired[
        "aws_sdk_imagebuilder.types.workflow_parameter_description.WorkflowParameterDescription"
    ]
    """<p>Describes this parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowParameterDetail) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    if "default_value" in value:
        import aws_sdk_imagebuilder.types.workflow_parameter_value_list

        out["defaultValue"] = (
            aws_sdk_imagebuilder.types.workflow_parameter_value_list.serialize_json(
                value["default_value"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> WorkflowParameterDetail:
    out: WorkflowParameterDetail = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("WorkflowParameterDetail.name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("WorkflowParameterDetail.type required")
    if "defaultValue" in data:
        import aws_sdk_imagebuilder.types.workflow_parameter_value_list

        out["default_value"] = (
            aws_sdk_imagebuilder.types.workflow_parameter_value_list.deserialize_json(
                data["defaultValue"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    return out
