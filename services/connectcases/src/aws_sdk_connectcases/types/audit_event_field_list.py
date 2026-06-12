"""Generated from Smithy shape ``com.amazonaws.connectcases#AuditEventFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.audit_event_field

AuditEventFieldList: TypeAlias = list[
    "aws_sdk_connectcases.types.audit_event_field.AuditEventField | None"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuditEventFieldList) -> list:
    import aws_sdk_connectcases.types.audit_event_field

    out: list = []
    for item in value:
        if item is None:
            out.append(None)
            continue
        out.append(aws_sdk_connectcases.types.audit_event_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> AuditEventFieldList:
    import aws_sdk_connectcases.types.audit_event_field

    out: AuditEventFieldList = []
    for item in data:
        if item is None:
            out.append(None)
            continue
        out.append(aws_sdk_connectcases.types.audit_event_field.deserialize_json(item))
    return out
