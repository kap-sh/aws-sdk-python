"""Generated from Smithy shape ``com.amazonaws.lakeformation#DataLocationResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string
    import aws_sdk_lakeformation.types.resource_arn_string


class DataLocationResource(TypedDict):
    catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog where the location is registered with Lake Formation. By default, it is the account ID of the caller.</p>"""
    resource_arn: "aws_sdk_lakeformation.types.resource_arn_string.ResourceArnString"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the data location resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLocationResource) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> DataLocationResource:
    out: DataLocationResource = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("DataLocationResource.resource_arn required")
    return out
