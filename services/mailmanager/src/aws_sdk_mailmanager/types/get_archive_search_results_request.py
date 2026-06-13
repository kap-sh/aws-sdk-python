"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetArchiveSearchResultsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.search_id


class GetArchiveSearchResultsRequest(TypedDict):
    search_id: "aws_sdk_mailmanager.types.search_id.SearchId"
    """<p>The identifier of the completed search job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetArchiveSearchResultsRequest) -> dict:
    out: dict = {}
    out["SearchId"] = value["search_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetArchiveSearchResultsRequest:
    out: GetArchiveSearchResultsRequest = {}  # type: ignore[typeddict-item]
    if "SearchId" in data:
        out["search_id"] = data["SearchId"]
    else:
        raise DeserializationError("GetArchiveSearchResultsRequest.search_id required")
    return out
