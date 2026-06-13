"""Generated from Smithy shape ``com.amazonaws.quicksight#AdditionalDashboardIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.short_restrictive_resource_id

AdditionalDashboardIdList: TypeAlias = list[
    "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalDashboardIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AdditionalDashboardIdList:
    return list(data)
