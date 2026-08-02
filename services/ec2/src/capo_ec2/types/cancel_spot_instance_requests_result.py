"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotInstanceRequestsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.cancelled_spot_instance_request_list


class CancelSpotInstanceRequestsResult(TypedDict, closed=True):
    cancelled_spot_instance_requests: NotRequired[
        "capo_ec2.types.cancelled_spot_instance_request_list.CancelledSpotInstanceRequestList"
    ]
    """<p>The Spot Instance requests.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelSpotInstanceRequestsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cancelled_spot_instance_requests" in value:
        import capo_ec2.types.cancelled_spot_instance_request_list

        capo_ec2.types.cancelled_spot_instance_request_list.serialize_ec2_query(
            value["cancelled_spot_instance_requests"],
            pairs,
            f"{key_prefix}SpotInstanceRequestSet",
        )


def deserialize_ec2_query(el: Element) -> CancelSpotInstanceRequestsResult:
    out: CancelSpotInstanceRequestsResult = {}  # type: ignore[typeddict-item]
    if el.find("SpotInstanceRequestSet") is not None:
        import capo_ec2.types.cancelled_spot_instance_request_list

        out["cancelled_spot_instance_requests"] = (
            capo_ec2.types.cancelled_spot_instance_request_list.deserialize_ec2_query(
                el, "SpotInstanceRequestSet"
            )
        )
    return out
