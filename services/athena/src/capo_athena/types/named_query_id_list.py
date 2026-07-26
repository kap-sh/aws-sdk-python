"""Generated from Smithy shape ``com.amazonaws.athena#NamedQueryIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.named_query_id

NamedQueryIdList: TypeAlias = list["capo_athena.types.named_query_id.NamedQueryId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamedQueryIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> NamedQueryIdList:
    return list(data)
