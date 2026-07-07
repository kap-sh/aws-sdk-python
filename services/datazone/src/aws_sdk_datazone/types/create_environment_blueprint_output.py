"""Generated from Smithy shape ``com.amazonaws.datazone#CreateEnvironmentBlueprintOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.custom_parameter_list
    import aws_sdk_datazone.types.deployment_properties
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.environment_blueprint_id
    import aws_sdk_datazone.types.environment_blueprint_name
    import aws_sdk_datazone.types.glossary_terms
    import aws_sdk_datazone.types.provisioning_properties


class CreateEnvironmentBlueprintOutput(TypedDict, closed=True):
    id: "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    """<p>The ID of this Amazon DataZone blueprint.</p>"""
    name: "aws_sdk_datazone.types.environment_blueprint_name.EnvironmentBlueprintName"
    """<p>The name of this Amazon DataZone blueprint.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of this Amazon DataZone blueprint.</p>"""
    provider: "str"
    """<p>The provider of this Amazon DataZone blueprint.</p>"""
    provisioning_properties: (
        "aws_sdk_datazone.types.provisioning_properties.ProvisioningProperties"
    )
    """<p>The provisioning properties of this Amazon DataZone blueprint.</p>"""
    deployment_properties: NotRequired[
        "aws_sdk_datazone.types.deployment_properties.DeploymentProperties"
    ]
    """<p>The deployment properties of this Amazon DataZone blueprint.</p>"""
    user_parameters: NotRequired[
        "aws_sdk_datazone.types.custom_parameter_list.CustomParameterList"
    ]
    """<p>The user parameters of this Amazon DataZone blueprint.</p>"""
    glossary_terms: NotRequired["aws_sdk_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms attached to this Amazon DataZone blueprint.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp at which the environment blueprint was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when this blueprint was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentBlueprintOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["provider"] = value["provider"]
    import aws_sdk_datazone.types.provisioning_properties

    out["provisioningProperties"] = (
        aws_sdk_datazone.types.provisioning_properties.serialize_json(
            value["provisioning_properties"]
        )
    )
    if "deployment_properties" in value:
        import aws_sdk_datazone.types.deployment_properties

        out["deploymentProperties"] = (
            aws_sdk_datazone.types.deployment_properties.serialize_json(
                value["deployment_properties"]
            )
        )
    if "user_parameters" in value:
        import aws_sdk_datazone.types.custom_parameter_list

        out["userParameters"] = (
            aws_sdk_datazone.types.custom_parameter_list.serialize_json(
                value["user_parameters"]
            )
        )
    if "glossary_terms" in value:
        import aws_sdk_datazone.types.glossary_terms

        out["glossaryTerms"] = aws_sdk_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    if "created_at" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["createdAt"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["updatedAt"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> CreateEnvironmentBlueprintOutput:
    out: CreateEnvironmentBlueprintOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateEnvironmentBlueprintOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateEnvironmentBlueprintOutput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("CreateEnvironmentBlueprintOutput.provider required")
    if "provisioningProperties" in data:
        import aws_sdk_datazone.types.provisioning_properties

        out["provisioning_properties"] = (
            aws_sdk_datazone.types.provisioning_properties.deserialize_json(
                data["provisioningProperties"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEnvironmentBlueprintOutput.provisioning_properties required"
        )
    if "deploymentProperties" in data:
        import aws_sdk_datazone.types.deployment_properties

        out["deployment_properties"] = (
            aws_sdk_datazone.types.deployment_properties.deserialize_json(
                data["deploymentProperties"]
            )
        )
    if "userParameters" in data:
        import aws_sdk_datazone.types.custom_parameter_list

        out["user_parameters"] = (
            aws_sdk_datazone.types.custom_parameter_list.deserialize_json(
                data["userParameters"]
            )
        )
    if "glossaryTerms" in data:
        import aws_sdk_datazone.types.glossary_terms

        out["glossary_terms"] = aws_sdk_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if "createdAt" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["created_at"] = aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["updated_at"] = aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out
