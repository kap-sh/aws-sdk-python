"""Generated from Smithy shape ``com.amazonaws.ec2#IpamScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.ipam_scope_external_authority_configuration
    import aws_sdk_ec2.types.ipam_scope_id
    import aws_sdk_ec2.types.ipam_scope_state
    import aws_sdk_ec2.types.ipam_scope_type
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class IpamScope(TypedDict, closed=True):
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID of the owner of the scope.</p>"""
    ipam_scope_id: NotRequired["aws_sdk_ec2.types.ipam_scope_id.IpamScopeId"]
    """<p>The ID of the scope.</p>"""
    ipam_scope_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the scope.</p>"""
    ipam_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the IPAM.</p>"""
    ipam_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region of the IPAM scope.</p>"""
    ipam_scope_type: NotRequired["aws_sdk_ec2.types.ipam_scope_type.IpamScopeType"]
    """<p>The type of the scope.</p>"""
    is_default: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Defines if the scope is the default scope or not.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of the scope.</p>"""
    pool_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of pools in the scope.</p>"""
    state: NotRequired["aws_sdk_ec2.types.ipam_scope_state.IpamScopeState"]
    """<p>The state of the IPAM scope.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p>"""
    external_authority_configuration: NotRequired[
        "aws_sdk_ec2.types.ipam_scope_external_authority_configuration.IpamScopeExternalAuthorityConfiguration"
    ]
    """<p>The external authority configuration for this IPAM scope, if configured.</p> <p>The configuration that links an Amazon VPC IPAM scope to an external authority system. It specifies the type of external system and the external resource identifier that identifies your account or instance in that system.</p> <p>In IPAM, an external authority is a third-party IP address management system that provides CIDR blocks when you provision address space for top-level IPAM pools. This allows you to use your existing IP management system to control which address ranges are allocated to Amazon Web Services while using Amazon VPC IPAM to manage subnets within those ranges.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamScope, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "ipam_scope_id" in value:
        pairs.append((f"{prefix}.IpamScopeId", str(value["ipam_scope_id"])))
    if "ipam_scope_arn" in value:
        pairs.append((f"{prefix}.IpamScopeArn", str(value["ipam_scope_arn"])))
    if "ipam_arn" in value:
        pairs.append((f"{prefix}.IpamArn", str(value["ipam_arn"])))
    if "ipam_region" in value:
        pairs.append((f"{prefix}.IpamRegion", str(value["ipam_region"])))
    if "ipam_scope_type" in value:
        import aws_sdk_ec2.types.ipam_scope_type

        aws_sdk_ec2.types.ipam_scope_type.serialize_ec2_query(
            value["ipam_scope_type"], pairs, f"{prefix}.IpamScopeType"
        )
    if "is_default" in value:
        pairs.append(
            (f"{prefix}.IsDefault", "true" if value["is_default"] else "false")
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "pool_count" in value:
        pairs.append((f"{prefix}.PoolCount", str(value["pool_count"])))
    if "state" in value:
        import aws_sdk_ec2.types.ipam_scope_state

        aws_sdk_ec2.types.ipam_scope_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "external_authority_configuration" in value:
        import aws_sdk_ec2.types.ipam_scope_external_authority_configuration

        aws_sdk_ec2.types.ipam_scope_external_authority_configuration.serialize_ec2_query(
            value["external_authority_configuration"],
            pairs,
            f"{prefix}.ExternalAuthorityConfiguration",
        )


def deserialize_ec2_query(el: Element) -> IpamScope:
    out: IpamScope = {}  # type: ignore[typeddict-item]
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_ipam_scope_id = el.find("IpamScopeId")
    if child_ipam_scope_id is not None:
        out["ipam_scope_id"] = str(child_ipam_scope_id.text or "")
    child_ipam_scope_arn = el.find("IpamScopeArn")
    if child_ipam_scope_arn is not None:
        out["ipam_scope_arn"] = str(child_ipam_scope_arn.text or "")
    child_ipam_arn = el.find("IpamArn")
    if child_ipam_arn is not None:
        out["ipam_arn"] = str(child_ipam_arn.text or "")
    child_ipam_region = el.find("IpamRegion")
    if child_ipam_region is not None:
        out["ipam_region"] = str(child_ipam_region.text or "")
    child_ipam_scope_type = el.find("IpamScopeType")
    if child_ipam_scope_type is not None:
        import aws_sdk_ec2.types.ipam_scope_type

        out["ipam_scope_type"] = (
            aws_sdk_ec2.types.ipam_scope_type.deserialize_ec2_query(
                child_ipam_scope_type
            )
        )
    child_is_default = el.find("IsDefault")
    if child_is_default is not None:
        out["is_default"] = (child_is_default.text or "").lower() == "true"
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_pool_count = el.find("PoolCount")
    if child_pool_count is not None:
        out["pool_count"] = int(child_pool_count.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.ipam_scope_state

        out["state"] = aws_sdk_ec2.types.ipam_scope_state.deserialize_ec2_query(
            child_state
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_external_authority_configuration = el.find("ExternalAuthorityConfiguration")
    if child_external_authority_configuration is not None:
        import aws_sdk_ec2.types.ipam_scope_external_authority_configuration

        out["external_authority_configuration"] = (
            aws_sdk_ec2.types.ipam_scope_external_authority_configuration.deserialize_ec2_query(
                child_external_authority_configuration
            )
        )
    return out
