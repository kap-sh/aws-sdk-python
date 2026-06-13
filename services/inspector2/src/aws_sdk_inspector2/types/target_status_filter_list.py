"""Generated from Smithy shape ``com.amazonaws.inspector2#TargetStatusFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_target_status_filter

TargetStatusFilterList: TypeAlias = list[
    "aws_sdk_inspector2.types.cis_target_status_filter.CisTargetStatusFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetStatusFilterList) -> list:
    import aws_sdk_inspector2.types.cis_target_status_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector2.types.cis_target_status_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TargetStatusFilterList:
    import aws_sdk_inspector2.types.cis_target_status_filter

    out: TargetStatusFilterList = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.cis_target_status_filter.deserialize_json(item)
        )
    return out
