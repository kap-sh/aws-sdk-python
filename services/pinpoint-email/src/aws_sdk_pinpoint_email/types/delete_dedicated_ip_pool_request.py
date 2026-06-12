"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DeleteDedicatedIpPoolRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.pool_name


class DeleteDedicatedIpPoolRequest(TypedDict):
    pool_name: "aws_sdk_pinpoint_email.types.pool_name.PoolName"
    """<p>The name of the dedicated IP pool that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDedicatedIpPoolRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDedicatedIpPoolRequest:
    out: DeleteDedicatedIpPoolRequest = {}  # type: ignore[typeddict-item]
    return out
