"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateEnvironmentBlueprintInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.custom_parameter_list
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_blueprint_id
    import aws_sdk_datazone.types.provisioning_properties


class UpdateEnvironmentBlueprintInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which an environment blueprint is to be updated.</p>"""
    identifier: "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    """<p>The identifier of the environment blueprint to be updated.</p>"""
    description: NotRequired["str"]
    """<p>The description to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>"""
    provisioning_properties: NotRequired[
        "aws_sdk_datazone.types.provisioning_properties.ProvisioningProperties"
    ]
    """<p>The provisioning properties to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>"""
    user_parameters: NotRequired[
        "aws_sdk_datazone.types.custom_parameter_list.CustomParameterList"
    ]
    """<p>The user parameters to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentBlueprintInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "provisioning_properties" in value:
        import aws_sdk_datazone.types.provisioning_properties

        out["provisioningProperties"] = (
            aws_sdk_datazone.types.provisioning_properties.serialize_json(
                value["provisioning_properties"]
            )
        )
    if "user_parameters" in value:
        import aws_sdk_datazone.types.custom_parameter_list

        out["userParameters"] = (
            aws_sdk_datazone.types.custom_parameter_list.serialize_json(
                value["user_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentBlueprintInput:
    out: UpdateEnvironmentBlueprintInput = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "provisioningProperties" in data:
        import aws_sdk_datazone.types.provisioning_properties

        out["provisioning_properties"] = (
            aws_sdk_datazone.types.provisioning_properties.deserialize_json(
                data["provisioningProperties"]
            )
        )
    if "userParameters" in data:
        import aws_sdk_datazone.types.custom_parameter_list

        out["user_parameters"] = (
            aws_sdk_datazone.types.custom_parameter_list.deserialize_json(
                data["userParameters"]
            )
        )
    return out
