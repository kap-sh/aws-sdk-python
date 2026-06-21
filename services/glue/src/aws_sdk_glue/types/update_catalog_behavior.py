"""Generated from Smithy shape ``com.amazonaws.glue#UpdateCatalogBehavior``."""

from typing import Literal, TypeAlias, cast

UpdateCatalogBehavior: TypeAlias = Literal[
    "UPDATE_IN_DATABASE",
    "LOG",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCatalogBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpdateCatalogBehavior:
    return cast(UpdateCatalogBehavior, data)
