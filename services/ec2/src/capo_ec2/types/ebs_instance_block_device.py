"""Generated from Smithy shape ``com.amazonaws.ec2#EbsInstanceBlockDevice``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.attachment_status
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.integer
    import capo_ec2.types.operator_response
    import capo_ec2.types.string


class EbsInstanceBlockDevice(TypedDict, closed=True):
    attach_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time stamp when the attachment initiated.</p>"""
    delete_on_termination: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the volume is deleted on instance termination.</p>"""
    status: NotRequired["capo_ec2.types.attachment_status.AttachmentStatus"]
    """<p>The attachment state.</p>"""
    volume_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the EBS volume.</p>"""
    associated_resource: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the Amazon Web Services-managed resource to which the volume is attached.</p>"""
    volume_owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the volume.</p> <p>This parameter is returned only for volumes that are attached to Amazon Web Services-managed resources.</p>"""
    operator: NotRequired["capo_ec2.types.operator_response.OperatorResponse"]
    """<p>The service provider that manages the EBS volume.</p>"""
    ebs_card_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The index of the EBS card. Some instance types support multiple EBS cards. The default EBS card index is 0.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EbsInstanceBlockDevice, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "attach_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["attach_time"], pairs, f"{key_prefix}AttachTime"
        )
    if "delete_on_termination" in value:
        pairs.append(
            (
                f"{key_prefix}DeleteOnTermination",
                "true" if value["delete_on_termination"] else "false",
            )
        )
    if "status" in value:
        import capo_ec2.types.attachment_status

        capo_ec2.types.attachment_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "volume_id" in value:
        pairs.append((f"{key_prefix}VolumeId", str(value["volume_id"])))
    if "associated_resource" in value:
        pairs.append(
            (f"{key_prefix}AssociatedResource", str(value["associated_resource"]))
        )
    if "volume_owner_id" in value:
        pairs.append((f"{key_prefix}VolumeOwnerId", str(value["volume_owner_id"])))
    if "operator" in value:
        import capo_ec2.types.operator_response

        capo_ec2.types.operator_response.serialize_ec2_query(
            value["operator"], pairs, f"{key_prefix}Operator"
        )
    if "ebs_card_index" in value:
        pairs.append((f"{key_prefix}EbsCardIndex", str(value["ebs_card_index"])))


def deserialize_ec2_query(el: Element) -> EbsInstanceBlockDevice:
    out: EbsInstanceBlockDevice = {}  # type: ignore[typeddict-item]
    child_attach_time = el.find("AttachTime")
    if child_attach_time is not None:
        import capo_ec2.types.date_time

        out["attach_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_attach_time
        )
    child_delete_on_termination = el.find("DeleteOnTermination")
    if child_delete_on_termination is not None:
        out["delete_on_termination"] = (
            child_delete_on_termination.text or ""
        ).lower() == "true"
    child_status = el.find("Status")
    if child_status is not None:
        import capo_ec2.types.attachment_status

        out["status"] = capo_ec2.types.attachment_status.deserialize_ec2_query(
            child_status
        )
    child_volume_id = el.find("VolumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    child_associated_resource = el.find("AssociatedResource")
    if child_associated_resource is not None:
        out["associated_resource"] = str(child_associated_resource.text or "")
    child_volume_owner_id = el.find("VolumeOwnerId")
    if child_volume_owner_id is not None:
        out["volume_owner_id"] = str(child_volume_owner_id.text or "")
    child_operator = el.find("Operator")
    if child_operator is not None:
        import capo_ec2.types.operator_response

        out["operator"] = capo_ec2.types.operator_response.deserialize_ec2_query(
            child_operator
        )
    child_ebs_card_index = el.find("EbsCardIndex")
    if child_ebs_card_index is not None:
        out["ebs_card_index"] = int(child_ebs_card_index.text or "")
    return out
