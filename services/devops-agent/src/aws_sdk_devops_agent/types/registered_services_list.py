"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredServicesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.registered_service

RegisteredServicesList: TypeAlias = list[
    "aws_sdk_devops_agent.types.registered_service.RegisteredService"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredServicesList) -> list:
    import aws_sdk_devops_agent.types.registered_service

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_agent.types.registered_service.serialize_json(item))
    return out


def deserialize_json(data: list) -> RegisteredServicesList:
    import aws_sdk_devops_agent.types.registered_service

    out: RegisteredServicesList = []
    for item in data:
        out.append(aws_sdk_devops_agent.types.registered_service.deserialize_json(item))
    return out
