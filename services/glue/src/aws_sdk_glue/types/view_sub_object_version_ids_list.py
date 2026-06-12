"""Generated from Smithy shape ``com.amazonaws.glue#ViewSubObjectVersionIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.table_version_id

ViewSubObjectVersionIdsList: TypeAlias = list[
    "aws_sdk_glue.types.table_version_id.TableVersionId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ViewSubObjectVersionIdsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ViewSubObjectVersionIdsList:
    return list(data)
