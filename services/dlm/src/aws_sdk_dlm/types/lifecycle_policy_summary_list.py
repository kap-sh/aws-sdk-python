"""Generated from Smithy shape ``com.amazonaws.dlm#LifecyclePolicySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dlm.types.lifecycle_policy_summary

LifecyclePolicySummaryList: TypeAlias = list[
    "aws_sdk_dlm.types.lifecycle_policy_summary.LifecyclePolicySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicySummaryList) -> list:
    import aws_sdk_dlm.types.lifecycle_policy_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_dlm.types.lifecycle_policy_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> LifecyclePolicySummaryList:
    import aws_sdk_dlm.types.lifecycle_policy_summary

    out: LifecyclePolicySummaryList = []
    for item in data:
        out.append(aws_sdk_dlm.types.lifecycle_policy_summary.deserialize_json(item))
    return out
