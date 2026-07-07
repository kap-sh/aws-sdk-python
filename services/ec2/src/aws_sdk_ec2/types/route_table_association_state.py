"""Generated from Smithy shape ``com.amazonaws.ec2#RouteTableAssociationState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_table_association_state_code
    import aws_sdk_ec2.types.string


class RouteTableAssociationState(TypedDict, closed=True):
    state: NotRequired[
        "aws_sdk_ec2.types.route_table_association_state_code.RouteTableAssociationStateCode"
    ]
    """<p>The state of the association.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status message, if applicable.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RouteTableAssociationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "state" in value:
        import aws_sdk_ec2.types.route_table_association_state_code

        aws_sdk_ec2.types.route_table_association_state_code.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "status_message" in value:
        pairs.append((f"{prefix}.StatusMessage", str(value["status_message"])))


def deserialize_ec2_query(el: Element) -> RouteTableAssociationState:
    out: RouteTableAssociationState = {}  # type: ignore[typeddict-item]
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.route_table_association_state_code

        out["state"] = (
            aws_sdk_ec2.types.route_table_association_state_code.deserialize_ec2_query(
                child_state
            )
        )
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    return out
