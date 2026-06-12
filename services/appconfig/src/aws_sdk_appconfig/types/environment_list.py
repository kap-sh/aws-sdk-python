"""Generated from Smithy shape ``com.amazonaws.appconfig#EnvironmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.environment

EnvironmentList: TypeAlias = list["aws_sdk_appconfig.types.environment.Environment"]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentList) -> list:
    import aws_sdk_appconfig.types.environment

    out: list = []
    for item in value:
        out.append(aws_sdk_appconfig.types.environment.serialize_json(item))
    return out


def deserialize_json(data: list) -> EnvironmentList:
    import aws_sdk_appconfig.types.environment

    out: EnvironmentList = []
    for item in data:
        out.append(aws_sdk_appconfig.types.environment.deserialize_json(item))
    return out
