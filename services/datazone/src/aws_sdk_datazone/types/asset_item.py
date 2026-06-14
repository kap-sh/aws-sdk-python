"""Generated from Smithy shape ``com.amazonaws.datazone#AssetItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_identifier
    import aws_sdk_datazone.types.asset_item_additional_attributes
    import aws_sdk_datazone.types.asset_name
    import aws_sdk_datazone.types.asset_type_identifier
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.created_by
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.external_identifier
    import aws_sdk_datazone.types.glossary_terms
    import aws_sdk_datazone.types.governed_glossary_terms
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.revision


class AssetItem(TypedDict):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which the inventory asset exists.</p>"""
    identifier: "aws_sdk_datazone.types.asset_identifier.AssetIdentifier"
    """<p>the identifier of the Amazon DataZone inventory asset.</p>"""
    name: "aws_sdk_datazone.types.asset_name.AssetName"
    """<p>The name of the Amazon DataZone inventory asset.</p>"""
    type_identifier: "aws_sdk_datazone.types.asset_type_identifier.AssetTypeIdentifier"
    """<p>The identifier of the asset type of the specified Amazon DataZone inventory asset.</p>"""
    type_revision: "aws_sdk_datazone.types.revision.Revision"
    """<p>The revision of the inventory asset type.</p>"""
    external_identifier: NotRequired[
        "aws_sdk_datazone.types.external_identifier.ExternalIdentifier"
    ]
    """<p>The external identifier of the Amazon DataZone inventory asset.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of an Amazon DataZone inventory asset.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp of when the Amazon DataZone inventory asset was created.</p>"""
    created_by: NotRequired["aws_sdk_datazone.types.created_by.CreatedBy"]
    """<p>The Amazon DataZone user who created the inventory asset.</p>"""
    first_revision_created_at: NotRequired[
        "aws_sdk_datazone.types.created_at.CreatedAt"
    ]
    """<p>The timestamp of when the first revision of the inventory asset was created.</p>"""
    first_revision_created_by: NotRequired[
        "aws_sdk_datazone.types.created_by.CreatedBy"
    ]
    """<p>The Amazon DataZone user who created the first revision of the inventory asset.</p>"""
    glossary_terms: NotRequired["aws_sdk_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms attached to the Amazon DataZone inventory asset.</p>"""
    owning_project_id: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The identifier of the Amazon DataZone project that owns the inventory asset.</p>"""
    additional_attributes: NotRequired[
        "aws_sdk_datazone.types.asset_item_additional_attributes.AssetItemAdditionalAttributes"
    ]
    """<p>The additional attributes of a Amazon DataZone inventory asset. </p>"""
    governed_glossary_terms: NotRequired[
        "aws_sdk_datazone.types.governed_glossary_terms.GovernedGlossaryTerms"
    ]
    """<p>The restricted glossary terms accociated with an asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetItem) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["identifier"] = value["identifier"]
    out["name"] = value["name"]
    out["typeIdentifier"] = value["type_identifier"]
    out["typeRevision"] = value["type_revision"]
    if "external_identifier" in value:
        out["externalIdentifier"] = value["external_identifier"]
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "first_revision_created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["firstRevisionCreatedAt"] = (
            aws_sdk_datazone.types.created_at.serialize_json(
                value["first_revision_created_at"]
            )
        )
    if "first_revision_created_by" in value:
        out["firstRevisionCreatedBy"] = value["first_revision_created_by"]
    if "glossary_terms" in value:
        import aws_sdk_datazone.types.glossary_terms

        out["glossaryTerms"] = aws_sdk_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    out["owningProjectId"] = value["owning_project_id"]
    if "additional_attributes" in value:
        import aws_sdk_datazone.types.asset_item_additional_attributes

        out["additionalAttributes"] = (
            aws_sdk_datazone.types.asset_item_additional_attributes.serialize_json(
                value["additional_attributes"]
            )
        )
    if "governed_glossary_terms" in value:
        import aws_sdk_datazone.types.governed_glossary_terms

        out["governedGlossaryTerms"] = (
            aws_sdk_datazone.types.governed_glossary_terms.serialize_json(
                value["governed_glossary_terms"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetItem:
    out: AssetItem = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("AssetItem.domain_id required")
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("AssetItem.identifier required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AssetItem.name required")
    if "typeIdentifier" in data:
        out["type_identifier"] = data["typeIdentifier"]
    else:
        raise DeserializationError("AssetItem.type_identifier required")
    if "typeRevision" in data:
        out["type_revision"] = data["typeRevision"]
    else:
        raise DeserializationError("AssetItem.type_revision required")
    if "externalIdentifier" in data:
        out["external_identifier"] = data["externalIdentifier"]
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    if "firstRevisionCreatedAt" in data:
        import aws_sdk_datazone.types.created_at

        out["first_revision_created_at"] = (
            aws_sdk_datazone.types.created_at.deserialize_json(
                data["firstRevisionCreatedAt"]
            )
        )
    if "firstRevisionCreatedBy" in data:
        out["first_revision_created_by"] = data["firstRevisionCreatedBy"]
    if "glossaryTerms" in data:
        import aws_sdk_datazone.types.glossary_terms

        out["glossary_terms"] = aws_sdk_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    else:
        raise DeserializationError("AssetItem.owning_project_id required")
    if "additionalAttributes" in data:
        import aws_sdk_datazone.types.asset_item_additional_attributes

        out["additional_attributes"] = (
            aws_sdk_datazone.types.asset_item_additional_attributes.deserialize_json(
                data["additionalAttributes"]
            )
        )
    if "governedGlossaryTerms" in data:
        import aws_sdk_datazone.types.governed_glossary_terms

        out["governed_glossary_terms"] = (
            aws_sdk_datazone.types.governed_glossary_terms.deserialize_json(
                data["governedGlossaryTerms"]
            )
        )
    return out
