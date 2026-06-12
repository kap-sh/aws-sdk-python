"""Generated from Smithy shape ``com.amazonaws.connectcases#DeleteLayoutRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.layout_id


class DeleteLayoutRequest(TypedDict):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain.</p>"""
    layout_id: "aws_sdk_connectcases.types.layout_id.LayoutId"
    """<p>The unique identifier of the layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLayoutRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteLayoutRequest:
    out: DeleteLayoutRequest = {}  # type: ignore[typeddict-item]
    return out
