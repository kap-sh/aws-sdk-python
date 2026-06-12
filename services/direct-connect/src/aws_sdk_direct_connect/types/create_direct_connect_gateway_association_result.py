"""Generated from Smithy shape ``com.amazonaws.directconnect#CreateDirectConnectGatewayAssociationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.direct_connect_gateway_association


class CreateDirectConnectGatewayAssociationResult(TypedDict):
    direct_connect_gateway_association: NotRequired[
        "aws_sdk_direct_connect.types.direct_connect_gateway_association.DirectConnectGatewayAssociation"
    ]
    """<p>The association to be created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDirectConnectGatewayAssociationResult) -> dict:
    out: dict = {}
    if "direct_connect_gateway_association" in value:
        import aws_sdk_direct_connect.types.direct_connect_gateway_association

        out["directConnectGatewayAssociation"] = (
            aws_sdk_direct_connect.types.direct_connect_gateway_association.serialize_aws_json_1_1(
                value["direct_connect_gateway_association"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDirectConnectGatewayAssociationResult:
    out: CreateDirectConnectGatewayAssociationResult = {}  # type: ignore[typeddict-item]
    if "directConnectGatewayAssociation" in data:
        import aws_sdk_direct_connect.types.direct_connect_gateway_association

        out["direct_connect_gateway_association"] = (
            aws_sdk_direct_connect.types.direct_connect_gateway_association.deserialize_aws_json_1_1(
                data["directConnectGatewayAssociation"]
            )
        )
    return out
