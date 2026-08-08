"""Generated from Smithy shape ``com.amazonaws.ec2#GetVpnConnectionDeviceTypesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.next_token
    import capo_ec2.types.vpn_connection_device_type_list


class GetVpnConnectionDeviceTypesResult(TypedDict, closed=True):
    vpn_connection_device_types: NotRequired[
        "capo_ec2.types.vpn_connection_device_type_list.VpnConnectionDeviceTypeList"
    ]
    """<p>List of customer gateway devices that have a sample configuration file available for use.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The <code>NextToken</code> value to include in a future <code>GetVpnConnectionDeviceTypes</code> request. When the results of a <code>GetVpnConnectionDeviceTypes</code> request exceed <code>MaxResults</code>, this value can be used to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetVpnConnectionDeviceTypesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpn_connection_device_types" in value:
        import capo_ec2.types.vpn_connection_device_type_list

        capo_ec2.types.vpn_connection_device_type_list.serialize_ec2_query(
            value["vpn_connection_device_types"],
            pairs,
            f"{key_prefix}VpnConnectionDeviceTypeSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetVpnConnectionDeviceTypesResult:
    out: GetVpnConnectionDeviceTypesResult = {}  # type: ignore[typeddict-item]
    if el.find("vpnConnectionDeviceTypeSet") is not None:
        import capo_ec2.types.vpn_connection_device_type_list

        out["vpn_connection_device_types"] = (
            capo_ec2.types.vpn_connection_device_type_list.deserialize_ec2_query(
                el, "vpnConnectionDeviceTypeSet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
