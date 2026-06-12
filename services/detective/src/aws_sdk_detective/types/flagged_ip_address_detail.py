"""Generated from Smithy shape ``com.amazonaws.detective#FlaggedIpAddressDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_detective.types.ip_address
    import aws_sdk_detective.types.reason


class FlaggedIpAddressDetail(TypedDict):
    ip_address: NotRequired["aws_sdk_detective.types.ip_address.IpAddress"]
    """<p>IP address of the suspicious entity.</p>"""
    reason: NotRequired["aws_sdk_detective.types.reason.Reason"]
    """<p>Details the reason the IP address was flagged as suspicious.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlaggedIpAddressDetail) -> dict:
    out: dict = {}
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "reason" in value:
        import aws_sdk_detective.types.reason

        out["Reason"] = aws_sdk_detective.types.reason.serialize_json(value["reason"])
    return out


def deserialize_json(data: dict) -> FlaggedIpAddressDetail:
    out: FlaggedIpAddressDetail = {}  # type: ignore[typeddict-item]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    if "Reason" in data:
        import aws_sdk_detective.types.reason

        out["reason"] = aws_sdk_detective.types.reason.deserialize_json(data["Reason"])
    return out
