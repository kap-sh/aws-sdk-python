"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListSamplesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name
    import aws_sdk_device_farm.types.pagination_token


class ListSamplesRequest(TypedDict, closed=True):
    arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the job used to list samples.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSamplesRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSamplesRequest:
    out: ListSamplesRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ListSamplesRequest.arn required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
