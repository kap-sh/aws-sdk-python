"""Generated from Smithy shape ``com.amazonaws.kendra#DescribeThesaurusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.index_id
    import capo_kendra.types.thesaurus_id


class DescribeThesaurusRequest(TypedDict, closed=True):
    id: "capo_kendra.types.thesaurus_id.ThesaurusId"
    """<p>The identifier of the thesaurus you want to get information on.</p>"""
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for the thesaurus.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeThesaurusRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["IndexId"] = value["index_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeThesaurusRequest:
    out: DescribeThesaurusRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DescribeThesaurusRequest.id required")
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("DescribeThesaurusRequest.index_id required")
    return out
