"""Generated from Smithy shape ``com.amazonaws.kendra#DescribeQuerySuggestionsConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.index_id


class DescribeQuerySuggestionsConfigRequest(TypedDict, closed=True):
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index with query suggestions that you want to get information on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeQuerySuggestionsConfigRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeQuerySuggestionsConfigRequest:
    out: DescribeQuerySuggestionsConfigRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError(
            "DescribeQuerySuggestionsConfigRequest.index_id required"
        )
    return out
