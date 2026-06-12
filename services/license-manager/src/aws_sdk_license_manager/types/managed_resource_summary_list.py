"""Generated from Smithy shape ``com.amazonaws.licensemanager#ManagedResourceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.managed_resource_summary

ManagedResourceSummaryList: TypeAlias = list[
    "aws_sdk_license_manager.types.managed_resource_summary.ManagedResourceSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedResourceSummaryList) -> list:
    import aws_sdk_license_manager.types.managed_resource_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager.types.managed_resource_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ManagedResourceSummaryList:
    import aws_sdk_license_manager.types.managed_resource_summary

    out: ManagedResourceSummaryList = []
    for item in data:
        out.append(
            aws_sdk_license_manager.types.managed_resource_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
