"""Generated from Smithy shape ``com.amazonaws.athena#UnprocessedNamedQueryIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.unprocessed_named_query_id

UnprocessedNamedQueryIdList: TypeAlias = list[
    "aws_sdk_athena.types.unprocessed_named_query_id.UnprocessedNamedQueryId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnprocessedNamedQueryIdList) -> list:
    import aws_sdk_athena.types.unprocessed_named_query_id

    out: list = []
    for item in value:
        out.append(
            aws_sdk_athena.types.unprocessed_named_query_id.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UnprocessedNamedQueryIdList:
    import aws_sdk_athena.types.unprocessed_named_query_id

    out: UnprocessedNamedQueryIdList = []
    for item in data:
        out.append(
            aws_sdk_athena.types.unprocessed_named_query_id.deserialize_aws_json_1_1(
                item
            )
        )
    return out
