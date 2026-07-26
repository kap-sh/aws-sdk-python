"""Generated from Smithy shape ``com.amazonaws.groundstation#DescribeContactVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.uuid
    import capo_groundstation.types.version_id


class DescribeContactVersionRequest(TypedDict, closed=True):
    contact_id: "capo_groundstation.types.uuid.Uuid"
    """<p>UUID of a contact.</p>"""
    version_id: "capo_groundstation.types.version_id.VersionId"
    """<p>Version ID of a contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeContactVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeContactVersionRequest:
    out: DescribeContactVersionRequest = {}  # type: ignore[typeddict-item]
    return out
