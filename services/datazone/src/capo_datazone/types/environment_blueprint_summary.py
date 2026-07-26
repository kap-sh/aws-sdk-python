"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentBlueprintSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.description
    import capo_datazone.types.environment_blueprint_id
    import capo_datazone.types.environment_blueprint_name
    import capo_datazone.types.provisioning_properties


class EnvironmentBlueprintSummary(TypedDict, closed=True):
    id: "capo_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    """<p>The identifier of the blueprint.</p>"""
    name: "capo_datazone.types.environment_blueprint_name.EnvironmentBlueprintName"
    """<p>The name of the blueprint.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The description of a blueprint.</p>"""
    provider: "str"
    """<p>The provider of the blueprint.</p>"""
    provisioning_properties: (
        "capo_datazone.types.provisioning_properties.ProvisioningProperties"
    )
    """<p>The provisioning properties of the blueprint.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when an environment blueprint was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the blueprint was enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentBlueprintSummary) -> dict:
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


def deserialize_json(data: dict) -> EnvironmentBlueprintSummary:
    out: EnvironmentBlueprintSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("EnvironmentBlueprintSummary.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("EnvironmentBlueprintSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("EnvironmentBlueprintSummary.provider required")
    if "provisioningProperties" in data:
        import capo_datazone.types.provisioning_properties

        out["provisioning_properties"] = (
            capo_datazone.types.provisioning_properties.deserialize_json(
                data["provisioningProperties"]
            )
        )
    else:
        raise DeserializationError(
            "EnvironmentBlueprintSummary.provisioning_properties required"
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
