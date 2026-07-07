"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListTestGridProjectsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.max_page_size
    import aws_sdk_device_farm.types.pagination_token


class ListTestGridProjectsRequest(TypedDict, closed=True):
    max_result: NotRequired["aws_sdk_device_farm.types.max_page_size.MaxPageSize"]
    """<p>Return no more than this number of results.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>From a response, used to continue a paginated listing. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTestGridProjectsRequest) -> dict:
    out: dict = {}
    if "max_result" in value:
        out["maxResult"] = value["max_result"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTestGridProjectsRequest:
    out: ListTestGridProjectsRequest = {}  # type: ignore[typeddict-item]
    if "maxResult" in data:
        out["max_result"] = data["maxResult"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
