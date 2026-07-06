"""Generated from Smithy shape ``com.amazonaws.kendra#DeleteThesaurusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.thesaurus_id


class DeleteThesaurusRequest(TypedDict, closed=True):
    id: "aws_sdk_kendra.types.thesaurus_id.ThesaurusId"
    """<p>The identifier of the thesaurus you want to delete.</p>"""
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for the thesaurus.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteThesaurusRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["IndexId"] = value["index_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteThesaurusRequest:
    out: DeleteThesaurusRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DeleteThesaurusRequest.id required")
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("DeleteThesaurusRequest.index_id required")
    return out
