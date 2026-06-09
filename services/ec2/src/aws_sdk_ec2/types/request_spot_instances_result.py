"""Generated from Smithy shape ``com.amazonaws.ec2#RequestSpotInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_instance_request_list


class RequestSpotInstancesResult(TypedDict):
    spot_instance_requests: NotRequired[
        "aws_sdk_ec2.types.spot_instance_request_list.SpotInstanceRequestList"
    ]
    """<p>The Spot Instance requests.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RequestSpotInstancesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "spot_instance_requests" in value:
        import aws_sdk_ec2.types.spot_instance_request_list

        aws_sdk_ec2.types.spot_instance_request_list.serialize_ec2_query(
            value["spot_instance_requests"], pairs, f"{prefix}.SpotInstanceRequestSet"
        )


def deserialize_ec2_query(el: Element) -> RequestSpotInstancesResult:
    out: RequestSpotInstancesResult = {}  # type: ignore[typeddict-item]
    if el.find("SpotInstanceRequestSet") is not None:
        import aws_sdk_ec2.types.spot_instance_request_list

        out["spot_instance_requests"] = (
            aws_sdk_ec2.types.spot_instance_request_list.deserialize_ec2_query(
                el, "SpotInstanceRequestSet"
            )
        )
    return out
