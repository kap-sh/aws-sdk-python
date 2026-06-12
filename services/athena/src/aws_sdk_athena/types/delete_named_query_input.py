"""Generated from Smithy shape ``com.amazonaws.athena#DeleteNamedQueryInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.named_query_id


class DeleteNamedQueryInput(TypedDict):
    named_query_id: "aws_sdk_athena.types.named_query_id.NamedQueryId"
    """<p>The unique ID of the query to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteNamedQueryInput) -> dict:
    out: dict = {}
    out["NamedQueryId"] = value["named_query_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteNamedQueryInput:
    out: DeleteNamedQueryInput = {}  # type: ignore[typeddict-item]
    if "NamedQueryId" in data:
        out["named_query_id"] = data["NamedQueryId"]
    else:
        raise DeserializationError("DeleteNamedQueryInput.named_query_id required")
    return out
