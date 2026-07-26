"""Generated from Smithy shape ``com.amazonaws.auditmanager#AWSServices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.aws_service

AWSServices: TypeAlias = list["capo_auditmanager.types.aws_service.AWSService"]


# --- restJson1 ser/de ---
def serialize_json(value: AWSServices) -> list:
    import capo_auditmanager.types.aws_service

    out: list = []
    for item in value:
        out.append(capo_auditmanager.types.aws_service.serialize_json(item))
    return out


def deserialize_json(data: list) -> AWSServices:
    import capo_auditmanager.types.aws_service

    out: AWSServices = []
    for item in data:
        out.append(capo_auditmanager.types.aws_service.deserialize_json(item))
    return out
