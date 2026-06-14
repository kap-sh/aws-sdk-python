"""Generated from Smithy shape ``com.amazonaws.datazone#DataProductItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.data_product_item_type
    import aws_sdk_datazone.types.entity_identifier
    import aws_sdk_datazone.types.item_glossary_terms
    import aws_sdk_datazone.types.revision


class DataProductItem(TypedDict):
    item_type: "aws_sdk_datazone.types.data_product_item_type.DataProductItemType"
    """<p>The type of the data product.</p>"""
    identifier: "aws_sdk_datazone.types.entity_identifier.EntityIdentifier"
    """<p>The ID of the data product.</p>"""
    revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision of the data product.</p>"""
    glossary_terms: NotRequired[
        "aws_sdk_datazone.types.item_glossary_terms.ItemGlossaryTerms"
    ]
    """<p>The glossary terms of the data product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataProductItem) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.data_product_item_type

    out["itemType"] = aws_sdk_datazone.types.data_product_item_type.serialize_json(
        value["item_type"]
    )
    out["identifier"] = value["identifier"]
    if "revision" in value:
        out["revision"] = value["revision"]
    if "glossary_terms" in value:
        import aws_sdk_datazone.types.item_glossary_terms

        out["glossaryTerms"] = (
            aws_sdk_datazone.types.item_glossary_terms.serialize_json(
                value["glossary_terms"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataProductItem:
    out: DataProductItem = {}  # type: ignore[typeddict-item]
    if "itemType" in data:
        import aws_sdk_datazone.types.data_product_item_type

        out["item_type"] = (
            aws_sdk_datazone.types.data_product_item_type.deserialize_json(
                data["itemType"]
            )
        )
    else:
        raise DeserializationError("DataProductItem.item_type required")
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("DataProductItem.identifier required")
    if "revision" in data:
        out["revision"] = data["revision"]
    if "glossaryTerms" in data:
        import aws_sdk_datazone.types.item_glossary_terms

        out["glossary_terms"] = (
            aws_sdk_datazone.types.item_glossary_terms.deserialize_json(
                data["glossaryTerms"]
            )
        )
    return out
