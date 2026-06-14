"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeTapeRecoveryPointsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.marker
    import aws_sdk_storage_gateway.types.positive_int_object


class DescribeTapeRecoveryPointsInput(TypedDict):
    gateway_arn: "aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"
    marker: NotRequired["aws_sdk_storage_gateway.types.marker.Marker"]
    """<p>An opaque string that indicates the position at which to begin describing the virtual tape recovery points.</p>"""
    limit: NotRequired[
        "aws_sdk_storage_gateway.types.positive_int_object.PositiveIntObject"
    ]
    """<p>Specifies that the number of virtual tape recovery points that are described be limited to the specified number.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTapeRecoveryPointsInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTapeRecoveryPointsInput:
    out: DescribeTapeRecoveryPointsInput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError(
            "DescribeTapeRecoveryPointsInput.gateway_arn required"
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "Limit" in data:
        out["limit"] = data["Limit"]
    return out
