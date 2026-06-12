"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupConfigurationParameter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resource_groups.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_configuration_parameter_name
    import aws_sdk_resource_groups.types.group_configuration_parameter_value_list


class GroupConfigurationParameter(TypedDict):
    name: "aws_sdk_resource_groups.types.group_configuration_parameter_name.GroupConfigurationParameterName"
    """<p>The name of the group configuration parameter. For the list of parameters that you can use with each configuration item type, see <a href=\"https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types\">Supported resource types and parameters</a>.</p>"""
    values: NotRequired[
        "aws_sdk_resource_groups.types.group_configuration_parameter_value_list.GroupConfigurationParameterValueList"
    ]
    """<p>The value or values to be used for the specified parameter. For the list of values you can use with each parameter, see <a href=\"https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html#about-slg-types\">Supported resource types and parameters</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupConfigurationParameter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "values" in value:
        import aws_sdk_resource_groups.types.group_configuration_parameter_value_list

        out["Values"] = (
            aws_sdk_resource_groups.types.group_configuration_parameter_value_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> GroupConfigurationParameter:
    out: GroupConfigurationParameter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GroupConfigurationParameter.name required")
    if "Values" in data:
        import aws_sdk_resource_groups.types.group_configuration_parameter_value_list

        out["values"] = (
            aws_sdk_resource_groups.types.group_configuration_parameter_value_list.deserialize_json(
                data["Values"]
            )
        )
    return out
