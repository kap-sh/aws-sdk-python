"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#CreateEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_migration_hub_refactor_spaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.client_token
    import capo_migration_hub_refactor_spaces.types.description
    import capo_migration_hub_refactor_spaces.types.environment_name
    import capo_migration_hub_refactor_spaces.types.network_fabric_type
    import capo_migration_hub_refactor_spaces.types.tag_map


class CreateEnvironmentRequest(TypedDict, closed=True):
    name: "capo_migration_hub_refactor_spaces.types.environment_name.EnvironmentName"
    """<p>The name of the environment.</p>"""
    description: NotRequired[
        "capo_migration_hub_refactor_spaces.types.description.Description"
    ]
    """<p>The description of the environment.</p>"""
    network_fabric_type: (
        "capo_migration_hub_refactor_spaces.types.network_fabric_type.NetworkFabricType"
    )
    """<p>The network fabric type of the environment.</p>"""
    tags: NotRequired["capo_migration_hub_refactor_spaces.types.tag_map.TagMap"]
    """<p>The tags to assign to the environment. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key-value pair.</p>"""
    client_token: NotRequired[
        "capo_migration_hub_refactor_spaces.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["NetworkFabricType"] = value["network_fabric_type"]
    if "tags" in value:
        import capo_migration_hub_refactor_spaces.types.tag_map

        out["Tags"] = capo_migration_hub_refactor_spaces.types.tag_map.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateEnvironmentRequest:
    out: CreateEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateEnvironmentRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "NetworkFabricType" in data:
        out["network_fabric_type"] = data["NetworkFabricType"]
    else:
        raise DeserializationError(
            "CreateEnvironmentRequest.network_fabric_type required"
        )
    if "Tags" in data:
        import capo_migration_hub_refactor_spaces.types.tag_map

        out["tags"] = capo_migration_hub_refactor_spaces.types.tag_map.deserialize_json(
            data["Tags"]
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
