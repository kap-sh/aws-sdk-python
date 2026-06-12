"""Generated from Smithy shape ``com.amazonaws.connectcases#GetLayoutRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.layout_id


class GetLayoutRequest(TypedDict):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    layout_id: "aws_sdk_connectcases.types.layout_id.LayoutId"
    """<p>The unique identifier of the layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLayoutRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLayoutRequest:
    out: GetLayoutRequest = {}  # type: ignore[typeddict-item]
    return out
