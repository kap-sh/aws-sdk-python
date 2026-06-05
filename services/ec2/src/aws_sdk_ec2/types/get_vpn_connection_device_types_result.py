"""Generated from Smithy shape ``com.amazonaws.ec2#GetVpnConnectionDeviceTypesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.vpn_connection_device_type_list


class GetVpnConnectionDeviceTypesResult(TypedDict):
    vpn_connection_device_types: NotRequired[
        "aws_sdk_ec2.types.vpn_connection_device_type_list.VpnConnectionDeviceTypeList"
    ]
    """<p>List of customer gateway devices that have a sample configuration file available for use.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The <code>NextToken</code> value to include in a future <code>GetVpnConnectionDeviceTypes</code> request. When the results of a <code>GetVpnConnectionDeviceTypes</code> request exceed <code>MaxResults</code>, this value can be used to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetVpnConnectionDeviceTypesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpn_connection_device_types" in value:
        import aws_sdk_ec2.types.vpn_connection_device_type_list

        aws_sdk_ec2.types.vpn_connection_device_type_list.serialize_ec2_query(
            value["vpn_connection_device_types"],
            pairs,
            f"{prefix}.VpnConnectionDeviceTypeSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetVpnConnectionDeviceTypesResult:
    out: GetVpnConnectionDeviceTypesResult = {}  # type: ignore[typeddict-item]
    if el.find("VpnConnectionDeviceTypeSet") is not None:
        import aws_sdk_ec2.types.vpn_connection_device_type_list

        out["vpn_connection_device_types"] = (
            aws_sdk_ec2.types.vpn_connection_device_type_list.deserialize_ec2_query(
                el, "VpnConnectionDeviceTypeSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
