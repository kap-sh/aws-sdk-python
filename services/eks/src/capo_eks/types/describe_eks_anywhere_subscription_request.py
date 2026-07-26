"""Generated from Smithy shape ``com.amazonaws.eks#DescribeEksAnywhereSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class DescribeEksAnywhereSubscriptionRequest(TypedDict, closed=True):
    id: "capo_eks.types.string.String"
    """<p>The ID of the subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEksAnywhereSubscriptionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeEksAnywhereSubscriptionRequest:
    out: DescribeEksAnywhereSubscriptionRequest = {}  # type: ignore[typeddict-item]
    return out
