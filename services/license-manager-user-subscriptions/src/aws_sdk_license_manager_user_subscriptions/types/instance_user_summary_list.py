"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#InstanceUserSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.instance_user_summary

InstanceUserSummaryList: TypeAlias = list[
    "aws_sdk_license_manager_user_subscriptions.types.instance_user_summary.InstanceUserSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceUserSummaryList) -> list:
    import aws_sdk_license_manager_user_subscriptions.types.instance_user_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager_user_subscriptions.types.instance_user_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InstanceUserSummaryList:
    import aws_sdk_license_manager_user_subscriptions.types.instance_user_summary

    out: InstanceUserSummaryList = []
    for item in data:
        out.append(
            aws_sdk_license_manager_user_subscriptions.types.instance_user_summary.deserialize_json(
                item
            )
        )
    return out
