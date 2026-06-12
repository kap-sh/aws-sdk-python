"""Generated from Smithy shape ``com.amazonaws.auditmanager#Resources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.resource

Resources: TypeAlias = list["aws_sdk_auditmanager.types.resource.Resource"]


# --- restJson1 ser/de ---
def serialize_json(value: Resources) -> list:
    import aws_sdk_auditmanager.types.resource

    out: list = []
    for item in value:
        out.append(aws_sdk_auditmanager.types.resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> Resources:
    import aws_sdk_auditmanager.types.resource

    out: Resources = []
    for item in data:
        out.append(aws_sdk_auditmanager.types.resource.deserialize_json(item))
    return out
