"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ComponentParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.component_parameter_name
    import aws_sdk_imagebuilder.types.component_parameter_value_list


class ComponentParameter(TypedDict, closed=True):
    name: "aws_sdk_imagebuilder.types.component_parameter_name.ComponentParameterName"
    """<p>The name of the component parameter to set.</p>"""
    value: "aws_sdk_imagebuilder.types.component_parameter_value_list.ComponentParameterValueList"
    """<p>Sets the value for the named component parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentParameter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_imagebuilder.types.component_parameter_value_list

    out["value"] = (
        aws_sdk_imagebuilder.types.component_parameter_value_list.serialize_json(
            value["value"]
        )
    )
    return out


def deserialize_json(data: dict) -> ComponentParameter:
    out: ComponentParameter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ComponentParameter.name required")
    if "value" in data:
        import aws_sdk_imagebuilder.types.component_parameter_value_list

        out["value"] = (
            aws_sdk_imagebuilder.types.component_parameter_value_list.deserialize_json(
                data["value"]
            )
        )
    else:
        raise DeserializationError("ComponentParameter.value required")
    return out
