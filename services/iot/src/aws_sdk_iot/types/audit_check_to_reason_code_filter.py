"""Generated from Smithy shape ``com.amazonaws.iot#AuditCheckToReasonCodeFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_check_name
    import aws_sdk_iot.types.reason_for_non_compliance_codes

AuditCheckToReasonCodeFilter: TypeAlias = dict[
    "aws_sdk_iot.types.audit_check_name.AuditCheckName",
    "aws_sdk_iot.types.reason_for_non_compliance_codes.ReasonForNonComplianceCodes",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AuditCheckToReasonCodeFilter) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_iot.types.reason_for_non_compliance_codes

        out[key] = aws_sdk_iot.types.reason_for_non_compliance_codes.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> AuditCheckToReasonCodeFilter:
    out: AuditCheckToReasonCodeFilter = {}
    for key, value in data.items():
        import aws_sdk_iot.types.reason_for_non_compliance_codes

        out[key] = aws_sdk_iot.types.reason_for_non_compliance_codes.deserialize_json(
            value
        )
    return out
