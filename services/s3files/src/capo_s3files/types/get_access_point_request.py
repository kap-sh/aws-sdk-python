"""Generated from Smithy shape ``com.amazonaws.s3files#GetAccessPointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.access_point_id


class GetAccessPointRequest(TypedDict, closed=True):
    access_point_id: "capo_s3files.types.access_point_id.AccessPointId"
    """<p>The ID or Amazon Resource Name (ARN) of the access point to retrieve information for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccessPointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAccessPointRequest:
    out: GetAccessPointRequest = {}  # type: ignore[typeddict-item]
    return out
