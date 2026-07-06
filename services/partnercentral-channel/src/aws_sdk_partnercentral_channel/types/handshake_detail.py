"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#HandshakeDetail``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_partnercentral_channel.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.program_management_account_handshake_detail
    import aws_sdk_partnercentral_channel.types.revoke_service_period_handshake_detail
    import aws_sdk_partnercentral_channel.types.start_service_period_handshake_detail


class _HandshakeDetail_startServicePeriodHandshakeDetail(TypedDict, closed=True):
    startServicePeriodHandshakeDetail: "aws_sdk_partnercentral_channel.types.start_service_period_handshake_detail.StartServicePeriodHandshakeDetail"


class _HandshakeDetail_revokeServicePeriodHandshakeDetail(TypedDict, closed=True):
    revokeServicePeriodHandshakeDetail: "aws_sdk_partnercentral_channel.types.revoke_service_period_handshake_detail.RevokeServicePeriodHandshakeDetail"


class _HandshakeDetail_programManagementAccountHandshakeDetail(TypedDict, closed=True):
    programManagementAccountHandshakeDetail: "aws_sdk_partnercentral_channel.types.program_management_account_handshake_detail.ProgramManagementAccountHandshakeDetail"


HandshakeDetail: TypeAlias = (
    _HandshakeDetail_startServicePeriodHandshakeDetail
    | _HandshakeDetail_revokeServicePeriodHandshakeDetail
    | _HandshakeDetail_programManagementAccountHandshakeDetail
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HandshakeDetail) -> dict:
    if "startServicePeriodHandshakeDetail" in value:
        import aws_sdk_partnercentral_channel.types.start_service_period_handshake_detail

        return {
            "startServicePeriodHandshakeDetail": aws_sdk_partnercentral_channel.types.start_service_period_handshake_detail.serialize_aws_json_1_0(
                value["startServicePeriodHandshakeDetail"]
            )
        }
    elif "revokeServicePeriodHandshakeDetail" in value:
        import aws_sdk_partnercentral_channel.types.revoke_service_period_handshake_detail

        return {
            "revokeServicePeriodHandshakeDetail": aws_sdk_partnercentral_channel.types.revoke_service_period_handshake_detail.serialize_aws_json_1_0(
                value["revokeServicePeriodHandshakeDetail"]
            )
        }
    elif "programManagementAccountHandshakeDetail" in value:
        import aws_sdk_partnercentral_channel.types.program_management_account_handshake_detail

        return {
            "programManagementAccountHandshakeDetail": aws_sdk_partnercentral_channel.types.program_management_account_handshake_detail.serialize_aws_json_1_0(
                value["programManagementAccountHandshakeDetail"]
            )
        }
    else:
        raise SerializationError("HandshakeDetail: no variant present")


def deserialize_aws_json_1_0(data: dict) -> HandshakeDetail:
    if "startServicePeriodHandshakeDetail" in data:
        import aws_sdk_partnercentral_channel.types.start_service_period_handshake_detail

        return {
            "startServicePeriodHandshakeDetail": aws_sdk_partnercentral_channel.types.start_service_period_handshake_detail.deserialize_aws_json_1_0(
                data["startServicePeriodHandshakeDetail"]
            )
        }
    elif "revokeServicePeriodHandshakeDetail" in data:
        import aws_sdk_partnercentral_channel.types.revoke_service_period_handshake_detail

        return {
            "revokeServicePeriodHandshakeDetail": aws_sdk_partnercentral_channel.types.revoke_service_period_handshake_detail.deserialize_aws_json_1_0(
                data["revokeServicePeriodHandshakeDetail"]
            )
        }
    elif "programManagementAccountHandshakeDetail" in data:
        import aws_sdk_partnercentral_channel.types.program_management_account_handshake_detail

        return {
            "programManagementAccountHandshakeDetail": aws_sdk_partnercentral_channel.types.program_management_account_handshake_detail.deserialize_aws_json_1_0(
                data["programManagementAccountHandshakeDetail"]
            )
        }
    else:
        raise DeserializationError("HandshakeDetail: no recognized variant key")
