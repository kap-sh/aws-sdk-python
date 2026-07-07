"""Generated from Smithy shape ``com.amazonaws.ec2#VpcPeeringConnectionStateReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_peering_connection_state_reason_code


class VpcPeeringConnectionStateReason(TypedDict, closed=True):
    code: NotRequired[
        "aws_sdk_ec2.types.vpc_peering_connection_state_reason_code.VpcPeeringConnectionStateReasonCode"
    ]
    """<p>The status of the VPC peering connection.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message that provides more information about the status, if applicable.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcPeeringConnectionStateReason, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "code" in value:
        import aws_sdk_ec2.types.vpc_peering_connection_state_reason_code

        aws_sdk_ec2.types.vpc_peering_connection_state_reason_code.serialize_ec2_query(
            value["code"], pairs, f"{prefix}.Code"
        )
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_ec2_query(el: Element) -> VpcPeeringConnectionStateReason:
    out: VpcPeeringConnectionStateReason = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        import aws_sdk_ec2.types.vpc_peering_connection_state_reason_code

        out["code"] = (
            aws_sdk_ec2.types.vpc_peering_connection_state_reason_code.deserialize_ec2_query(
                child_code
            )
        )
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out
