"""Generated from Smithy shape ``com.amazonaws.ec2#CreateInstanceConnectEndpointResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ec2_instance_connect_endpoint
    import aws_sdk_ec2.types.string


class CreateInstanceConnectEndpointResult(TypedDict):
    instance_connect_endpoint: NotRequired[
        "aws_sdk_ec2.types.ec2_instance_connect_endpoint.Ec2InstanceConnectEndpoint"
    ]
    """<p>Information about the EC2 Instance Connect Endpoint.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive idempotency token provided by the client in the the request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateInstanceConnectEndpointResult,
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
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateInstanceConnectEndpointResult:
    out: CreateInstanceConnectEndpointResult = {}  # type: ignore[typeddict-item]
    child_instance_connect_endpoint = el.find("InstanceConnectEndpoint")
    if child_instance_connect_endpoint is not None:
        import aws_sdk_ec2.types.ec2_instance_connect_endpoint

        out["instance_connect_endpoint"] = (
            aws_sdk_ec2.types.ec2_instance_connect_endpoint.deserialize_ec2_query(
                child_instance_connect_endpoint
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
