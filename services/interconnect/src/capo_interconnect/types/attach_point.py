"""Generated from Smithy shape ``com.amazonaws.interconnect#AttachPoint``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_interconnect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_interconnect.types.amazon_resource_name
    import capo_interconnect.types.direct_connect_gateway_attach_point


class _AttachPoint_directConnectGateway(TypedDict, closed=True):
    directConnectGateway: "capo_interconnect.types.direct_connect_gateway_attach_point.DirectConnectGatewayAttachPoint"


class _AttachPoint_arn(TypedDict, closed=True):
    arn: "capo_interconnect.types.amazon_resource_name.AmazonResourceName"


AttachPoint: TypeAlias = _AttachPoint_directConnectGateway | _AttachPoint_arn


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttachPoint) -> dict:
    if "directConnectGateway" in value:
        return {"directConnectGateway": value["directConnectGateway"]}
    elif "arn" in value:
        return {"arn": value["arn"]}
    else:
        raise SerializationError("AttachPoint: no variant present")


def deserialize_aws_json_1_0(data: dict) -> AttachPoint:
    if "directConnectGateway" in data:
        return {"directConnectGateway": data["directConnectGateway"]}
    elif "arn" in data:
        return {"arn": data["arn"]}
    else:
        raise DeserializationError("AttachPoint: no recognized variant key")
