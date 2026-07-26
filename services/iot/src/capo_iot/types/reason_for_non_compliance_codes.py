"""Generated from Smithy shape ``com.amazonaws.iot#ReasonForNonComplianceCodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.reason_for_non_compliance_code

ReasonForNonComplianceCodes: TypeAlias = list[
    "capo_iot.types.reason_for_non_compliance_code.ReasonForNonComplianceCode"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReasonForNonComplianceCodes) -> list:
    return list(value)


def deserialize_json(data: list) -> ReasonForNonComplianceCodes:
    return list(data)
