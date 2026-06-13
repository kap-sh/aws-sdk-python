"""Generated from Smithy shape ``com.amazonaws.s3files#GetAccessPointRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3files.types.access_point_id


class GetAccessPointRequest(TypedDict):
    access_point_id: "aws_sdk_s3files.types.access_point_id.AccessPointId"
    """<p>The ID or Amazon Resource Name (ARN) of the access point to retrieve information for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccessPointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAccessPointRequest:
    out: GetAccessPointRequest = {}  # type: ignore[typeddict-item]
    return out
