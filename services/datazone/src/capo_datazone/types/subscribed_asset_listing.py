"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedAssetListing``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.asset_id
    import capo_datazone.types.asset_scope
    import capo_datazone.types.detailed_glossary_terms
    import capo_datazone.types.forms
    import capo_datazone.types.permissions
    import capo_datazone.types.revision
    import capo_datazone.types.type_name


class SubscribedAssetListing(TypedDict, closed=True):
    entity_id: NotRequired["capo_datazone.types.asset_id.AssetId"]
    """<p>The identifier of the published asset for which the subscription grant is created.</p>"""
    entity_revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision of the published asset for which the subscription grant is created.</p>"""
    entity_type: NotRequired["capo_datazone.types.type_name.TypeName"]
    """<p>The type of the published asset for which the subscription grant is created.</p>"""
    forms: NotRequired["capo_datazone.types.forms.Forms"]
    """<p>The forms attached to the published asset for which the subscription grant is created.</p>"""
    glossary_terms: NotRequired[
        "capo_datazone.types.detailed_glossary_terms.DetailedGlossaryTerms"
    ]
    """<p>The glossary terms attached to the published asset for which the subscription grant is created.</p>"""
    asset_scope: NotRequired["capo_datazone.types.asset_scope.AssetScope"]
    """<p>The asset scope of the subscribed asset listing.</p>"""
    permissions: NotRequired["capo_datazone.types.permissions.Permissions"]
    """<p>The asset permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedAssetListing) -> dict:
    out: dict = {}
    if "entity_id" in value:
        out["entityId"] = value["entity_id"]
    if "entity_revision" in value:
        out["entityRevision"] = value["entity_revision"]
    if "entity_type" in value:
        out["entityType"] = value["entity_type"]
    if "forms" in value:
        out["forms"] = value["forms"]
    if "glossary_terms" in value:
        import capo_datazone.types.detailed_glossary_terms

        out["glossaryTerms"] = (
            capo_datazone.types.detailed_glossary_terms.serialize_json(
                value["glossary_terms"]
            )
        )
    if "asset_scope" in value:
        import capo_datazone.types.asset_scope

        out["assetScope"] = capo_datazone.types.asset_scope.serialize_json(
            value["asset_scope"]
        )
    if "permissions" in value:
        import capo_datazone.types.permissions

        out["permissions"] = capo_datazone.types.permissions.serialize_json(
            value["permissions"]
        )
    return out


def deserialize_json(data: dict) -> SubscribedAssetListing:
    out: SubscribedAssetListing = {}  # type: ignore[typeddict-item]
    if "entityId" in data:
        out["entity_id"] = data["entityId"]
    if "entityRevision" in data:
        out["entity_revision"] = data["entityRevision"]
    if "entityType" in data:
        out["entity_type"] = data["entityType"]
    if "forms" in data:
        out["forms"] = data["forms"]
    if "glossaryTerms" in data:
        import capo_datazone.types.detailed_glossary_terms

        out["glossary_terms"] = (
            capo_datazone.types.detailed_glossary_terms.deserialize_json(
                data["glossaryTerms"]
            )
        )
    if "assetScope" in data:
        import capo_datazone.types.asset_scope

        out["asset_scope"] = capo_datazone.types.asset_scope.deserialize_json(
            data["assetScope"]
        )
    if "permissions" in data:
        import capo_datazone.types.permissions

        out["permissions"] = capo_datazone.types.permissions.deserialize_json(
            data["permissions"]
        )
    return out
