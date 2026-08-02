"""Generated from Smithy shape ``com.amazonaws.ec2#VpcBlockPublicAccessExclusion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.internet_gateway_exclusion_mode
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.resource_arn
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.vpc_block_public_access_exclusion_id
    import capo_ec2.types.vpc_block_public_access_exclusion_state


class VpcBlockPublicAccessExclusion(TypedDict, closed=True):
    exclusion_id: NotRequired[
        "capo_ec2.types.vpc_block_public_access_exclusion_id.VpcBlockPublicAccessExclusionId"
    ]
    """<p>The ID of the exclusion.</p>"""
    internet_gateway_exclusion_mode: NotRequired[
        "capo_ec2.types.internet_gateway_exclusion_mode.InternetGatewayExclusionMode"
    ]
    """<p>The exclusion mode for internet gateway traffic.</p> <ul> <li> <p> <code>allow-bidirectional</code>: Allow all internet traffic to and from the excluded VPCs and subnets.</p> </li> <li> <p> <code>allow-egress</code>: Allow outbound internet traffic from the excluded VPCs and subnets. Block inbound internet traffic to the excluded VPCs and subnets. Only applies when VPC Block Public Access is set to Bidirectional.</p> </li> </ul>"""
    resource_arn: NotRequired["capo_ec2.types.resource_arn.ResourceArn"]
    """<p>The ARN of the exclusion.</p>"""
    state: NotRequired[
        "capo_ec2.types.vpc_block_public_access_exclusion_state.VpcBlockPublicAccessExclusionState"
    ]
    """<p>The state of the exclusion.</p>"""
    reason: NotRequired["capo_ec2.types.string.String"]
    """<p>The reason for the current exclusion state.</p>"""
    creation_timestamp: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>When the exclusion was created.</p>"""
    last_update_timestamp: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>When the exclusion was last updated.</p>"""
    deletion_timestamp: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>When the exclusion was deleted.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p> <code>tag</code> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcBlockPublicAccessExclusion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "exclusion_id" in value:
        pairs.append((f"{key_prefix}ExclusionId", str(value["exclusion_id"])))
    if "internet_gateway_exclusion_mode" in value:
        import capo_ec2.types.internet_gateway_exclusion_mode

        capo_ec2.types.internet_gateway_exclusion_mode.serialize_ec2_query(
            value["internet_gateway_exclusion_mode"],
            pairs,
            f"{key_prefix}InternetGatewayExclusionMode",
        )
    if "resource_arn" in value:
        pairs.append((f"{key_prefix}ResourceArn", str(value["resource_arn"])))
    if "state" in value:
        import capo_ec2.types.vpc_block_public_access_exclusion_state

        capo_ec2.types.vpc_block_public_access_exclusion_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "reason" in value:
        pairs.append((f"{key_prefix}Reason", str(value["reason"])))
    if "creation_timestamp" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["creation_timestamp"], pairs, f"{key_prefix}CreationTimestamp"
        )
    if "last_update_timestamp" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["last_update_timestamp"], pairs, f"{key_prefix}LastUpdateTimestamp"
        )
    if "deletion_timestamp" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["deletion_timestamp"], pairs, f"{key_prefix}DeletionTimestamp"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> VpcBlockPublicAccessExclusion:
    out: VpcBlockPublicAccessExclusion = {}  # type: ignore[typeddict-item]
    child_exclusion_id = el.find("ExclusionId")
    if child_exclusion_id is not None:
        out["exclusion_id"] = str(child_exclusion_id.text or "")
    child_internet_gateway_exclusion_mode = el.find("InternetGatewayExclusionMode")
    if child_internet_gateway_exclusion_mode is not None:
        import capo_ec2.types.internet_gateway_exclusion_mode

        out["internet_gateway_exclusion_mode"] = (
            capo_ec2.types.internet_gateway_exclusion_mode.deserialize_ec2_query(
                child_internet_gateway_exclusion_mode
            )
        )
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.vpc_block_public_access_exclusion_state

        out["state"] = (
            capo_ec2.types.vpc_block_public_access_exclusion_state.deserialize_ec2_query(
                child_state
            )
        )
    child_reason = el.find("Reason")
    if child_reason is not None:
        out["reason"] = str(child_reason.text or "")
    child_creation_timestamp = el.find("CreationTimestamp")
    if child_creation_timestamp is not None:
        import capo_ec2.types.millisecond_date_time

        out["creation_timestamp"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_creation_timestamp
            )
        )
    child_last_update_timestamp = el.find("LastUpdateTimestamp")
    if child_last_update_timestamp is not None:
        import capo_ec2.types.millisecond_date_time

        out["last_update_timestamp"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_last_update_timestamp
            )
        )
    child_deletion_timestamp = el.find("DeletionTimestamp")
    if child_deletion_timestamp is not None:
        import capo_ec2.types.millisecond_date_time

        out["deletion_timestamp"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_deletion_timestamp
            )
        )
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
