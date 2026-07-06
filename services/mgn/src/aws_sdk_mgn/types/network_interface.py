"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.bounded_string
    import aws_sdk_mgn.types.i_ps_list


class NetworkInterface(TypedDict, closed=True):
    mac_address: NotRequired["aws_sdk_mgn.types.bounded_string.BoundedString"]
    """<p>Network interface Mac address.</p>"""
    ips: NotRequired["aws_sdk_mgn.types.i_ps_list.IPsList"]
    """<p>Network interface IPs.</p>"""
    is_primary: NotRequired["bool"]
    """<p>Network interface primary IP.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkInterface) -> dict:
    out: dict = {}
    if "mac_address" in value:
        out["macAddress"] = value["mac_address"]
    if "ips" in value:
        import aws_sdk_mgn.types.i_ps_list

        out["ips"] = aws_sdk_mgn.types.i_ps_list.serialize_json(value["ips"])
    if "is_primary" in value:
        out["isPrimary"] = value["is_primary"]
    return out


def deserialize_json(data: dict) -> NetworkInterface:
    out: NetworkInterface = {}  # type: ignore[typeddict-item]
    if "macAddress" in data:
        out["mac_address"] = data["macAddress"]
    if "ips" in data:
        import aws_sdk_mgn.types.i_ps_list

        out["ips"] = aws_sdk_mgn.types.i_ps_list.deserialize_json(data["ips"])
    if "isPrimary" in data:
        out["is_primary"] = data["isPrimary"]
    return out
