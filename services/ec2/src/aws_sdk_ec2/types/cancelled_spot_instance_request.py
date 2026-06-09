"""Generated from Smithy shape ``com.amazonaws.ec2#CancelledSpotInstanceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancel_spot_instance_request_state
    import aws_sdk_ec2.types.string


class CancelledSpotInstanceRequest(TypedDict):
    spot_instance_request_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Spot Instance request.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.cancel_spot_instance_request_state.CancelSpotInstanceRequestState"
    ]
    """<p>The state of the Spot Instance request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelledSpotInstanceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "spot_instance_request_id" in value:
        pairs.append(
            (f"{prefix}.SpotInstanceRequestId", str(value["spot_instance_request_id"]))
        )
    if "state" in value:
        import aws_sdk_ec2.types.cancel_spot_instance_request_state

        aws_sdk_ec2.types.cancel_spot_instance_request_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )


def deserialize_ec2_query(el: Element) -> CancelledSpotInstanceRequest:
    out: CancelledSpotInstanceRequest = {}  # type: ignore[typeddict-item]
    child_spot_instance_request_id = el.find("SpotInstanceRequestId")
    if child_spot_instance_request_id is not None:
        out["spot_instance_request_id"] = str(child_spot_instance_request_id.text or "")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.cancel_spot_instance_request_state

        out["state"] = (
            aws_sdk_ec2.types.cancel_spot_instance_request_state.deserialize_ec2_query(
                child_state
            )
        )
    return out
