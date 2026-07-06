"""Generated from Smithy shape ``com.amazonaws.athena#BatchGetNamedQueryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.named_query_id_list


class BatchGetNamedQueryInput(TypedDict, closed=True):
    named_query_ids: "aws_sdk_athena.types.named_query_id_list.NamedQueryIdList"
    """<p>An array of query IDs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetNamedQueryInput) -> dict:
    out: dict = {}
    import aws_sdk_athena.types.named_query_id_list

    out["NamedQueryIds"] = (
        aws_sdk_athena.types.named_query_id_list.serialize_aws_json_1_1(
            value["named_query_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetNamedQueryInput:
    out: BatchGetNamedQueryInput = {}  # type: ignore[typeddict-item]
    if "NamedQueryIds" in data:
        import aws_sdk_athena.types.named_query_id_list

        out["named_query_ids"] = (
            aws_sdk_athena.types.named_query_id_list.deserialize_aws_json_1_1(
                data["NamedQueryIds"]
            )
        )
    else:
        raise DeserializationError("BatchGetNamedQueryInput.named_query_ids required")
    return out
