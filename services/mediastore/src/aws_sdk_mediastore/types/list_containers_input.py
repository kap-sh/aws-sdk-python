"""Generated from Smithy shape ``com.amazonaws.mediastore#ListContainersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.container_list_limit
    import aws_sdk_mediastore.types.pagination_token


class ListContainersInput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_mediastore.types.pagination_token.PaginationToken"]
    """<p>Only if you used <code>MaxResults</code> in the first command, enter the token (which was included in the previous response) to obtain the next set of containers. This token is included in a response only if there actually are more containers to list.</p>"""
    max_results: NotRequired[
        "aws_sdk_mediastore.types.container_list_limit.ContainerListLimit"
    ]
    """<p>Enter the maximum number of containers in the response. Use from 1 to 255 characters. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListContainersInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListContainersInput:
    out: ListContainersInput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
