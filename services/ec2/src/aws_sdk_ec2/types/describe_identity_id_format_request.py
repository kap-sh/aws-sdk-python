"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIdentityIdFormatRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class DescribeIdentityIdFormatRequest(TypedDict):
    resource: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of resource: <code>bundle</code> | <code>conversion-task</code> | <code>customer-gateway</code> | <code>dhcp-options</code> | <code>elastic-ip-allocation</code> | <code>elastic-ip-association</code> | <code>export-task</code> | <code>flow-log</code> | <code>image</code> | <code>import-task</code> | <code>instance</code> | <code>internet-gateway</code> | <code>network-acl</code> | <code>network-acl-association</code> | <code>network-interface</code> | <code>network-interface-attachment</code> | <code>prefix-list</code> | <code>reservation</code> | <code>route-table</code> | <code>route-table-association</code> | <code>security-group</code> | <code>snapshot</code> | <code>subnet</code> | <code>subnet-cidr-block-association</code> | <code>volume</code> | <code>vpc</code> | <code>vpc-cidr-block-association</code> | <code>vpc-endpoint</code> | <code>vpc-peering-connection</code> | <code>vpn-connection</code> | <code>vpn-gateway</code> </p>"""
    principal_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the principal, which can be an IAM role, IAM user, or the root user.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIdentityIdFormatRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource" in value:
        pairs.append((f"{prefix}.Resource", str(value["resource"])))
    if "principal_arn" in value:
        pairs.append((f"{prefix}.PrincipalArn", str(value["principal_arn"])))


def deserialize_ec2_query(el: Element) -> DescribeIdentityIdFormatRequest:
    out: DescribeIdentityIdFormatRequest = {}  # type: ignore[typeddict-item]
    child_resource = el.find("Resource")
    if child_resource is not None:
        out["resource"] = str(child_resource.text or "")
    child_principal_arn = el.find("PrincipalArn")
    if child_principal_arn is not None:
        out["principal_arn"] = str(child_principal_arn.text or "")
    return out
