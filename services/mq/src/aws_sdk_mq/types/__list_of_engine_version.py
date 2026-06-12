"""Generated from Smithy shape ``com.amazonaws.mq#__listOfEngineVersion``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mq.types.engine_version

__listOfEngineVersion: TypeAlias = list["aws_sdk_mq.types.engine_version.EngineVersion"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfEngineVersion) -> list:
    import aws_sdk_mq.types.engine_version

    out: list = []
    for item in value:
        out.append(aws_sdk_mq.types.engine_version.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfEngineVersion:
    import aws_sdk_mq.types.engine_version

    out: __listOfEngineVersion = []
    for item in data:
        out.append(aws_sdk_mq.types.engine_version.deserialize_json(item))
    return out
