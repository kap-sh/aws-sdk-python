"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#InstanceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.instance_summary

InstanceSummaryList: TypeAlias = list[
    "aws_sdk_license_manager_user_subscriptions.types.instance_summary.InstanceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceSummaryList) -> list:
    import aws_sdk_license_manager_user_subscriptions.types.instance_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager_user_subscriptions.types.instance_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InstanceSummaryList:
    import aws_sdk_license_manager_user_subscriptions.types.instance_summary

    out: InstanceSummaryList = []
    for item in data:
        out.append(
            aws_sdk_license_manager_user_subscriptions.types.instance_summary.deserialize_json(
                item
            )
        )
    return out
