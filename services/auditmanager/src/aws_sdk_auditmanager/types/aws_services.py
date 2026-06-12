"""Generated from Smithy shape ``com.amazonaws.auditmanager#AWSServices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.aws_service

AWSServices: TypeAlias = list["aws_sdk_auditmanager.types.aws_service.AWSService"]


# --- restJson1 ser/de ---
def serialize_json(value: AWSServices) -> list:
    import aws_sdk_auditmanager.types.aws_service

    out: list = []
    for item in value:
        out.append(aws_sdk_auditmanager.types.aws_service.serialize_json(item))
    return out


def deserialize_json(data: list) -> AWSServices:
    import aws_sdk_auditmanager.types.aws_service

    out: AWSServices = []
    for item in data:
        out.append(aws_sdk_auditmanager.types.aws_service.deserialize_json(item))
    return out
