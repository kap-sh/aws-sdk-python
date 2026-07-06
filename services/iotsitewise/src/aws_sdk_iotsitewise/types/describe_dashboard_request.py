"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeDashboardRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id


class DescribeDashboardRequest(TypedDict, closed=True):
    dashboard_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDashboardRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDashboardRequest:
    out: DescribeDashboardRequest = {}  # type: ignore[typeddict-item]
    return out
