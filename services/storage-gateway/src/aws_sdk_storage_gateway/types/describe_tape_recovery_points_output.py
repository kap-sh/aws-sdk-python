"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeTapeRecoveryPointsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.marker
    import aws_sdk_storage_gateway.types.tape_recovery_point_infos


class DescribeTapeRecoveryPointsOutput(TypedDict):
    gateway_arn: NotRequired["aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"]
    tape_recovery_point_infos: NotRequired[
        "aws_sdk_storage_gateway.types.tape_recovery_point_infos.TapeRecoveryPointInfos"
    ]
    """<p>An array of TapeRecoveryPointInfos that are available for the specified gateway.</p>"""
    marker: NotRequired["aws_sdk_storage_gateway.types.marker.Marker"]
    """<p>An opaque string that indicates the position at which the virtual tape recovery points that were listed for description ended.</p> <p>Use this marker in your next request to list the next set of virtual tape recovery points in the list. If there are no more recovery points to describe, this field does not appear in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTapeRecoveryPointsOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "tape_recovery_point_infos" in value:
        import aws_sdk_storage_gateway.types.tape_recovery_point_infos

        out["TapeRecoveryPointInfos"] = (
            aws_sdk_storage_gateway.types.tape_recovery_point_infos.serialize_aws_json_1_1(
                value["tape_recovery_point_infos"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTapeRecoveryPointsOutput:
    out: DescribeTapeRecoveryPointsOutput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    if "TapeRecoveryPointInfos" in data:
        import aws_sdk_storage_gateway.types.tape_recovery_point_infos

        out["tape_recovery_point_infos"] = (
            aws_sdk_storage_gateway.types.tape_recovery_point_infos.deserialize_aws_json_1_1(
                data["TapeRecoveryPointInfos"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
