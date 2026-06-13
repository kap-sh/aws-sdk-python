"""Generated from Smithy shape ``com.amazonaws.ssmsap#IpAddressMember``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.allocation_type


class IpAddressMember(TypedDict):
    ip_address: NotRequired["str"]
    """<p>The IP address.</p>"""
    primary: NotRequired["bool"]
    """<p>The primary IP address.</p>"""
    allocation_type: NotRequired["aws_sdk_ssm_sap.types.allocation_type.AllocationType"]
    """<p>The type of allocation for the IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IpAddressMember) -> dict:
    out: dict = {}
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "primary" in value:
        out["Primary"] = value["primary"]
    if "allocation_type" in value:
        import aws_sdk_ssm_sap.types.allocation_type

        out["AllocationType"] = aws_sdk_ssm_sap.types.allocation_type.serialize_json(
            value["allocation_type"]
        )
    return out


def deserialize_json(data: dict) -> IpAddressMember:
    out: IpAddressMember = {}  # type: ignore[typeddict-item]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    if "Primary" in data:
        out["primary"] = data["Primary"]
    if "AllocationType" in data:
        import aws_sdk_ssm_sap.types.allocation_type

        out["allocation_type"] = aws_sdk_ssm_sap.types.allocation_type.deserialize_json(
            data["AllocationType"]
        )
    return out
