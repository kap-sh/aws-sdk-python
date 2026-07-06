"""Generated from Smithy shape ``com.amazonaws.sesv2#GetDedicatedIpPoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.pool_name


class GetDedicatedIpPoolRequest(TypedDict, closed=True):
    pool_name: "aws_sdk_sesv2.types.pool_name.PoolName"
    """<p>The name of the dedicated IP pool to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDedicatedIpPoolRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDedicatedIpPoolRequest:
    out: GetDedicatedIpPoolRequest = {}  # type: ignore[typeddict-item]
    return out
