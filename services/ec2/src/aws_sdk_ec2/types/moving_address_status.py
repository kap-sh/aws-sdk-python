"""Generated from Smithy shape ``com.amazonaws.ec2#MovingAddressStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.move_status
    import aws_sdk_ec2.types.string


class MovingAddressStatus(TypedDict):
    move_status: NotRequired["aws_sdk_ec2.types.move_status.MoveStatus"]
    """<p>The status of the Elastic IP address that's being moved or restored.</p>"""
    public_ip: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Elastic IP address.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MovingAddressStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "move_status" in value:
        import aws_sdk_ec2.types.move_status

        aws_sdk_ec2.types.move_status.serialize_ec2_query(
            value["move_status"], pairs, f"{prefix}.MoveStatus"
        )
    if "public_ip" in value:
        pairs.append((f"{prefix}.PublicIp", str(value["public_ip"])))


def deserialize_ec2_query(el: Element) -> MovingAddressStatus:
    out: MovingAddressStatus = {}  # type: ignore[typeddict-item]
    child_move_status = el.find("MoveStatus")
    if child_move_status is not None:
        import aws_sdk_ec2.types.move_status

        out["move_status"] = aws_sdk_ec2.types.move_status.deserialize_ec2_query(
            child_move_status
        )
    child_public_ip = el.find("PublicIp")
    if child_public_ip is not None:
        out["public_ip"] = str(child_public_ip.text or "")
    return out
