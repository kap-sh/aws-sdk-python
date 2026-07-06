"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#GetAccessSourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id


class GetAccessSourceInput(TypedDict, closed=True):
    access_source_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the access source to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccessSourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAccessSourceInput:
    out: GetAccessSourceInput = {}  # type: ignore[typeddict-item]
    return out
