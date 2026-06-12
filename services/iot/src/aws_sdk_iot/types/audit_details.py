"""Generated from Smithy shape ``com.amazonaws.iot#AuditDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_check_details
    import aws_sdk_iot.types.audit_check_name

AuditDetails: TypeAlias = dict[
    "aws_sdk_iot.types.audit_check_name.AuditCheckName",
    "aws_sdk_iot.types.audit_check_details.AuditCheckDetails",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AuditDetails) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_iot.types.audit_check_details

        out[key] = aws_sdk_iot.types.audit_check_details.serialize_json(value)
    return out


def deserialize_json(data: dict) -> AuditDetails:
    out: AuditDetails = {}
    for key, value in data.items():
        import aws_sdk_iot.types.audit_check_details

        out[key] = aws_sdk_iot.types.audit_check_details.deserialize_json(value)
    return out
