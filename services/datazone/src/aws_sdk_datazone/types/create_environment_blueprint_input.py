"""Generated from Smithy shape ``com.amazonaws.datazone#CreateEnvironmentBlueprintInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.custom_parameter_list
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_blueprint_name
    import aws_sdk_datazone.types.provisioning_properties


class CreateEnvironmentBlueprintInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the domain in which this blueprint is created.</p>"""
    name: "aws_sdk_datazone.types.environment_blueprint_name.EnvironmentBlueprintName"
    """<p>The name of this Amazon DataZone blueprint.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the Amazon DataZone blueprint.</p>"""
    provisioning_properties: (
        "aws_sdk_datazone.types.provisioning_properties.ProvisioningProperties"
    )
    """<p>The provisioning properties of this Amazon DataZone blueprint.</p>"""
    user_parameters: NotRequired[
        "aws_sdk_datazone.types.custom_parameter_list.CustomParameterList"
    ]
    """<p>The user parameters of this Amazon DataZone blueprint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentBlueprintInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
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


def deserialize_json(data: dict) -> CreateEnvironmentBlueprintInput:
    out: CreateEnvironmentBlueprintInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateEnvironmentBlueprintInput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "provisioningProperties" in data:
        import aws_sdk_datazone.types.provisioning_properties

        out["provisioning_properties"] = (
            aws_sdk_datazone.types.provisioning_properties.deserialize_json(
                data["provisioningProperties"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEnvironmentBlueprintInput.provisioning_properties required"
        )
    if "userParameters" in data:
        import aws_sdk_datazone.types.custom_parameter_list

        out["user_parameters"] = (
            aws_sdk_datazone.types.custom_parameter_list.deserialize_json(
                data["userParameters"]
            )
        )
    return out
