"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteInstanceConnectEndpointResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ec2_instance_connect_endpoint


class DeleteInstanceConnectEndpointResult(TypedDict):
    instance_connect_endpoint: NotRequired[
        "aws_sdk_ec2.types.ec2_instance_connect_endpoint.Ec2InstanceConnectEndpoint"
    ]
    """<p>Information about the EC2 Instance Connect Endpoint.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteInstanceConnectEndpointResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_connect_endpoint" in value:
        import aws_sdk_ec2.types.ec2_instance_connect_endpoint

        aws_sdk_ec2.types.ec2_instance_connect_endpoint.serialize_ec2_query(
            value["instance_connect_endpoint"],
            pairs,
            f"{prefix}.InstanceConnectEndpoint",
        )


def deserialize_ec2_query(el: Element) -> DeleteInstanceConnectEndpointResult:
    out: DeleteInstanceConnectEndpointResult = {}  # type: ignore[typeddict-item]
    child_instance_connect_endpoint = el.find("InstanceConnectEndpoint")
    if child_instance_connect_endpoint is not None:
        import aws_sdk_ec2.types.ec2_instance_connect_endpoint

        out["instance_connect_endpoint"] = (
            aws_sdk_ec2.types.ec2_instance_connect_endpoint.deserialize_ec2_query(
                child_instance_connect_endpoint
            )
        )
    return out
