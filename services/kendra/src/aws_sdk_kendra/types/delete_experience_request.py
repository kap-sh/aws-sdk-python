"""Generated from Smithy shape ``com.amazonaws.kendra#DeleteExperienceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.experience_id
    import aws_sdk_kendra.types.index_id


class DeleteExperienceRequest(TypedDict, closed=True):
    id: "aws_sdk_kendra.types.experience_id.ExperienceId"
    """<p>The identifier of your Amazon Kendra experience you want to delete.</p>"""
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for your Amazon Kendra experience.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteExperienceRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["IndexId"] = value["index_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteExperienceRequest:
    out: DeleteExperienceRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DeleteExperienceRequest.id required")
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("DeleteExperienceRequest.index_id required")
    return out
