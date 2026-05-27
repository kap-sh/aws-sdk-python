"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIdFormatRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class ModifyIdFormatRequest(TypedDict):
    resource: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of resource: <code>bundle</code> | <code>conversion-task</code> | <code>customer-gateway</code> | <code>dhcp-options</code> | <code>elastic-ip-allocation</code> | <code>elastic-ip-association</code> | <code>export-task</code> | <code>flow-log</code> | <code>image</code> | <code>import-task</code> | <code>internet-gateway</code> | <code>network-acl</code> | <code>network-acl-association</code> | <code>network-interface</code> | <code>network-interface-attachment</code> | <code>prefix-list</code> | <code>route-table</code> | <code>route-table-association</code> | <code>security-group</code> | <code>subnet</code> | <code>subnet-cidr-block-association</code> | <code>vpc</code> | <code>vpc-cidr-block-association</code> | <code>vpc-endpoint</code> | <code>vpc-peering-connection</code> | <code>vpn-connection</code> | <code>vpn-gateway</code>.</p> <p>Alternatively, use the <code>all-current</code> option to include all resource types that are currently within their opt-in period for longer IDs.</p>"""
    use_long_ids: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicate whether the resource should use longer IDs (17-character IDs).</p>"""
