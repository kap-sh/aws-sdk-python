"""Generated from Smithy shape ``com.amazonaws.athena#UnprocessedNamedQueryIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.unprocessed_named_query_id

UnprocessedNamedQueryIdList: TypeAlias = list[
    "capo_athena.types.unprocessed_named_query_id.UnprocessedNamedQueryId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnprocessedNamedQueryIdList) -> list:
    import capo_athena.types.unprocessed_named_query_id

    out: list = []
    for item in value:
        out.append(
            capo_athena.types.unprocessed_named_query_id.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UnprocessedNamedQueryIdList:
    import capo_athena.types.unprocessed_named_query_id

    out: UnprocessedNamedQueryIdList = []
    for item in data:
        out.append(
            capo_athena.types.unprocessed_named_query_id.deserialize_aws_json_1_1(item)
        )
    return out
