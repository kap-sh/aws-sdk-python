"""Generated from Smithy shape ``com.amazonaws.ec2#Volume``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.integer
    import capo_ec2.types.operator_response
    import capo_ec2.types.sse_type
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.volume_attachment_list
    import capo_ec2.types.volume_state
    import capo_ec2.types.volume_type


class Volume(TypedDict, closed=True):
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Availability Zone for the volume.</p>"""
    outpost_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost.</p>"""
    source_volume_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the source volume from which the volume copy was created. Only for volume copies.</p>"""
    iops: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of I/O operations per second (IOPS). For <code>gp3</code>, <code>io1</code>, and <code>io2</code> volumes, this represents the number of IOPS that are provisioned for the volume. For <code>gp2</code> volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the volume.</p>"""
    volume_type: NotRequired["capo_ec2.types.volume_type.VolumeType"]
    """<p>The volume type.</p>"""
    fast_restored: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<note> <p>This parameter is not returned by CreateVolume.</p> </note> <p>Indicates whether the volume was created using fast snapshot restore.</p>"""
    multi_attach_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether Amazon EBS Multi-Attach is enabled.</p>"""
    throughput: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The throughput that the volume supports, in MiB/s.</p>"""
    sse_type: NotRequired["capo_ec2.types.sse_type.SSEType"]
    """<note> <p>This parameter is not returned by CreateVolume.</p> </note> <p>Reserved for future use.</p>"""
    operator: NotRequired["capo_ec2.types.operator_response.OperatorResponse"]
    """<p>The service provider that manages the volume.</p>"""
    volume_initialization_rate: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate) specified for the volume during creation, in MiB/s. If no volume initialization rate was specified, the value is <code>null</code>.</p>"""
    volume_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the volume.</p>"""
    size: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The size of the volume, in GiBs.</p>"""
    snapshot_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The snapshot from which the volume was created, if applicable.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone for the volume.</p>"""
    state: NotRequired["capo_ec2.types.volume_state.VolumeState"]
    """<p>The volume state.</p>"""
    create_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time stamp when volume creation was initiated.</p>"""
    attachments: NotRequired[
        "capo_ec2.types.volume_attachment_list.VolumeAttachmentList"
    ]
    """<note> <p>This parameter is not returned by CreateVolume.</p> </note> <p>Information about the volume attachments.</p>"""
    encrypted: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the volume is encrypted.</p>"""
    kms_key_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the KMS key that was used to protect the volume encryption key for the volume.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Volume, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "outpost_arn" in value:
        pairs.append((f"{key_prefix}OutpostArn", str(value["outpost_arn"])))
    if "source_volume_id" in value:
        pairs.append((f"{key_prefix}SourceVolumeId", str(value["source_volume_id"])))
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "volume_type" in value:
        import capo_ec2.types.volume_type

        capo_ec2.types.volume_type.serialize_ec2_query(
            value["volume_type"], pairs, f"{key_prefix}VolumeType"
        )
    if "fast_restored" in value:
        pairs.append(
            (f"{key_prefix}FastRestored", "true" if value["fast_restored"] else "false")
        )
    if "multi_attach_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}MultiAttachEnabled",
                "true" if value["multi_attach_enabled"] else "false",
            )
        )
    if "throughput" in value:
        pairs.append((f"{key_prefix}Throughput", str(value["throughput"])))
    if "sse_type" in value:
        import capo_ec2.types.sse_type

        capo_ec2.types.sse_type.serialize_ec2_query(
            value["sse_type"], pairs, f"{key_prefix}SseType"
        )
    if "operator" in value:
        import capo_ec2.types.operator_response

        capo_ec2.types.operator_response.serialize_ec2_query(
            value["operator"], pairs, f"{key_prefix}Operator"
        )
    if "volume_initialization_rate" in value:
        pairs.append(
            (
                f"{key_prefix}VolumeInitializationRate",
                str(value["volume_initialization_rate"]),
            )
        )
    if "volume_id" in value:
        pairs.append((f"{key_prefix}VolumeId", str(value["volume_id"])))
    if "size" in value:
        pairs.append((f"{key_prefix}Size", str(value["size"])))
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "state" in value:
        import capo_ec2.types.volume_state

        capo_ec2.types.volume_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}Status"
        )
    if "create_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["create_time"], pairs, f"{key_prefix}CreateTime"
        )
    if "attachments" in value:
        import capo_ec2.types.volume_attachment_list

        capo_ec2.types.volume_attachment_list.serialize_ec2_query(
            value["attachments"], pairs, f"{key_prefix}AttachmentSet"
        )
    if "encrypted" in value:
        pairs.append(
            (f"{key_prefix}Encrypted", "true" if value["encrypted"] else "false")
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))


def deserialize_ec2_query(el: Element) -> Volume:
    out: Volume = {}  # type: ignore[typeddict-item]
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_outpost_arn = el.find("outpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_source_volume_id = el.find("sourceVolumeId")
    if child_source_volume_id is not None:
        out["source_volume_id"] = str(child_source_volume_id.text or "")
    child_iops = el.find("iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_volume_type = el.find("volumeType")
    if child_volume_type is not None:
        import capo_ec2.types.volume_type

        out["volume_type"] = capo_ec2.types.volume_type.deserialize_ec2_query(
            child_volume_type
        )
    child_fast_restored = el.find("fastRestored")
    if child_fast_restored is not None:
        out["fast_restored"] = (child_fast_restored.text or "").lower() == "true"
    child_multi_attach_enabled = el.find("multiAttachEnabled")
    if child_multi_attach_enabled is not None:
        out["multi_attach_enabled"] = (
            child_multi_attach_enabled.text or ""
        ).lower() == "true"
    child_throughput = el.find("throughput")
    if child_throughput is not None:
        out["throughput"] = int(child_throughput.text or "")
    child_sse_type = el.find("sseType")
    if child_sse_type is not None:
        import capo_ec2.types.sse_type

        out["sse_type"] = capo_ec2.types.sse_type.deserialize_ec2_query(child_sse_type)
    child_operator = el.find("operator")
    if child_operator is not None:
        import capo_ec2.types.operator_response

        out["operator"] = capo_ec2.types.operator_response.deserialize_ec2_query(
            child_operator
        )
    child_volume_initialization_rate = el.find("volumeInitializationRate")
    if child_volume_initialization_rate is not None:
        out["volume_initialization_rate"] = int(
            child_volume_initialization_rate.text or ""
        )
    child_volume_id = el.find("volumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    child_size = el.find("size")
    if child_size is not None:
        out["size"] = int(child_size.text or "")
    child_snapshot_id = el.find("snapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_state = el.find("status")
    if child_state is not None:
        import capo_ec2.types.volume_state

        out["state"] = capo_ec2.types.volume_state.deserialize_ec2_query(child_state)
    child_create_time = el.find("createTime")
    if child_create_time is not None:
        import capo_ec2.types.date_time

        out["create_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_create_time
        )
    child_attachments = el.find("attachmentSet")
    if child_attachments is not None:
        import capo_ec2.types.volume_attachment_list

        out["attachments"] = (
            capo_ec2.types.volume_attachment_list.deserialize_ec2_query(
                child_attachments
            )
        )
    child_encrypted = el.find("encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_kms_key_id = el.find("kmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    return out
