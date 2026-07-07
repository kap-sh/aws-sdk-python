"""Generated from Smithy shape ``com.amazonaws.kendra#CreateIndexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.index_id


class CreateIndexResponse(TypedDict, closed=True):
    id: NotRequired["aws_sdk_kendra.types.index_id.IndexId"]
    """<p>The identifier of the index. Use this identifier when you query an index, set up a data source, or index a document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateIndexResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateIndexResponse:
    out: CreateIndexResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
