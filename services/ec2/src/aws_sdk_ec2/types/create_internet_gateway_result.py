"""Generated from Smithy shape ``com.amazonaws.ec2#CreateInternetGatewayResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.internet_gateway


class CreateInternetGatewayResult(TypedDict, closed=True):
    internet_gateway: NotRequired["aws_sdk_ec2.types.internet_gateway.InternetGateway"]
    """<p>Information about the internet gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateInternetGatewayResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "internet_gateway" in value:
        import aws_sdk_ec2.types.internet_gateway

        aws_sdk_ec2.types.internet_gateway.serialize_ec2_query(
            value["internet_gateway"], pairs, f"{prefix}.InternetGateway"
        )


def deserialize_ec2_query(el: Element) -> CreateInternetGatewayResult:
    out: CreateInternetGatewayResult = {}  # type: ignore[typeddict-item]
    child_internet_gateway = el.find("InternetGateway")
    if child_internet_gateway is not None:
        import aws_sdk_ec2.types.internet_gateway

        out["internet_gateway"] = (
            aws_sdk_ec2.types.internet_gateway.deserialize_ec2_query(
                child_internet_gateway
            )
        )
    return out
