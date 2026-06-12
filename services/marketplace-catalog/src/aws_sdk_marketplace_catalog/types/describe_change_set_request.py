"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#DescribeChangeSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.catalog
    import aws_sdk_marketplace_catalog.types.resource_id


class DescribeChangeSetRequest(TypedDict):
    catalog: "aws_sdk_marketplace_catalog.types.catalog.Catalog"
    """<p>Required. The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>"""
    change_set_id: "aws_sdk_marketplace_catalog.types.resource_id.ResourceId"
    """<p>Required. The unique identifier for the <code>StartChangeSet</code> request that you want to describe the details for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeChangeSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeChangeSetRequest:
    out: DescribeChangeSetRequest = {}  # type: ignore[typeddict-item]
    return out
