"""Generated from Smithy shape ``com.amazonaws.eks#StartInsightsRefreshRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class StartInsightsRefreshRequest(TypedDict):
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The name of the cluster for the refresh insights operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartInsightsRefreshRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartInsightsRefreshRequest:
    out: StartInsightsRefreshRequest = {}  # type: ignore[typeddict-item]
    return out
