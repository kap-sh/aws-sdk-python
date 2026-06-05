"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcEndpointServiceConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.service_configuration
    import aws_sdk_ec2.types.string


class CreateVpcEndpointServiceConfigurationResult(TypedDict):
    service_configuration: NotRequired[
        "aws_sdk_ec2.types.service_configuration.ServiceConfiguration"
    ]
    """<p>Information about the service configuration.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVpcEndpointServiceConfigurationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "service_configuration" in value:
        import aws_sdk_ec2.types.service_configuration

        aws_sdk_ec2.types.service_configuration.serialize_ec2_query(
            value["service_configuration"], pairs, f"{prefix}.ServiceConfiguration"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateVpcEndpointServiceConfigurationResult:
    out: CreateVpcEndpointServiceConfigurationResult = {}  # type: ignore[typeddict-item]
    child_service_configuration = el.find("ServiceConfiguration")
    if child_service_configuration is not None:
        import aws_sdk_ec2.types.service_configuration

        out["service_configuration"] = (
            aws_sdk_ec2.types.service_configuration.deserialize_ec2_query(
                child_service_configuration
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
