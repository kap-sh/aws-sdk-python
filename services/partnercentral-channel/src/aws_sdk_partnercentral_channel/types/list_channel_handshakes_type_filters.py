"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ListChannelHandshakesTypeFilters``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_partnercentral_channel.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.program_management_account_type_filters
    import aws_sdk_partnercentral_channel.types.revoke_service_period_type_filters
    import aws_sdk_partnercentral_channel.types.start_service_period_type_filters


class _ListChannelHandshakesTypeFilters_startServicePeriodTypeFilters(TypedDict):
    startServicePeriodTypeFilters: "aws_sdk_partnercentral_channel.types.start_service_period_type_filters.StartServicePeriodTypeFilters"


class _ListChannelHandshakesTypeFilters_revokeServicePeriodTypeFilters(TypedDict):
    revokeServicePeriodTypeFilters: "aws_sdk_partnercentral_channel.types.revoke_service_period_type_filters.RevokeServicePeriodTypeFilters"


class _ListChannelHandshakesTypeFilters_programManagementAccountTypeFilters(TypedDict):
    programManagementAccountTypeFilters: "aws_sdk_partnercentral_channel.types.program_management_account_type_filters.ProgramManagementAccountTypeFilters"


ListChannelHandshakesTypeFilters: TypeAlias = (
    _ListChannelHandshakesTypeFilters_startServicePeriodTypeFilters
    | _ListChannelHandshakesTypeFilters_revokeServicePeriodTypeFilters
    | _ListChannelHandshakesTypeFilters_programManagementAccountTypeFilters
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListChannelHandshakesTypeFilters) -> dict:
    if "startServicePeriodTypeFilters" in value:
        import aws_sdk_partnercentral_channel.types.start_service_period_type_filters

        return {
            "startServicePeriodTypeFilters": aws_sdk_partnercentral_channel.types.start_service_period_type_filters.serialize_aws_json_1_0(
                value["startServicePeriodTypeFilters"]
            )
        }
    elif "revokeServicePeriodTypeFilters" in value:
        import aws_sdk_partnercentral_channel.types.revoke_service_period_type_filters

        return {
            "revokeServicePeriodTypeFilters": aws_sdk_partnercentral_channel.types.revoke_service_period_type_filters.serialize_aws_json_1_0(
                value["revokeServicePeriodTypeFilters"]
            )
        }
    elif "programManagementAccountTypeFilters" in value:
        import aws_sdk_partnercentral_channel.types.program_management_account_type_filters

        return {
            "programManagementAccountTypeFilters": aws_sdk_partnercentral_channel.types.program_management_account_type_filters.serialize_aws_json_1_0(
                value["programManagementAccountTypeFilters"]
            )
        }
    else:
        raise SerializationError("ListChannelHandshakesTypeFilters: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ListChannelHandshakesTypeFilters:
    if "startServicePeriodTypeFilters" in data:
        import aws_sdk_partnercentral_channel.types.start_service_period_type_filters

        return {
            "startServicePeriodTypeFilters": aws_sdk_partnercentral_channel.types.start_service_period_type_filters.deserialize_aws_json_1_0(
                data["startServicePeriodTypeFilters"]
            )
        }
    elif "revokeServicePeriodTypeFilters" in data:
        import aws_sdk_partnercentral_channel.types.revoke_service_period_type_filters

        return {
            "revokeServicePeriodTypeFilters": aws_sdk_partnercentral_channel.types.revoke_service_period_type_filters.deserialize_aws_json_1_0(
                data["revokeServicePeriodTypeFilters"]
            )
        }
    elif "programManagementAccountTypeFilters" in data:
        import aws_sdk_partnercentral_channel.types.program_management_account_type_filters

        return {
            "programManagementAccountTypeFilters": aws_sdk_partnercentral_channel.types.program_management_account_type_filters.deserialize_aws_json_1_0(
                data["programManagementAccountTypeFilters"]
            )
        }
    else:
        raise DeserializationError(
            "ListChannelHandshakesTypeFilters: no recognized variant key"
        )
