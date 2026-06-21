"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RefreshSchemasStatusTypeValue``."""

from typing import Literal, TypeAlias, cast

RefreshSchemasStatusTypeValue: TypeAlias = Literal[
    "successful",
    "failed",
    "refreshing",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RefreshSchemasStatusTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RefreshSchemasStatusTypeValue:
    return cast(RefreshSchemasStatusTypeValue, data)
