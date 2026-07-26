"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#EndpointSettingTypeValue``."""

from typing import Literal, TypeAlias, cast

EndpointSettingTypeValue: TypeAlias = Literal[
    "string",
    "boolean",
    "integer",
    "enum",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointSettingTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EndpointSettingTypeValue:
    return cast(EndpointSettingTypeValue, data)
