"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotFleetRequestsSuccessItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.batch_state
    import aws_sdk_ec2.types.string


class CancelSpotFleetRequestsSuccessItem(TypedDict, closed=True):
    current_spot_fleet_request_state: NotRequired[
        "aws_sdk_ec2.types.batch_state.BatchState"
    ]
    """<p>The current state of the Spot Fleet request.</p>"""
    previous_spot_fleet_request_state: NotRequired[
        "aws_sdk_ec2.types.batch_state.BatchState"
    ]
    """<p>The previous state of the Spot Fleet request.</p>"""
    spot_fleet_request_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Spot Fleet request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelSpotFleetRequestsSuccessItem, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "current_spot_fleet_request_state" in value:
        import aws_sdk_ec2.types.batch_state

        aws_sdk_ec2.types.batch_state.serialize_ec2_query(
            value["current_spot_fleet_request_state"],
            pairs,
            f"{prefix}.CurrentSpotFleetRequestState",
        )
    if "previous_spot_fleet_request_state" in value:
        import aws_sdk_ec2.types.batch_state

        aws_sdk_ec2.types.batch_state.serialize_ec2_query(
            value["previous_spot_fleet_request_state"],
            pairs,
            f"{prefix}.PreviousSpotFleetRequestState",
        )
    if "spot_fleet_request_id" in value:
        pairs.append(
            (f"{prefix}.SpotFleetRequestId", str(value["spot_fleet_request_id"]))
        )


def deserialize_ec2_query(el: Element) -> CancelSpotFleetRequestsSuccessItem:
    out: CancelSpotFleetRequestsSuccessItem = {}  # type: ignore[typeddict-item]
    child_current_spot_fleet_request_state = el.find("CurrentSpotFleetRequestState")
    if child_current_spot_fleet_request_state is not None:
        import aws_sdk_ec2.types.batch_state

        out["current_spot_fleet_request_state"] = (
            aws_sdk_ec2.types.batch_state.deserialize_ec2_query(
                child_current_spot_fleet_request_state
            )
        )
    child_previous_spot_fleet_request_state = el.find("PreviousSpotFleetRequestState")
    if child_previous_spot_fleet_request_state is not None:
        import aws_sdk_ec2.types.batch_state

        out["previous_spot_fleet_request_state"] = (
            aws_sdk_ec2.types.batch_state.deserialize_ec2_query(
                child_previous_spot_fleet_request_state
            )
        )
    child_spot_fleet_request_id = el.find("SpotFleetRequestId")
    if child_spot_fleet_request_id is not None:
        out["spot_fleet_request_id"] = str(child_spot_fleet_request_id.text or "")
    return out
