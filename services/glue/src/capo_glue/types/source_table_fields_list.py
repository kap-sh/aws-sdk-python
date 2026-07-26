"""Generated from Smithy shape ``com.amazonaws.glue#SourceTableFieldsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.string128

SourceTableFieldsList: TypeAlias = list["capo_glue.types.string128.String128"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceTableFieldsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SourceTableFieldsList:
    return list(data)
