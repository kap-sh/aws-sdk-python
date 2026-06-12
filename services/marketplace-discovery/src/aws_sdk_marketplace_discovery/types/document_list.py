"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#DocumentList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.document_item

DocumentList: TypeAlias = list["aws_sdk_marketplace_discovery.types.document_item.DocumentItem"]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentList) -> list:
    import aws_sdk_marketplace_discovery.types.document_item
    out: list = []
    for item in value:
        out.append(aws_sdk_marketplace_discovery.types.document_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> DocumentList:
    import aws_sdk_marketplace_discovery.types.document_item
    out: DocumentList = []
    for item in data:
        out.append(aws_sdk_marketplace_discovery.types.document_item.deserialize_json(item))
    return out