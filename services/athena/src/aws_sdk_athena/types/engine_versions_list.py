"""Generated from Smithy shape ``com.amazonaws.athena#EngineVersionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.engine_version

EngineVersionsList: TypeAlias = list[
    "aws_sdk_athena.types.engine_version.EngineVersion"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EngineVersionsList) -> list:
    import aws_sdk_athena.types.engine_version

    out: list = []
    for item in value:
        out.append(aws_sdk_athena.types.engine_version.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EngineVersionsList:
    import aws_sdk_athena.types.engine_version

    out: EngineVersionsList = []
    for item in data:
        out.append(aws_sdk_athena.types.engine_version.deserialize_aws_json_1_1(item))
    return out
