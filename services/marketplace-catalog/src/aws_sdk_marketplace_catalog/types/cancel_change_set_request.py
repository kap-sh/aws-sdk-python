"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#CancelChangeSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.catalog
    import aws_sdk_marketplace_catalog.types.resource_id


class CancelChangeSetRequest(TypedDict, closed=True):
    catalog: "aws_sdk_marketplace_catalog.types.catalog.Catalog"
    """<p>Required. The catalog related to the request. Fixed value: <code>AWSMarketplace</code>.</p>"""
    change_set_id: "aws_sdk_marketplace_catalog.types.resource_id.ResourceId"
    """<p>Required. The unique identifier of the <code>StartChangeSet</code> request that you want to cancel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelChangeSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelChangeSetRequest:
    out: CancelChangeSetRequest = {}  # type: ignore[typeddict-item]
    return out
