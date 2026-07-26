"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#UploadEntityDefinitionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.definition_document
    import capo_iotthingsgraph.types.deprecate_existing_entities
    import capo_iotthingsgraph.types.sync_with_public_namespace


class UploadEntityDefinitionsRequest(TypedDict, closed=True):
    document: NotRequired[
        "capo_iotthingsgraph.types.definition_document.DefinitionDocument"
    ]
    """<p>The <code>DefinitionDocument</code> that defines the updated entities.</p>"""
    sync_with_public_namespace: (
        "capo_iotthingsgraph.types.sync_with_public_namespace.SyncWithPublicNamespace"
    )
    """<p>A Boolean that specifies whether to synchronize with the latest version of the public namespace. If set to <code>true</code>, the upload will create a new namespace version.</p>"""
    deprecate_existing_entities: "capo_iotthingsgraph.types.deprecate_existing_entities.DeprecateExistingEntities"
    """<p>A Boolean that specifies whether to deprecate all entities in the latest version before uploading the new <code>DefinitionDocument</code>. If set to <code>true</code>, the upload will create a new namespace version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UploadEntityDefinitionsRequest) -> dict:
    out: dict = {}
    if "document" in value:
        import capo_iotthingsgraph.types.definition_document

        out["document"] = (
            capo_iotthingsgraph.types.definition_document.serialize_aws_json_1_1(
                value["document"]
            )
        )
    out["syncWithPublicNamespace"] = value.get("sync_with_public_namespace", False)
    out["deprecateExistingEntities"] = value.get("deprecate_existing_entities", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> UploadEntityDefinitionsRequest:
    out: UploadEntityDefinitionsRequest = {}  # type: ignore[typeddict-item]
    if "document" in data:
        import capo_iotthingsgraph.types.definition_document

        out["document"] = (
            capo_iotthingsgraph.types.definition_document.deserialize_aws_json_1_1(
                data["document"]
            )
        )
    if "syncWithPublicNamespace" in data:
        out["sync_with_public_namespace"] = data["syncWithPublicNamespace"]
    else:
        out["sync_with_public_namespace"] = False
    if "deprecateExistingEntities" in data:
        out["deprecate_existing_entities"] = data["deprecateExistingEntities"]
    else:
        out["deprecate_existing_entities"] = False
    return out
