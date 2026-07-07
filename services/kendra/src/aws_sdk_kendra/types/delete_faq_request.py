"""Generated from Smithy shape ``com.amazonaws.kendra#DeleteFaqRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.faq_id
    import aws_sdk_kendra.types.index_id


class DeleteFaqRequest(TypedDict, closed=True):
    id: "aws_sdk_kendra.types.faq_id.FaqId"
    """<p>The identifier of the FAQ you want to remove.</p>"""
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for the FAQ.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFaqRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["IndexId"] = value["index_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFaqRequest:
    out: DeleteFaqRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DeleteFaqRequest.id required")
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("DeleteFaqRequest.index_id required")
    return out
