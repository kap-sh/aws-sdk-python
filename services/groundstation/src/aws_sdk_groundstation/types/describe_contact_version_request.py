"""Generated from Smithy shape ``com.amazonaws.groundstation#DescribeContactVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.uuid
    import aws_sdk_groundstation.types.version_id


class DescribeContactVersionRequest(TypedDict):
    contact_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>UUID of a contact.</p>"""
    version_id: "aws_sdk_groundstation.types.version_id.VersionId"
    """<p>Version ID of a contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeContactVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeContactVersionRequest:
    out: DescribeContactVersionRequest = {}  # type: ignore[typeddict-item]
    return out
