"""Generated from Smithy shape ``com.amazonaws.s3files#DeleteAccessPointRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_s3files.types.access_point_id


class DeleteAccessPointRequest(TypedDict):
    access_point_id: "aws_sdk_s3files.types.access_point_id.AccessPointId"
    """<p>The ID or Amazon Resource Name (ARN) of the access point to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccessPointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAccessPointRequest:
    out: DeleteAccessPointRequest = {}  # type: ignore[typeddict-item]
    return out
