"""Generated from Smithy shape ``com.amazonaws.ssmincidents#Integrations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.integration

Integrations: TypeAlias = list["aws_sdk_ssm_incidents.types.integration.Integration"]


# --- restJson1 ser/de ---
def serialize_json(value: Integrations) -> list:
    import aws_sdk_ssm_incidents.types.integration

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_incidents.types.integration.serialize_json(item))
    return out


def deserialize_json(data: list) -> Integrations:
    import aws_sdk_ssm_incidents.types.integration

    out: Integrations = []
    for item in data:
        out.append(aws_sdk_ssm_incidents.types.integration.deserialize_json(item))
    return out
