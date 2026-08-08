"""Generated from Smithy shape ``com.amazonaws.ec2#DisableFastSnapshotRestoreSuccessItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fast_snapshot_restore_state_code
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class DisableFastSnapshotRestoreSuccessItem(TypedDict, closed=True):
    snapshot_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the snapshot.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Availability Zone.</p>"""
    state: NotRequired[
        "capo_ec2.types.fast_snapshot_restore_state_code.FastSnapshotRestoreStateCode"
    ]
    """<p>The state of fast snapshot restores for the snapshot.</p>"""
    state_transition_reason: NotRequired["capo_ec2.types.string.String"]
    """<p>The reason for the state transition. The possible values are as follows:</p> <ul> <li> <p> <code>Client.UserInitiated</code> - The state successfully transitioned to <code>enabling</code> or <code>disabling</code>.</p> </li> <li> <p> <code>Client.UserInitiated - Lifecycle state transition</code> - The state successfully transitioned to <code>optimizing</code>, <code>enabled</code>, or <code>disabled</code>.</p> </li> </ul>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that enabled fast snapshot restores on the snapshot.</p>"""
    owner_alias: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services owner alias that enabled fast snapshot restores on the snapshot. This is intended for future use.</p>"""
    enabling_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time at which fast snapshot restores entered the <code>enabling</code> state.</p>"""
    optimizing_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time at which fast snapshot restores entered the <code>optimizing</code> state.</p>"""
    enabled_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time at which fast snapshot restores entered the <code>enabled</code> state.</p>"""
    disabling_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time at which fast snapshot restores entered the <code>disabling</code> state.</p>"""
    disabled_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time at which fast snapshot restores entered the <code>disabled</code> state.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableFastSnapshotRestoreSuccessItem,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "state" in value:
        import capo_ec2.types.fast_snapshot_restore_state_code

        capo_ec2.types.fast_snapshot_restore_state_code.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "state_transition_reason" in value:
        pairs.append(
            (
                f"{key_prefix}StateTransitionReason",
                str(value["state_transition_reason"]),
            )
        )
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "owner_alias" in value:
        pairs.append((f"{key_prefix}OwnerAlias", str(value["owner_alias"])))
    if "enabling_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["enabling_time"], pairs, f"{key_prefix}EnablingTime"
        )
    if "optimizing_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["optimizing_time"], pairs, f"{key_prefix}OptimizingTime"
        )
    if "enabled_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["enabled_time"], pairs, f"{key_prefix}EnabledTime"
        )
    if "disabling_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["disabling_time"], pairs, f"{key_prefix}DisablingTime"
        )
    if "disabled_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["disabled_time"], pairs, f"{key_prefix}DisabledTime"
        )


def deserialize_ec2_query(el: Element) -> DisableFastSnapshotRestoreSuccessItem:
    out: DisableFastSnapshotRestoreSuccessItem = {}  # type: ignore[typeddict-item]
    child_snapshot_id = el.find("snapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.fast_snapshot_restore_state_code

        out["state"] = (
            capo_ec2.types.fast_snapshot_restore_state_code.deserialize_ec2_query(
                child_state
            )
        )
    child_state_transition_reason = el.find("stateTransitionReason")
    if child_state_transition_reason is not None:
        out["state_transition_reason"] = str(child_state_transition_reason.text or "")
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_owner_alias = el.find("ownerAlias")
    if child_owner_alias is not None:
        out["owner_alias"] = str(child_owner_alias.text or "")
    child_enabling_time = el.find("enablingTime")
    if child_enabling_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["enabling_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_enabling_time
            )
        )
    child_optimizing_time = el.find("optimizingTime")
    if child_optimizing_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["optimizing_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_optimizing_time
            )
        )
    child_enabled_time = el.find("enabledTime")
    if child_enabled_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["enabled_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_enabled_time
            )
        )
    child_disabling_time = el.find("disablingTime")
    if child_disabling_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["disabling_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_disabling_time
            )
        )
    child_disabled_time = el.find("disabledTime")
    if child_disabled_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["disabled_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_disabled_time
            )
        )
    return out
