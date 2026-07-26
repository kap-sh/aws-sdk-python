"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ListChannelHandshakesTypeSort``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_partnercentral_channel.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.program_management_account_type_sort
    import capo_partnercentral_channel.types.revoke_service_period_type_sort
    import capo_partnercentral_channel.types.start_service_period_type_sort


class _ListChannelHandshakesTypeSort_startServicePeriodTypeSort(TypedDict, closed=True):
    startServicePeriodTypeSort: "capo_partnercentral_channel.types.start_service_period_type_sort.StartServicePeriodTypeSort"


class _ListChannelHandshakesTypeSort_revokeServicePeriodTypeSort(
    TypedDict, closed=True
):
    revokeServicePeriodTypeSort: "capo_partnercentral_channel.types.revoke_service_period_type_sort.RevokeServicePeriodTypeSort"


class _ListChannelHandshakesTypeSort_programManagementAccountTypeSort(
    TypedDict, closed=True
):
    programManagementAccountTypeSort: "capo_partnercentral_channel.types.program_management_account_type_sort.ProgramManagementAccountTypeSort"


ListChannelHandshakesTypeSort: TypeAlias = (
    _ListChannelHandshakesTypeSort_startServicePeriodTypeSort
    | _ListChannelHandshakesTypeSort_revokeServicePeriodTypeSort
    | _ListChannelHandshakesTypeSort_programManagementAccountTypeSort
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListChannelHandshakesTypeSort) -> dict:
    if "startServicePeriodTypeSort" in value:
        import capo_partnercentral_channel.types.start_service_period_type_sort

        return {
            "startServicePeriodTypeSort": capo_partnercentral_channel.types.start_service_period_type_sort.serialize_aws_json_1_0(
                value["startServicePeriodTypeSort"]
            )
        }
    elif "revokeServicePeriodTypeSort" in value:
        import capo_partnercentral_channel.types.revoke_service_period_type_sort

        return {
            "revokeServicePeriodTypeSort": capo_partnercentral_channel.types.revoke_service_period_type_sort.serialize_aws_json_1_0(
                value["revokeServicePeriodTypeSort"]
            )
        }
    elif "programManagementAccountTypeSort" in value:
        import capo_partnercentral_channel.types.program_management_account_type_sort

        return {
            "programManagementAccountTypeSort": capo_partnercentral_channel.types.program_management_account_type_sort.serialize_aws_json_1_0(
                value["programManagementAccountTypeSort"]
            )
        }
    else:
        raise SerializationError("ListChannelHandshakesTypeSort: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ListChannelHandshakesTypeSort:
    if "startServicePeriodTypeSort" in data:
        import capo_partnercentral_channel.types.start_service_period_type_sort

        return {
            "startServicePeriodTypeSort": capo_partnercentral_channel.types.start_service_period_type_sort.deserialize_aws_json_1_0(
                data["startServicePeriodTypeSort"]
            )
        }
    elif "revokeServicePeriodTypeSort" in data:
        import capo_partnercentral_channel.types.revoke_service_period_type_sort

        return {
            "revokeServicePeriodTypeSort": capo_partnercentral_channel.types.revoke_service_period_type_sort.deserialize_aws_json_1_0(
                data["revokeServicePeriodTypeSort"]
            )
        }
    elif "programManagementAccountTypeSort" in data:
        import capo_partnercentral_channel.types.program_management_account_type_sort

        return {
            "programManagementAccountTypeSort": capo_partnercentral_channel.types.program_management_account_type_sort.deserialize_aws_json_1_0(
                data["programManagementAccountTypeSort"]
            )
        }
    else:
        raise DeserializationError(
            "ListChannelHandshakesTypeSort: no recognized variant key"
        )
