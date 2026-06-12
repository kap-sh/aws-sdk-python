"""Generated from Smithy shape ``com.amazonaws.efs#DeleteAccessPointRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_efs.types.access_point_id


class DeleteAccessPointRequest(TypedDict):
    access_point_id: "aws_sdk_efs.types.access_point_id.AccessPointId"
    """<p>The ID of the access point that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAccessPointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAccessPointRequest:
    out: DeleteAccessPointRequest = {}  # type: ignore[typeddict-item]
    return out
