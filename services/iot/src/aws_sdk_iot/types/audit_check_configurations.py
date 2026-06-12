"""Generated from Smithy shape ``com.amazonaws.iot#AuditCheckConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_check_configuration
    import aws_sdk_iot.types.audit_check_name

AuditCheckConfigurations: TypeAlias = dict[
    "aws_sdk_iot.types.audit_check_name.AuditCheckName",
    "aws_sdk_iot.types.audit_check_configuration.AuditCheckConfiguration",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AuditCheckConfigurations) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_iot.types.audit_check_configuration

        out[key] = aws_sdk_iot.types.audit_check_configuration.serialize_json(value)
    return out


def deserialize_json(data: dict) -> AuditCheckConfigurations:
    out: AuditCheckConfigurations = {}
    for key, value in data.items():
        import aws_sdk_iot.types.audit_check_configuration

        out[key] = aws_sdk_iot.types.audit_check_configuration.deserialize_json(value)
    return out
