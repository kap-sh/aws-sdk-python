"""Generated from Smithy shape ``com.amazonaws.ec2#EbsInstanceBlockDeviceSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.volume_id


class EbsInstanceBlockDeviceSpecification(TypedDict):
    volume_id: NotRequired["aws_sdk_ec2.types.volume_id.VolumeId"]
    """<p>The ID of the EBS volume.</p>"""
    delete_on_termination: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the volume is deleted on instance termination.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EbsInstanceBlockDeviceSpecification,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "volume_id" in value:
        pairs.append((f"{prefix}.VolumeId", str(value["volume_id"])))
    if "delete_on_termination" in value:
        pairs.append(
            (
                f"{prefix}.DeleteOnTermination",
                "true" if value["delete_on_termination"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> EbsInstanceBlockDeviceSpecification:
    out: EbsInstanceBlockDeviceSpecification = {}  # type: ignore[typeddict-item]
    child_volume_id = el.find("VolumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    child_delete_on_termination = el.find("DeleteOnTermination")
    if child_delete_on_termination is not None:
        out["delete_on_termination"] = (
            child_delete_on_termination.text or ""
        ).lower() == "true"
    return out
