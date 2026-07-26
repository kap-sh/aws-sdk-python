"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#PluginNameValue``."""

from typing import Literal, TypeAlias, cast

PluginNameValue: TypeAlias = Literal[
    "no-preference",
    "test-decoding",
    "pglogical",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PluginNameValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PluginNameValue:
    return cast(PluginNameValue, data)
