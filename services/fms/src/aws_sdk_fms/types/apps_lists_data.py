"""Generated from Smithy shape ``com.amazonaws.fms#AppsListsData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.apps_list_data_summary

AppsListsData: TypeAlias = list[
    "aws_sdk_fms.types.apps_list_data_summary.AppsListDataSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppsListsData) -> list:
    import aws_sdk_fms.types.apps_list_data_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fms.types.apps_list_data_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AppsListsData:
    import aws_sdk_fms.types.apps_list_data_summary

    out: AppsListsData = []
    for item in data:
        out.append(
            aws_sdk_fms.types.apps_list_data_summary.deserialize_aws_json_1_1(item)
        )
    return out
