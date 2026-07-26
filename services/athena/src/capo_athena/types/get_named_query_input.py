"""Generated from Smithy shape ``com.amazonaws.athena#GetNamedQueryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_athena.errors import DeserializationError

if TYPE_CHECKING:
    import capo_athena.types.named_query_id


class GetNamedQueryInput(TypedDict, closed=True):
    named_query_id: "capo_athena.types.named_query_id.NamedQueryId"
    """<p>The unique ID of the query. Use <a>ListNamedQueries</a> to get query IDs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetNamedQueryInput) -> dict:
    out: dict = {}
    out["NamedQueryId"] = value["named_query_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetNamedQueryInput:
    out: GetNamedQueryInput = {}  # type: ignore[typeddict-item]
    if "NamedQueryId" in data:
        out["named_query_id"] = data["NamedQueryId"]
    else:
        raise DeserializationError("GetNamedQueryInput.named_query_id required")
    return out
