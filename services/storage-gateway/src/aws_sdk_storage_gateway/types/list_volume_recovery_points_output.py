"""Generated from Smithy shape ``com.amazonaws.storagegateway#ListVolumeRecoveryPointsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.volume_recovery_point_infos


class ListVolumeRecoveryPointsOutput(TypedDict):
    gateway_arn: NotRequired["aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"]
    volume_recovery_point_infos: NotRequired[
        "aws_sdk_storage_gateway.types.volume_recovery_point_infos.VolumeRecoveryPointInfos"
    ]
    """<p>An array of <a>VolumeRecoveryPointInfo</a> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListVolumeRecoveryPointsOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "volume_recovery_point_infos" in value:
        import aws_sdk_storage_gateway.types.volume_recovery_point_infos

        out["VolumeRecoveryPointInfos"] = (
            aws_sdk_storage_gateway.types.volume_recovery_point_infos.serialize_aws_json_1_1(
                value["volume_recovery_point_infos"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListVolumeRecoveryPointsOutput:
    out: ListVolumeRecoveryPointsOutput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    if "VolumeRecoveryPointInfos" in data:
        import aws_sdk_storage_gateway.types.volume_recovery_point_infos

        out["volume_recovery_point_infos"] = (
            aws_sdk_storage_gateway.types.volume_recovery_point_infos.deserialize_aws_json_1_1(
                data["VolumeRecoveryPointInfos"]
            )
        )
    return out
