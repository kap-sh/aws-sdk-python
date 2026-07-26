"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateEnvironmentBlueprintOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.custom_parameter_list
    import capo_datazone.types.deployment_properties
    import capo_datazone.types.description
    import capo_datazone.types.environment_blueprint_id
    import capo_datazone.types.environment_blueprint_name
    import capo_datazone.types.glossary_terms
    import capo_datazone.types.provisioning_properties


class UpdateEnvironmentBlueprintOutput(TypedDict, closed=True):
    id: "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    """<p>The identifier of the blueprint to be updated.</p>"""
    name: "capo_datazone.types.environment_blueprint_name.EnvironmentBlueprintName"
    """<p>The name to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>"""
    provider: "str"
    """<p>The provider of the blueprint to be udpated.</p>"""
    provisioning_properties: (
        "capo_datazone.types.provisioning_properties.ProvisioningProperties"
    )
    """<p>The provisioning properties to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>"""
    deployment_properties: NotRequired[
        "capo_datazone.types.deployment_properties.DeploymentProperties"
    ]
    """<p>The deployment properties to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>"""
    user_parameters: NotRequired[
        "capo_datazone.types.custom_parameter_list.CustomParameterList"
    ]
    """<p>The user parameters to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>"""
    glossary_terms: NotRequired["capo_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms to be updated as part of the <code>UpdateEnvironmentBlueprint</code> action.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the environment blueprint was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the blueprint was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentBlueprintOutput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["provider"] = value["provider"]
    import capo_datazone.types.provisioning_properties

    out["provisioningProperties"] = (
        capo_datazone.types.provisioning_properties.serialize_json(
            value["provisioning_properties"]
        )
    )
    if "deployment_properties" in value:
        import capo_datazone.types.deployment_properties

        out["deploymentProperties"] = (
            capo_datazone.types.deployment_properties.serialize_json(
                value["deployment_properties"]
            )
        )
    if "user_parameters" in value:
        import capo_datazone.types.custom_parameter_list

        out["userParameters"] = (
            capo_datazone.types.custom_parameter_list.serialize_json(
                value["user_parameters"]
            )
        )
    if "glossary_terms" in value:
        import capo_datazone.types.glossary_terms

        out["glossaryTerms"] = capo_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    if "created_at" in value:
        import capo_datazone.types._prelude.timestamp

        out["createdAt"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_datazone.types._prelude.timestamp

        out["updatedAt"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentBlueprintOutput:
    out: UpdateEnvironmentBlueprintOutput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateEnvironmentBlueprintOutput.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateEnvironmentBlueprintOutput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("UpdateEnvironmentBlueprintOutput.provider required")
    if "provisioningProperties" in data:
        import capo_datazone.types.provisioning_properties

        out["provisioning_properties"] = (
            capo_datazone.types.provisioning_properties.deserialize_json(
                data["provisioningProperties"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateEnvironmentBlueprintOutput.provisioning_properties required"
        )
    if "deploymentProperties" in data:
        import capo_datazone.types.deployment_properties

        out["deployment_properties"] = (
            capo_datazone.types.deployment_properties.deserialize_json(
                data["deploymentProperties"]
            )
        )
    if "userParameters" in data:
        import capo_datazone.types.custom_parameter_list

        out["user_parameters"] = (
            capo_datazone.types.custom_parameter_list.deserialize_json(
                data["userParameters"]
            )
        )
    if "glossaryTerms" in data:
        import capo_datazone.types.glossary_terms

        out["glossary_terms"] = capo_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if "createdAt" in data:
        import capo_datazone.types._prelude.timestamp

        out["created_at"] = capo_datazone.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import capo_datazone.types._prelude.timestamp

        out["updated_at"] = capo_datazone.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out
