"""Generated from Smithy shape ``com.amazonaws.kendra#DeleteIndexRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.index_id


class DeleteIndexRequest(TypedDict):
    id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIndexRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIndexRequest:
    out: DeleteIndexRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DeleteIndexRequest.id required")
    return out
