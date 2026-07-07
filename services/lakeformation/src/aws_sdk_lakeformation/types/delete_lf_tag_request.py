"""Generated from Smithy shape ``com.amazonaws.lakeformation#DeleteLFTagRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string
    import aws_sdk_lakeformation.types.lf_tag_key


class DeleteLFTagRequest(TypedDict, closed=True):
    catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    tag_key: "aws_sdk_lakeformation.types.lf_tag_key.LFTagKey"
    """<p>The key-name for the LF-tag to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLFTagRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["TagKey"] = value["tag_key"]
    return out


def deserialize_json(data: dict) -> DeleteLFTagRequest:
    out: DeleteLFTagRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "TagKey" in data:
        out["tag_key"] = data["TagKey"]
    else:
        raise DeserializationError("DeleteLFTagRequest.tag_key required")
    return out
