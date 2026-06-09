"""Generated from Smithy shape ``com.amazonaws.ec2#IpamResourceDiscoveryAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_associated_resource_discovery_status
    import aws_sdk_ec2.types.ipam_id
    import aws_sdk_ec2.types.ipam_resource_discovery_association_id
    import aws_sdk_ec2.types.ipam_resource_discovery_association_state
    import aws_sdk_ec2.types.ipam_resource_discovery_id
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class IpamResourceDiscoveryAssociation(TypedDict):
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the resource discovery owner.</p>"""
    ipam_resource_discovery_association_id: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_association_id.IpamResourceDiscoveryAssociationId"
    ]
    """<p>The resource discovery association ID.</p>"""
    ipam_resource_discovery_association_arn: NotRequired[
        "aws_sdk_ec2.types.string.String"
    ]
    """<p>The resource discovery association Amazon Resource Name (ARN).</p>"""
    ipam_resource_discovery_id: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_id.IpamResourceDiscoveryId"
    ]
    """<p>The resource discovery ID.</p>"""
    ipam_id: NotRequired["aws_sdk_ec2.types.ipam_id.IpamId"]
    """<p>The IPAM ID.</p>"""
    ipam_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The IPAM ARN.</p>"""
    ipam_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPAM home Region.</p>"""
    is_default: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Defines if the resource discovery is the default. When you create an IPAM, a default resource discovery is created for your IPAM and it's associated with your IPAM.</p>"""
    resource_discovery_status: NotRequired[
        "aws_sdk_ec2.types.ipam_associated_resource_discovery_status.IpamAssociatedResourceDiscoveryStatus"
    ]
    """<p>The resource discovery status.</p> <ul> <li> <p> <code>active</code> - Connection or permissions required to read the results of the resource discovery are intact.</p> </li> <li> <p> <code>not-found</code> - Connection or permissions required to read the results of the resource discovery are broken. This may happen if the owner of the resource discovery stopped sharing it or deleted the resource discovery. Verify the resource discovery still exists and the Amazon Web Services RAM resource share is still intact.</p> </li> </ul>"""
    state: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_discovery_association_state.IpamResourceDiscoveryAssociationState"
    ]
    """<p>The lifecycle state of the association when you associate or disassociate a resource discovery.</p> <ul> <li> <p> <code>associate-in-progress</code> - Resource discovery is being associated.</p> </li> <li> <p> <code>associate-complete</code> - Resource discovery association is complete.</p> </li> <li> <p> <code>associate-failed</code> - Resource discovery association has failed.</p> </li> <li> <p> <code>disassociate-in-progress</code> - Resource discovery is being disassociated.</p> </li> <li> <p> <code>disassociate-complete</code> - Resource discovery disassociation is complete.</p> </li> <li> <p> <code>disassociate-failed </code> - Resource discovery disassociation has failed.</p> </li> <li> <p> <code>isolate-in-progress</code> - Amazon Web Services account that created the resource discovery association has been removed and the resource discovery association is being isolated.</p> </li> <li> <p> <code>isolate-complete</code> - Resource discovery isolation is complete.</p> </li> <li> <p> <code>restore-in-progress</code> - Resource discovery is being restored.</p> </li> </ul>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamResourceDiscoveryAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "ipam_resource_discovery_association_id" in value:
        pairs.append(
            (
                f"{prefix}.IpamResourceDiscoveryAssociationId",
                str(value["ipam_resource_discovery_association_id"]),
            )
        )
    if "ipam_resource_discovery_association_arn" in value:
        pairs.append(
            (
                f"{prefix}.IpamResourceDiscoveryAssociationArn",
                str(value["ipam_resource_discovery_association_arn"]),
            )
        )
    if "ipam_resource_discovery_id" in value:
        pairs.append(
            (
                f"{prefix}.IpamResourceDiscoveryId",
                str(value["ipam_resource_discovery_id"]),
            )
        )
    if "ipam_id" in value:
        pairs.append((f"{prefix}.IpamId", str(value["ipam_id"])))
    if "ipam_arn" in value:
        pairs.append((f"{prefix}.IpamArn", str(value["ipam_arn"])))
    if "ipam_region" in value:
        pairs.append((f"{prefix}.IpamRegion", str(value["ipam_region"])))
    if "is_default" in value:
        pairs.append(
            (f"{prefix}.IsDefault", "true" if value["is_default"] else "false")
        )
    if "resource_discovery_status" in value:
        import aws_sdk_ec2.types.ipam_associated_resource_discovery_status

        aws_sdk_ec2.types.ipam_associated_resource_discovery_status.serialize_ec2_query(
            value["resource_discovery_status"],
            pairs,
            f"{prefix}.ResourceDiscoveryStatus",
        )
    if "state" in value:
        import aws_sdk_ec2.types.ipam_resource_discovery_association_state

        aws_sdk_ec2.types.ipam_resource_discovery_association_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> IpamResourceDiscoveryAssociation:
    out: IpamResourceDiscoveryAssociation = {}  # type: ignore[typeddict-item]
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_ipam_resource_discovery_association_id = el.find(
        "IpamResourceDiscoveryAssociationId"
    )
    if child_ipam_resource_discovery_association_id is not None:
        out["ipam_resource_discovery_association_id"] = str(
            child_ipam_resource_discovery_association_id.text or ""
        )
    child_ipam_resource_discovery_association_arn = el.find(
        "IpamResourceDiscoveryAssociationArn"
    )
    if child_ipam_resource_discovery_association_arn is not None:
        out["ipam_resource_discovery_association_arn"] = str(
            child_ipam_resource_discovery_association_arn.text or ""
        )
    child_ipam_resource_discovery_id = el.find("IpamResourceDiscoveryId")
    if child_ipam_resource_discovery_id is not None:
        out["ipam_resource_discovery_id"] = str(
            child_ipam_resource_discovery_id.text or ""
        )
    child_ipam_id = el.find("IpamId")
    if child_ipam_id is not None:
        out["ipam_id"] = str(child_ipam_id.text or "")
    child_ipam_arn = el.find("IpamArn")
    if child_ipam_arn is not None:
        out["ipam_arn"] = str(child_ipam_arn.text or "")
    child_ipam_region = el.find("IpamRegion")
    if child_ipam_region is not None:
        out["ipam_region"] = str(child_ipam_region.text or "")
    child_is_default = el.find("IsDefault")
    if child_is_default is not None:
        out["is_default"] = (child_is_default.text or "").lower() == "true"
    child_resource_discovery_status = el.find("ResourceDiscoveryStatus")
    if child_resource_discovery_status is not None:
        import aws_sdk_ec2.types.ipam_associated_resource_discovery_status

        out["resource_discovery_status"] = (
            aws_sdk_ec2.types.ipam_associated_resource_discovery_status.deserialize_ec2_query(
                child_resource_discovery_status
            )
        )
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.ipam_resource_discovery_association_state

        out["state"] = (
            aws_sdk_ec2.types.ipam_resource_discovery_association_state.deserialize_ec2_query(
                child_state
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
