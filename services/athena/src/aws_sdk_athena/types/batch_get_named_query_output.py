"""Generated from Smithy shape ``com.amazonaws.athena#BatchGetNamedQueryOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.named_query_list
    import aws_sdk_athena.types.unprocessed_named_query_id_list


class BatchGetNamedQueryOutput(TypedDict):
    named_queries: NotRequired["aws_sdk_athena.types.named_query_list.NamedQueryList"]
    """<p>Information about the named query IDs submitted.</p>"""
    unprocessed_named_query_ids: NotRequired[
        "aws_sdk_athena.types.unprocessed_named_query_id_list.UnprocessedNamedQueryIdList"
    ]
    """<p>Information about provided query IDs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetNamedQueryOutput) -> dict:
    out: dict = {}
    if "named_queries" in value:
        import aws_sdk_athena.types.named_query_list

        out["NamedQueries"] = (
            aws_sdk_athena.types.named_query_list.serialize_aws_json_1_1(
                value["named_queries"]
            )
        )
    if "unprocessed_named_query_ids" in value:
        import aws_sdk_athena.types.unprocessed_named_query_id_list

        out["UnprocessedNamedQueryIds"] = (
            aws_sdk_athena.types.unprocessed_named_query_id_list.serialize_aws_json_1_1(
                value["unprocessed_named_query_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetNamedQueryOutput:
    out: BatchGetNamedQueryOutput = {}  # type: ignore[typeddict-item]
    if "NamedQueries" in data:
        import aws_sdk_athena.types.named_query_list

        out["named_queries"] = (
            aws_sdk_athena.types.named_query_list.deserialize_aws_json_1_1(
                data["NamedQueries"]
            )
        )
    if "UnprocessedNamedQueryIds" in data:
        import aws_sdk_athena.types.unprocessed_named_query_id_list

        out["unprocessed_named_query_ids"] = (
            aws_sdk_athena.types.unprocessed_named_query_id_list.deserialize_aws_json_1_1(
                data["UnprocessedNamedQueryIds"]
            )
        )
    return out
