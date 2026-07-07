"""Generated from Smithy shape ``com.amazonaws.kendra#ListExperienceEntitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.experience_id
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.next_token


class ListExperienceEntitiesRequest(TypedDict, closed=True):
    id: "aws_sdk_kendra.types.experience_id.ExperienceId"
    """<p>The identifier of your Amazon Kendra experience.</p>"""
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for your Amazon Kendra experience.</p>"""
    next_token: NotRequired["aws_sdk_kendra.types.next_token.NextToken"]
    """<p>If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of users or groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListExperienceEntitiesRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["IndexId"] = value["index_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListExperienceEntitiesRequest:
    out: ListExperienceEntitiesRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("ListExperienceEntitiesRequest.id required")
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("ListExperienceEntitiesRequest.index_id required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
