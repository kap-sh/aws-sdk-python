"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ProgramManagementAccountTypeSort``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_channel.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.program_management_account_type_sort_name
    import aws_sdk_partnercentral_channel.types.sort_order


class ProgramManagementAccountTypeSort(TypedDict, closed=True):
    sort_order: "aws_sdk_partnercentral_channel.types.sort_order.SortOrder"
    """<p>The sort order (ascending or descending).</p>"""
    sort_by: "aws_sdk_partnercentral_channel.types.program_management_account_type_sort_name.ProgramManagementAccountTypeSortName"
    """<p>The field to sort by.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProgramManagementAccountTypeSort) -> dict:
    out: dict = {}
    import aws_sdk_partnercentral_channel.types.sort_order

    out["sortOrder"] = (
        aws_sdk_partnercentral_channel.types.sort_order.serialize_aws_json_1_0(
            value["sort_order"]
        )
    )
    import aws_sdk_partnercentral_channel.types.program_management_account_type_sort_name

    out["sortBy"] = (
        aws_sdk_partnercentral_channel.types.program_management_account_type_sort_name.serialize_aws_json_1_0(
            value["sort_by"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProgramManagementAccountTypeSort:
    out: ProgramManagementAccountTypeSort = {}  # type: ignore[typeddict-item]
    if "sortOrder" in data:
        import aws_sdk_partnercentral_channel.types.sort_order

        out["sort_order"] = (
            aws_sdk_partnercentral_channel.types.sort_order.deserialize_aws_json_1_0(
                data["sortOrder"]
            )
        )
    else:
        raise DeserializationError(
            "ProgramManagementAccountTypeSort.sort_order required"
        )
    if "sortBy" in data:
        import aws_sdk_partnercentral_channel.types.program_management_account_type_sort_name

        out["sort_by"] = (
            aws_sdk_partnercentral_channel.types.program_management_account_type_sort_name.deserialize_aws_json_1_0(
                data["sortBy"]
            )
        )
    else:
        raise DeserializationError("ProgramManagementAccountTypeSort.sort_by required")
    return out
