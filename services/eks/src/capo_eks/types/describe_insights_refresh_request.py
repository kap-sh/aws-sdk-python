"""Generated from Smithy shape ``com.amazonaws.eks#DescribeInsightsRefreshRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eks.types.string


class DescribeInsightsRefreshRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of the cluster associated with the insights refresh operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInsightsRefreshRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeInsightsRefreshRequest:
    out: DescribeInsightsRefreshRequest = {}  # type: ignore[typeddict-item]
    return out
