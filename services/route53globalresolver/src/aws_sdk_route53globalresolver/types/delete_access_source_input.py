"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#DeleteAccessSourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.resource_id


class DeleteAccessSourceInput(TypedDict, closed=True):
    access_source_id: "aws_sdk_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the access source to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccessSourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAccessSourceInput:
    out: DeleteAccessSourceInput = {}  # type: ignore[typeddict-item]
    return out
