"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#GetIndexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.index_schema


class GetIndexResponse(TypedDict, closed=True):
    index_schema: NotRequired[
        "capo_opensearchserverless.types.index_schema.IndexSchema"
    ]
    """<p>The JSON schema definition for the index, including field mappings and settings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetIndexResponse) -> dict:
    out: dict = {}
    if "index_schema" in value:
        out["indexSchema"] = value["index_schema"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetIndexResponse:
    out: GetIndexResponse = {}  # type: ignore[typeddict-item]
    if "indexSchema" in data:
        out["index_schema"] = data["indexSchema"]
    return out
