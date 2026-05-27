"""Generated from Smithy shape ``com.amazonaws.ec2#GetVpnConnectionDeviceTypesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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
