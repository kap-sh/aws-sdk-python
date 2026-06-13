"""Generated from Smithy shape ``com.amazonaws.inspector2#TargetStatusReasonFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_target_status_reason_filter

TargetStatusReasonFilterList: TypeAlias = list[
    "aws_sdk_inspector2.types.cis_target_status_reason_filter.CisTargetStatusReasonFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetStatusReasonFilterList) -> list:
    import aws_sdk_inspector2.types.cis_target_status_reason_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector2.types.cis_target_status_reason_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TargetStatusReasonFilterList:
    import aws_sdk_inspector2.types.cis_target_status_reason_filter

    out: TargetStatusReasonFilterList = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.cis_target_status_reason_filter.deserialize_json(
                item
            )
        )
    return out
