"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxDocumentMetadatas``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.tax_document_metadata

TaxDocumentMetadatas: TypeAlias = list["aws_sdk_taxsettings.types.tax_document_metadata.TaxDocumentMetadata"]


# --- restJson1 ser/de ---
def serialize_json(value: TaxDocumentMetadatas) -> list:
    import aws_sdk_taxsettings.types.tax_document_metadata
    out: list = []
    for item in value:
        out.append(aws_sdk_taxsettings.types.tax_document_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> TaxDocumentMetadatas:
    import aws_sdk_taxsettings.types.tax_document_metadata
    out: TaxDocumentMetadatas = []
    for item in data:
        out.append(aws_sdk_taxsettings.types.tax_document_metadata.deserialize_json(item))
    return out