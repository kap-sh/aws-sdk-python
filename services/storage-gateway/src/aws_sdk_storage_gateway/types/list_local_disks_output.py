"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListLocalDisksOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.disks
    import aws_sdk_storage_gateway.types.gateway_arn


class ListLocalDisksOutput(TypedDict):
    gateway_arn: NotRequired["aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"]
    disks: NotRequired["aws_sdk_storage_gateway.types.disks.Disks"]
    """<p>A JSON object containing the following fields:</p> <ul> <li> <p> <a>ListLocalDisksOutput$Disks</a> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLocalDisksOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "disks" in value:
        import aws_sdk_storage_gateway.types.disks

        out["Disks"] = aws_sdk_storage_gateway.types.disks.serialize_aws_json_1_1(
            value["disks"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLocalDisksOutput:
    out: ListLocalDisksOutput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    if "Disks" in data:
        import aws_sdk_storage_gateway.types.disks

        out["disks"] = aws_sdk_storage_gateway.types.disks.deserialize_aws_json_1_1(
            data["Disks"]
        )
    return out
