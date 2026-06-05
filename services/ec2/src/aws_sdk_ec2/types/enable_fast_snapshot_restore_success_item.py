"""Generated from Smithy shape ``com.amazonaws.ec2#EnableFastSnapshotRestoreSuccessItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fast_snapshot_restore_state_code
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class EnableFastSnapshotRestoreSuccessItem(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the snapshot.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.fast_snapshot_restore_state_code.FastSnapshotRestoreStateCode"
    ]
    """<p>The state of fast snapshot restores.</p>"""
    state_transition_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason for the state transition. The possible values are as follows:</p> <ul> <li> <p> <code>Client.UserInitiated</code> - The state successfully transitioned to <code>enabling</code> or <code>disabling</code>.</p> </li> <li> <p> <code>Client.UserInitiated - Lifecycle state transition</code> - The state successfully transitioned to <code>optimizing</code>, <code>enabled</code>, or <code>disabled</code>.</p> </li> </ul>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that enabled fast snapshot restores on the snapshot.</p>"""
    owner_alias: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services owner alias that enabled fast snapshot restores on the snapshot. This is intended for future use.</p>"""
    enabling_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time at which fast snapshot restores entered the <code>enabling</code> state.</p>"""
    optimizing_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time at which fast snapshot restores entered the <code>optimizing</code> state.</p>"""
    enabled_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time at which fast snapshot restores entered the <code>enabled</code> state.</p>"""
    disabling_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time at which fast snapshot restores entered the <code>disabling</code> state.</p>"""
    disabled_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time at which fast snapshot restores entered the <code>disabled</code> state.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableFastSnapshotRestoreSuccessItem,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "snapshot_id" in value:
        pairs.append((f"{prefix}.SnapshotId", str(value["snapshot_id"])))
    if "availability_zone" in value:
        pairs.append((f"{prefix}.AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "state" in value:
        import aws_sdk_ec2.types.fast_snapshot_restore_state_code

        aws_sdk_ec2.types.fast_snapshot_restore_state_code.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "state_transition_reason" in value:
        pairs.append(
            (f"{prefix}.StateTransitionReason", str(value["state_transition_reason"]))
        )
    if "owner_id" in value:
        pairs.append((f"{prefix}.OwnerId", str(value["owner_id"])))
    if "owner_alias" in value:
        pairs.append((f"{prefix}.OwnerAlias", str(value["owner_alias"])))
    if "enabling_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["enabling_time"], pairs, f"{prefix}.EnablingTime"
        )
    if "optimizing_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["optimizing_time"], pairs, f"{prefix}.OptimizingTime"
        )
    if "enabled_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["enabled_time"], pairs, f"{prefix}.EnabledTime"
        )
    if "disabling_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["disabling_time"], pairs, f"{prefix}.DisablingTime"
        )
    if "disabled_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["disabled_time"], pairs, f"{prefix}.DisabledTime"
        )


def deserialize_ec2_query(el: Element) -> EnableFastSnapshotRestoreSuccessItem:
    out: EnableFastSnapshotRestoreSuccessItem = {}  # type: ignore[typeddict-item]
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.fast_snapshot_restore_state_code

        out["state"] = (
            aws_sdk_ec2.types.fast_snapshot_restore_state_code.deserialize_ec2_query(
                child_state
            )
        )
    child_state_transition_reason = el.find("StateTransitionReason")
    if child_state_transition_reason is not None:
        out["state_transition_reason"] = str(child_state_transition_reason.text or "")
    child_owner_id = el.find("OwnerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_owner_alias = el.find("OwnerAlias")
    if child_owner_alias is not None:
        out["owner_alias"] = str(child_owner_alias.text or "")
    child_enabling_time = el.find("EnablingTime")
    if child_enabling_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["enabling_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_enabling_time
            )
        )
    child_optimizing_time = el.find("OptimizingTime")
    if child_optimizing_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["optimizing_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_optimizing_time
            )
        )
    child_enabled_time = el.find("EnabledTime")
    if child_enabled_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["enabled_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_enabled_time
            )
        )
    child_disabling_time = el.find("DisablingTime")
    if child_disabling_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["disabling_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_disabling_time
            )
        )
    child_disabled_time = el.find("DisabledTime")
    if child_disabled_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["disabled_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_disabled_time
            )
        )
    return out
