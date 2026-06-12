"""Generated from Smithy shape ``com.amazonaws.lakeformation#LFTagExpressionResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string
    import aws_sdk_lakeformation.types.name_string


class LFTagExpressionResource(TypedDict):
    catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. </p>"""
    name: "aws_sdk_lakeformation.types.name_string.NameString"
    """<p>The name of the LF-Tag expression to grant permissions on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LFTagExpressionResource) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> LFTagExpressionResource:
    out: LFTagExpressionResource = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("LFTagExpressionResource.name required")
    return out
