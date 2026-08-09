"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPrefixListResolverTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.boxed_long
    import capo_ec2.types.ipam_prefix_list_resolver_id
    import capo_ec2.types.ipam_prefix_list_resolver_target_id
    import capo_ec2.types.ipam_prefix_list_resolver_target_state
    import capo_ec2.types.prefix_list_resource_id
    import capo_ec2.types.resource_arn
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class IpamPrefixListResolverTarget(TypedDict, closed=True):
    ipam_prefix_list_resolver_target_id: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_target_id.IpamPrefixListResolverTargetId"
    ]
    """<p>The ID of the IPAM prefix list resolver target.</p>"""
    ipam_prefix_list_resolver_target_arn: NotRequired[
        "capo_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IPAM prefix list resolver target.</p>"""
    ipam_prefix_list_resolver_id: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_id.IpamPrefixListResolverId"
    ]
    """<p>The ID of the IPAM prefix list resolver associated with this target.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the IPAM prefix list resolver target.</p>"""
    prefix_list_id: NotRequired[
        "capo_ec2.types.prefix_list_resource_id.PrefixListResourceId"
    ]
    """<p>The ID of the managed prefix list associated with this target.</p>"""
    prefix_list_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services Region where the prefix list associated with this target is located.</p>"""
    desired_version: NotRequired["capo_ec2.types.boxed_long.BoxedLong"]
    """<p>The desired version of the prefix list that this target should synchronize with.</p>"""
    last_synced_version: NotRequired["capo_ec2.types.boxed_long.BoxedLong"]
    """<p>The version of the prefix list that was last successfully synchronized by this target.</p>"""
    track_latest_version: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether this target automatically tracks the latest version of the prefix list.</p>"""
    state_message: NotRequired["capo_ec2.types.string.String"]
    """<p>A message describing the current state of the IPAM prefix list resolver target, including any error information.</p>"""
    state: NotRequired[
        "capo_ec2.types.ipam_prefix_list_resolver_target_state.IpamPrefixListResolverTargetState"
    ]
    """<p>The current state of the IPAM prefix list resolver target. Valid values include <code>create-in-progress</code>, <code>create-complete</code>, <code>create-failed</code>, <code>modify-in-progress</code>, <code>modify-complete</code>, <code>modify-failed</code>, <code>delete-in-progress</code>, <code>delete-complete</code>, and <code>delete-failed</code>.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the IPAM prefix list resolver target.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamPrefixListResolverTarget, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_prefix_list_resolver_target_id" in value:
        pairs.append(
            (
                f"{key_prefix}IpamPrefixListResolverTargetId",
                str(value["ipam_prefix_list_resolver_target_id"]),
            )
        )
    if "ipam_prefix_list_resolver_target_arn" in value:
        pairs.append(
            (
                f"{key_prefix}IpamPrefixListResolverTargetArn",
                str(value["ipam_prefix_list_resolver_target_arn"]),
            )
        )
    if "ipam_prefix_list_resolver_id" in value:
        pairs.append(
            (
                f"{key_prefix}IpamPrefixListResolverId",
                str(value["ipam_prefix_list_resolver_id"]),
            )
        )
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "prefix_list_id" in value:
        pairs.append((f"{key_prefix}PrefixListId", str(value["prefix_list_id"])))
    if "prefix_list_region" in value:
        pairs.append(
            (f"{key_prefix}PrefixListRegion", str(value["prefix_list_region"]))
        )
    if "desired_version" in value:
        pairs.append((f"{key_prefix}DesiredVersion", str(value["desired_version"])))
    if "last_synced_version" in value:
        pairs.append(
            (f"{key_prefix}LastSyncedVersion", str(value["last_synced_version"]))
        )
    if "track_latest_version" in value:
        pairs.append(
            (
                f"{key_prefix}TrackLatestVersion",
                "true" if value["track_latest_version"] else "false",
            )
        )
    if "state_message" in value:
        pairs.append((f"{key_prefix}StateMessage", str(value["state_message"])))
    if "state" in value:
        import capo_ec2.types.ipam_prefix_list_resolver_target_state

        capo_ec2.types.ipam_prefix_list_resolver_target_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> IpamPrefixListResolverTarget:
    out: IpamPrefixListResolverTarget = {}  # type: ignore[typeddict-item]
    child_ipam_prefix_list_resolver_target_id = el.find(
        "ipamPrefixListResolverTargetId"
    )
    if child_ipam_prefix_list_resolver_target_id is not None:
        out["ipam_prefix_list_resolver_target_id"] = str(
            child_ipam_prefix_list_resolver_target_id.text or ""
        )
    child_ipam_prefix_list_resolver_target_arn = el.find(
        "ipamPrefixListResolverTargetArn"
    )
    if child_ipam_prefix_list_resolver_target_arn is not None:
        out["ipam_prefix_list_resolver_target_arn"] = str(
            child_ipam_prefix_list_resolver_target_arn.text or ""
        )
    child_ipam_prefix_list_resolver_id = el.find("ipamPrefixListResolverId")
    if child_ipam_prefix_list_resolver_id is not None:
        out["ipam_prefix_list_resolver_id"] = str(
            child_ipam_prefix_list_resolver_id.text or ""
        )
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_prefix_list_id = el.find("prefixListId")
    if child_prefix_list_id is not None:
        out["prefix_list_id"] = str(child_prefix_list_id.text or "")
    child_prefix_list_region = el.find("prefixListRegion")
    if child_prefix_list_region is not None:
        out["prefix_list_region"] = str(child_prefix_list_region.text or "")
    child_desired_version = el.find("desiredVersion")
    if child_desired_version is not None:
        out["desired_version"] = int(child_desired_version.text or "")
    child_last_synced_version = el.find("lastSyncedVersion")
    if child_last_synced_version is not None:
        out["last_synced_version"] = int(child_last_synced_version.text or "")
    child_track_latest_version = el.find("trackLatestVersion")
    if child_track_latest_version is not None:
        out["track_latest_version"] = (
            child_track_latest_version.text or ""
        ).lower() == "true"
    child_state_message = el.find("stateMessage")
    if child_state_message is not None:
        out["state_message"] = str(child_state_message.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.ipam_prefix_list_resolver_target_state

        out["state"] = (
            capo_ec2.types.ipam_prefix_list_resolver_target_state.deserialize_ec2_query(
                child_state
            )
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out
