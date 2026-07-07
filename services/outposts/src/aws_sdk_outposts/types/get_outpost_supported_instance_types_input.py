"""Generated from Smithy shape ``com.amazonaws.outposts#GetOutpostSupportedInstanceTypesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_outposts.types.asset_id_input
    import aws_sdk_outposts.types.max_results1000
    import aws_sdk_outposts.types.order_id
    import aws_sdk_outposts.types.outpost_identifier
    import aws_sdk_outposts.types.token


class GetOutpostSupportedInstanceTypesInput(TypedDict, closed=True):
    outpost_identifier: "aws_sdk_outposts.types.outpost_identifier.OutpostIdentifier"
    """<p>The ID or ARN of the Outpost.</p>"""
    order_id: NotRequired["aws_sdk_outposts.types.order_id.OrderId"]
    """<p>The ID for the Amazon Web Services Outposts order.</p>"""
    asset_id: NotRequired["aws_sdk_outposts.types.asset_id_input.AssetIdInput"]
    """<p>The ID of the Outpost asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.</p>"""
    max_results: NotRequired["aws_sdk_outposts.types.max_results1000.MaxResults1000"]
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]


# --- restJson1 ser/de ---
def serialize_json(value: GetOutpostSupportedInstanceTypesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOutpostSupportedInstanceTypesInput:
    out: GetOutpostSupportedInstanceTypesInput = {}  # type: ignore[typeddict-item]
    return out
