"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateCodeSecurityIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.create_integration_detail
    import capo_inspector2.types.integration_name
    import capo_inspector2.types.integration_type
    import capo_inspector2.types.tag_map


class CreateCodeSecurityIntegrationRequest(TypedDict, closed=True):
    name: "capo_inspector2.types.integration_name.IntegrationName"
    """<p>The name of the code security integration.</p>"""
    type: "capo_inspector2.types.integration_type.IntegrationType"
    """<p>The type of repository provider for the integration.</p>"""
    details: NotRequired[
        "capo_inspector2.types.create_integration_detail.CreateIntegrationDetail"
    ]
    """<p>The integration details specific to the repository provider type.</p>"""
    tags: NotRequired["capo_inspector2.types.tag_map.TagMap"]
    """<p>The tags to apply to the code security integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeSecurityIntegrationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_inspector2.types.integration_type

    out["type"] = capo_inspector2.types.integration_type.serialize_json(value["type"])
    if "details" in value:
        import capo_inspector2.types.create_integration_detail

        out["details"] = capo_inspector2.types.create_integration_detail.serialize_json(
            value["details"]
        )
    if "tags" in value:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateCodeSecurityIntegrationRequest:
    out: CreateCodeSecurityIntegrationRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateCodeSecurityIntegrationRequest.name required")
    if "type" in data:
        import capo_inspector2.types.integration_type

        out["type"] = capo_inspector2.types.integration_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("CreateCodeSecurityIntegrationRequest.type required")
    if "details" in data:
        import capo_inspector2.types.create_integration_detail

        out["details"] = (
            capo_inspector2.types.create_integration_detail.deserialize_json(
                data["details"]
            )
        )
    if "tags" in data:
        import capo_inspector2.types.tag_map

        out["tags"] = capo_inspector2.types.tag_map.deserialize_json(data["tags"])
    return out
