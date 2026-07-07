"""Generated from Smithy shape ``com.amazonaws.datazone#DataProductListing``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.created_at
    import aws_sdk_datazone.types.data_product_id
    import aws_sdk_datazone.types.detailed_glossary_terms
    import aws_sdk_datazone.types.forms
    import aws_sdk_datazone.types.listing_summaries
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.revision


class DataProductListing(TypedDict, closed=True):
    data_product_id: NotRequired["aws_sdk_datazone.types.data_product_id.DataProductId"]
    """<p>The ID of the data product listing.</p>"""
    data_product_revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision of the data product listing.</p>"""
    created_at: NotRequired["aws_sdk_datazone.types.created_at.CreatedAt"]
    """<p>The timestamp at which the data product listing was created.</p>"""
    forms: NotRequired["aws_sdk_datazone.types.forms.Forms"]
    """<p>The metadata forms of the data product listing.</p>"""
    glossary_terms: NotRequired[
        "aws_sdk_datazone.types.detailed_glossary_terms.DetailedGlossaryTerms"
    ]
    """<p>The glossary terms of the data product listing.</p>"""
    owning_project_id: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
    """<p>The ID of the owning project of the data product listing.</p>"""
    items: NotRequired["aws_sdk_datazone.types.listing_summaries.ListingSummaries"]
    """<p>The data assets of the data product listing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataProductListing) -> dict:
    out: dict = {}
    if "data_product_id" in value:
        out["dataProductId"] = value["data_product_id"]
    if "data_product_revision" in value:
        out["dataProductRevision"] = value["data_product_revision"]
    if "created_at" in value:
        import aws_sdk_datazone.types.created_at

        out["createdAt"] = aws_sdk_datazone.types.created_at.serialize_json(
            value["created_at"]
        )
    if "forms" in value:
        out["forms"] = value["forms"]
    if "glossary_terms" in value:
        import aws_sdk_datazone.types.detailed_glossary_terms

        out["glossaryTerms"] = (
            aws_sdk_datazone.types.detailed_glossary_terms.serialize_json(
                value["glossary_terms"]
            )
        )
    if "owning_project_id" in value:
        out["owningProjectId"] = value["owning_project_id"]
    if "items" in value:
        import aws_sdk_datazone.types.listing_summaries

        out["items"] = aws_sdk_datazone.types.listing_summaries.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> DataProductListing:
    out: DataProductListing = {}  # type: ignore[typeddict-item]
    if "dataProductId" in data:
        out["data_product_id"] = data["dataProductId"]
    if "dataProductRevision" in data:
        out["data_product_revision"] = data["dataProductRevision"]
    if "createdAt" in data:
        import aws_sdk_datazone.types.created_at

        out["created_at"] = aws_sdk_datazone.types.created_at.deserialize_json(
            data["createdAt"]
        )
    if "forms" in data:
        out["forms"] = data["forms"]
    if "glossaryTerms" in data:
        import aws_sdk_datazone.types.detailed_glossary_terms

        out["glossary_terms"] = (
            aws_sdk_datazone.types.detailed_glossary_terms.deserialize_json(
                data["glossaryTerms"]
            )
        )
    if "owningProjectId" in data:
        out["owning_project_id"] = data["owningProjectId"]
    if "items" in data:
        import aws_sdk_datazone.types.listing_summaries

        out["items"] = aws_sdk_datazone.types.listing_summaries.deserialize_json(
            data["items"]
        )
    return out
