"""Generated from Smithy shape ``com.amazonaws.fms#EntryViolationReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.entry_violation_reason

EntryViolationReasons: TypeAlias = list[
    "capo_fms.types.entry_violation_reason.EntryViolationReason"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntryViolationReasons) -> list:
    import capo_fms.types.entry_violation_reason

    out: list = []
    for item in value:
        out.append(capo_fms.types.entry_violation_reason.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EntryViolationReasons:
    import capo_fms.types.entry_violation_reason

    out: EntryViolationReasons = []
    for item in data:
        out.append(capo_fms.types.entry_violation_reason.deserialize_aws_json_1_1(item))
    return out
