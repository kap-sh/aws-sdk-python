"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribePortalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id


class DescribePortalRequest(TypedDict, closed=True):
    portal_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the portal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePortalRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribePortalRequest:
    out: DescribePortalRequest = {}  # type: ignore[typeddict-item]
    return out
