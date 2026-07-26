"""Generated from Smithy shape ``com.amazonaws.athena#BatchGetNamedQueryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.named_query_list
    import capo_athena.types.unprocessed_named_query_id_list


class BatchGetNamedQueryOutput(TypedDict, closed=True):
    named_queries: NotRequired["capo_athena.types.named_query_list.NamedQueryList"]
    """<p>Information about the named query IDs submitted.</p>"""
    unprocessed_named_query_ids: NotRequired[
        "capo_athena.types.unprocessed_named_query_id_list.UnprocessedNamedQueryIdList"
    ]
    """<p>Information about provided query IDs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetNamedQueryOutput) -> dict:
    out: dict = {}
    if "named_queries" in value:
        import capo_athena.types.named_query_list

        out["NamedQueries"] = capo_athena.types.named_query_list.serialize_aws_json_1_1(
            value["named_queries"]
        )
    if "unprocessed_named_query_ids" in value:
        import capo_athena.types.unprocessed_named_query_id_list

        out["UnprocessedNamedQueryIds"] = (
            capo_athena.types.unprocessed_named_query_id_list.serialize_aws_json_1_1(
                value["unprocessed_named_query_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetNamedQueryOutput:
    out: BatchGetNamedQueryOutput = {}  # type: ignore[typeddict-item]
    if "NamedQueries" in data:
        import capo_athena.types.named_query_list

        out["named_queries"] = (
            capo_athena.types.named_query_list.deserialize_aws_json_1_1(
                data["NamedQueries"]
            )
        )
    if "UnprocessedNamedQueryIds" in data:
        import capo_athena.types.unprocessed_named_query_id_list

        out["unprocessed_named_query_ids"] = (
            capo_athena.types.unprocessed_named_query_id_list.deserialize_aws_json_1_1(
                data["UnprocessedNamedQueryIds"]
            )
        )
    return out
