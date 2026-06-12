"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListTestGridSessionActionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.device_farm_arn
    import aws_sdk_device_farm.types.max_page_size
    import aws_sdk_device_farm.types.pagination_token


class ListTestGridSessionActionsRequest(TypedDict):
    session_arn: "aws_sdk_device_farm.types.device_farm_arn.DeviceFarmArn"
    """<p>The ARN of the session to retrieve.</p>"""
    max_result: NotRequired["aws_sdk_device_farm.types.max_page_size.MaxPageSize"]
    """<p>The maximum number of sessions to return per response.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>Pagination token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTestGridSessionActionsRequest) -> dict:
    out: dict = {}
    out["sessionArn"] = value["session_arn"]
    if "max_result" in value:
        out["maxResult"] = value["max_result"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTestGridSessionActionsRequest:
    out: ListTestGridSessionActionsRequest = {}  # type: ignore[typeddict-item]
    if "sessionArn" in data:
        out["session_arn"] = data["sessionArn"]
    else:
        raise DeserializationError(
            "ListTestGridSessionActionsRequest.session_arn required"
        )
    if "maxResult" in data:
        out["max_result"] = data["maxResult"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
