"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListComponentBuildVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.component_summary_list
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.pagination_token


class ListComponentBuildVersionsResponse(TypedDict, closed=True):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    component_summary_list: NotRequired[
        "aws_sdk_imagebuilder.types.component_summary_list.ComponentSummaryList"
    ]
    """<p>The list of component summaries for the specified semantic version.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentBuildVersionsResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "component_summary_list" in value:
        import aws_sdk_imagebuilder.types.component_summary_list

        out["componentSummaryList"] = (
            aws_sdk_imagebuilder.types.component_summary_list.serialize_json(
                value["component_summary_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListComponentBuildVersionsResponse:
    out: ListComponentBuildVersionsResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "componentSummaryList" in data:
        import aws_sdk_imagebuilder.types.component_summary_list

        out["component_summary_list"] = (
            aws_sdk_imagebuilder.types.component_summary_list.deserialize_json(
                data["componentSummaryList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
