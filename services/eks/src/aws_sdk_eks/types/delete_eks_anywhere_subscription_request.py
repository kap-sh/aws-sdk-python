"""Generated from Smithy shape ``com.amazonaws.eks#DeleteEksAnywhereSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class DeleteEksAnywhereSubscriptionRequest(TypedDict, closed=True):
    id: "aws_sdk_eks.types.string.String"
    """<p>The ID of the subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEksAnywhereSubscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEksAnywhereSubscriptionRequest:
    out: DeleteEksAnywhereSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out
