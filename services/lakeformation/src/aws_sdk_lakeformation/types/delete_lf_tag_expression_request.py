"""Generated from Smithy shape ``com.amazonaws.lakeformation#DeleteLFTagExpressionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string
    import aws_sdk_lakeformation.types.name_string


class DeleteLFTagExpressionRequest(TypedDict):
    name: "aws_sdk_lakeformation.types.name_string.NameString"
    """<p>The name for the LF-Tag expression.</p>"""
    catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID in which the LF-Tag expression is saved. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLFTagExpressionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    return out


def deserialize_json(data: dict) -> DeleteLFTagExpressionRequest:
    out: DeleteLFTagExpressionRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteLFTagExpressionRequest.name required")
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    return out
