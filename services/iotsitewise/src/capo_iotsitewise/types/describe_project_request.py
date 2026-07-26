"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.id


class DescribeProjectRequest(TypedDict, closed=True):
    project_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeProjectRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeProjectRequest:
    out: DescribeProjectRequest = {}  # type: ignore[typeddict-item]
    return out
