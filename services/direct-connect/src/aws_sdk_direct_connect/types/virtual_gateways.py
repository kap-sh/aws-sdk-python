"""Generated from Smithy shape ``com.amazonaws.directconnect#VirtualGateways``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.virtual_gateway_list


class VirtualGateways(TypedDict, closed=True):
    virtual_gateways: NotRequired[
        "aws_sdk_direct_connect.types.virtual_gateway_list.VirtualGatewayList"
    ]
    """<p>The virtual private gateways.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VirtualGateways) -> dict:
    out: dict = {}
    if "virtual_gateways" in value:
        import aws_sdk_direct_connect.types.virtual_gateway_list

        out["virtualGateways"] = (
            aws_sdk_direct_connect.types.virtual_gateway_list.serialize_aws_json_1_1(
                value["virtual_gateways"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VirtualGateways:
    out: VirtualGateways = {}  # type: ignore[typeddict-item]
    if "virtualGateways" in data:
        import aws_sdk_direct_connect.types.virtual_gateway_list

        out["virtual_gateways"] = (
            aws_sdk_direct_connect.types.virtual_gateway_list.deserialize_aws_json_1_1(
                data["virtualGateways"]
            )
        )
    return out
