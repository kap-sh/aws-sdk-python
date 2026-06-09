"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.volume_status_name


class VolumeStatusDetails(TypedDict):
    name: NotRequired["aws_sdk_ec2.types.volume_status_name.VolumeStatusName"]
    """<p>The name of the volume status.</p> <ul> <li> <p> <code>io-enabled</code> - Indicates the volume I/O status. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-volume-checks.html\">Amazon EBS volume status checks</a>.</p> </li> <li> <p> <code>io-performance</code> - Indicates the volume performance status. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-volume-checks.html\">Amazon EBS volume status checks</a>.</p> </li> <li> <p> <code>initialization-state</code> - Indicates the status of the volume initialization process. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html\">Initialize Amazon EBS volumes</a>.</p> </li> </ul>"""
    status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The intended status of the volume status.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VolumeStatusDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        import aws_sdk_ec2.types.volume_status_name

        aws_sdk_ec2.types.volume_status_name.serialize_ec2_query(
            value["name"], pairs, f"{prefix}.Name"
        )
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))


def deserialize_ec2_query(el: Element) -> VolumeStatusDetails:
    out: VolumeStatusDetails = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        import aws_sdk_ec2.types.volume_status_name

        out["name"] = aws_sdk_ec2.types.volume_status_name.deserialize_ec2_query(
            child_name
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
