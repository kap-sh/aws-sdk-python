"""Generated from Smithy shape ``com.amazonaws.sesv2#GetDedicatedIpPoolResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.dedicated_ip_pool


class GetDedicatedIpPoolResponse(TypedDict, closed=True):
    dedicated_ip_pool: NotRequired[
        "aws_sdk_sesv2.types.dedicated_ip_pool.DedicatedIpPool"
    ]
    """<p>An object that contains information about a dedicated IP pool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDedicatedIpPoolResponse) -> dict:
    out: dict = {}
    if "dedicated_ip_pool" in value:
        import aws_sdk_sesv2.types.dedicated_ip_pool

        out["DedicatedIpPool"] = aws_sdk_sesv2.types.dedicated_ip_pool.serialize_json(
            value["dedicated_ip_pool"]
        )
    return out


def deserialize_json(data: dict) -> GetDedicatedIpPoolResponse:
    out: GetDedicatedIpPoolResponse = {}  # type: ignore[typeddict-item]
    if "DedicatedIpPool" in data:
        import aws_sdk_sesv2.types.dedicated_ip_pool

        out["dedicated_ip_pool"] = (
            aws_sdk_sesv2.types.dedicated_ip_pool.deserialize_json(
                data["DedicatedIpPool"]
            )
        )
    return out
