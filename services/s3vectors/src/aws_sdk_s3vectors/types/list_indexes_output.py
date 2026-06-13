"""Generated from Smithy shape ``com.amazonaws.s3vectors#ListIndexesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.list_indexes_next_token
    import aws_sdk_s3vectors.types.list_indexes_output_list


class ListIndexesOutput(TypedDict):
    next_token: NotRequired[
        "aws_sdk_s3vectors.types.list_indexes_next_token.ListIndexesNextToken"
    ]
    """<p>The next pagination token.</p>"""
    indexes: "aws_sdk_s3vectors.types.list_indexes_output_list.ListIndexesOutputList"
    """<p>The attributes of the vector indexes</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIndexesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_s3vectors.types.list_indexes_output_list

    out["indexes"] = aws_sdk_s3vectors.types.list_indexes_output_list.serialize_json(
        value["indexes"]
    )
    return out


def deserialize_json(data: dict) -> ListIndexesOutput:
    out: ListIndexesOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "indexes" in data:
        import aws_sdk_s3vectors.types.list_indexes_output_list

        out["indexes"] = (
            aws_sdk_s3vectors.types.list_indexes_output_list.deserialize_json(
                data["indexes"]
            )
        )
    else:
        raise DeserializationError("ListIndexesOutput.indexes required")
    return out
