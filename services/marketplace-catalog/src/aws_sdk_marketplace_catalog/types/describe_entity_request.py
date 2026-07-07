"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#DescribeEntityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.catalog
    import aws_sdk_marketplace_catalog.types.resource_id


class DescribeEntityRequest(TypedDict, closed=True):
    catalog: "aws_sdk_marketplace_catalog.types.catalog.Catalog"
    """<p>Required. The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>"""
    entity_id: "aws_sdk_marketplace_catalog.types.resource_id.ResourceId"
    """<p>Required. The unique ID of the entity to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEntityRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeEntityRequest:
    out: DescribeEntityRequest = {}  # type: ignore[typeddict-item]
    return out
