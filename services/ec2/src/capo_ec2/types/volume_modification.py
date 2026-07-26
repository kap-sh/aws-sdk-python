"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeModification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.integer
    import capo_ec2.types.long
    import capo_ec2.types.operator_response
    import capo_ec2.types.string
    import capo_ec2.types.volume_modification_state
    import capo_ec2.types.volume_type


class VolumeModification(TypedDict, closed=True):
    volume_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the volume.</p>"""
    modification_state: NotRequired[
        "capo_ec2.types.volume_modification_state.VolumeModificationState"
    ]
    """<p>The current modification state.</p>"""
    status_message: NotRequired["capo_ec2.types.string.String"]
    """<p>A status message about the modification progress or failure.</p>"""
    target_size: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The target size of the volume, in GiB.</p>"""
    target_iops: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The target IOPS rate of the volume.</p>"""
    target_volume_type: NotRequired["capo_ec2.types.volume_type.VolumeType"]
    """<p>The target EBS volume type of the volume.</p>"""
    target_throughput: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The target throughput of the volume, in MiB/s.</p>"""
    target_multi_attach_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>The target setting for Amazon EBS Multi-Attach.</p>"""
    original_size: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The original size of the volume, in GiB.</p>"""
    original_iops: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The original IOPS rate of the volume.</p>"""
    original_volume_type: NotRequired["capo_ec2.types.volume_type.VolumeType"]
    """<p>The original EBS volume type of the volume.</p>"""
    original_throughput: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The original throughput of the volume, in MiB/s.</p>"""
    original_multi_attach_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>The original setting for Amazon EBS Multi-Attach.</p>"""
    progress: NotRequired["capo_ec2.types.long.Long"]
    """<p>The modification progress, from 0 to 100 percent complete.</p>"""
    start_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The modification start time.</p>"""
    end_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The modification completion or failure time.</p>"""
    operator: NotRequired["capo_ec2.types.operator_response.OperatorResponse"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VolumeModification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "volume_id" in value:
        pairs.append((f"{prefix}.VolumeId", str(value["volume_id"])))
    if "modification_state" in value:
        import capo_ec2.types.volume_modification_state

        capo_ec2.types.volume_modification_state.serialize_ec2_query(
            value["modification_state"], pairs, f"{prefix}.ModificationState"
        )
    if "status_message" in value:
        pairs.append((f"{prefix}.StatusMessage", str(value["status_message"])))
    if "target_size" in value:
        pairs.append((f"{prefix}.TargetSize", str(value["target_size"])))
    if "target_iops" in value:
        pairs.append((f"{prefix}.TargetIops", str(value["target_iops"])))
    if "target_volume_type" in value:
        import capo_ec2.types.volume_type

        capo_ec2.types.volume_type.serialize_ec2_query(
            value["target_volume_type"], pairs, f"{prefix}.TargetVolumeType"
        )
    if "target_throughput" in value:
        pairs.append((f"{prefix}.TargetThroughput", str(value["target_throughput"])))
    if "target_multi_attach_enabled" in value:
        pairs.append(
            (
                f"{prefix}.TargetMultiAttachEnabled",
                "true" if value["target_multi_attach_enabled"] else "false",
            )
        )
    if "original_size" in value:
        pairs.append((f"{prefix}.OriginalSize", str(value["original_size"])))
    if "original_iops" in value:
        pairs.append((f"{prefix}.OriginalIops", str(value["original_iops"])))
    if "original_volume_type" in value:
        import capo_ec2.types.volume_type

        capo_ec2.types.volume_type.serialize_ec2_query(
            value["original_volume_type"], pairs, f"{prefix}.OriginalVolumeType"
        )
    if "original_throughput" in value:
        pairs.append(
            (f"{prefix}.OriginalThroughput", str(value["original_throughput"]))
        )
    if "original_multi_attach_enabled" in value:
        pairs.append(
            (
                f"{prefix}.OriginalMultiAttachEnabled",
                "true" if value["original_multi_attach_enabled"] else "false",
            )
        )
    if "progress" in value:
        pairs.append((f"{prefix}.Progress", str(value["progress"])))
    if "start_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "end_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["end_time"], pairs, f"{prefix}.EndTime"
        )
    if "operator" in value:
        import capo_ec2.types.operator_response

        capo_ec2.types.operator_response.serialize_ec2_query(
            value["operator"], pairs, f"{prefix}.Operator"
        )


def deserialize_ec2_query(el: Element) -> VolumeModification:
    out: VolumeModification = {}  # type: ignore[typeddict-item]
    child_volume_id = el.find("VolumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    child_modification_state = el.find("ModificationState")
    if child_modification_state is not None:
        import capo_ec2.types.volume_modification_state

        out["modification_state"] = (
            capo_ec2.types.volume_modification_state.deserialize_ec2_query(
                child_modification_state
            )
        )
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_target_size = el.find("TargetSize")
    if child_target_size is not None:
        out["target_size"] = int(child_target_size.text or "")
    child_target_iops = el.find("TargetIops")
    if child_target_iops is not None:
        out["target_iops"] = int(child_target_iops.text or "")
    child_target_volume_type = el.find("TargetVolumeType")
    if child_target_volume_type is not None:
        import capo_ec2.types.volume_type

        out["target_volume_type"] = capo_ec2.types.volume_type.deserialize_ec2_query(
            child_target_volume_type
        )
    child_target_throughput = el.find("TargetThroughput")
    if child_target_throughput is not None:
        out["target_throughput"] = int(child_target_throughput.text or "")
    child_target_multi_attach_enabled = el.find("TargetMultiAttachEnabled")
    if child_target_multi_attach_enabled is not None:
        out["target_multi_attach_enabled"] = (
            child_target_multi_attach_enabled.text or ""
        ).lower() == "true"
    child_original_size = el.find("OriginalSize")
    if child_original_size is not None:
        out["original_size"] = int(child_original_size.text or "")
    child_original_iops = el.find("OriginalIops")
    if child_original_iops is not None:
        out["original_iops"] = int(child_original_iops.text or "")
    child_original_volume_type = el.find("OriginalVolumeType")
    if child_original_volume_type is not None:
        import capo_ec2.types.volume_type

        out["original_volume_type"] = capo_ec2.types.volume_type.deserialize_ec2_query(
            child_original_volume_type
        )
    child_original_throughput = el.find("OriginalThroughput")
    if child_original_throughput is not None:
        out["original_throughput"] = int(child_original_throughput.text or "")
    child_original_multi_attach_enabled = el.find("OriginalMultiAttachEnabled")
    if child_original_multi_attach_enabled is not None:
        out["original_multi_attach_enabled"] = (
            child_original_multi_attach_enabled.text or ""
        ).lower() == "true"
    child_progress = el.find("Progress")
    if child_progress is not None:
        out["progress"] = int(child_progress.text or "")
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_ec2.types.date_time

        out["start_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import capo_ec2.types.date_time

        out["end_time"] = capo_ec2.types.date_time.deserialize_ec2_query(child_end_time)
    child_operator = el.find("Operator")
    if child_operator is not None:
        import capo_ec2.types.operator_response

        out["operator"] = capo_ec2.types.operator_response.deserialize_ec2_query(
            child_operator
        )
    return out
