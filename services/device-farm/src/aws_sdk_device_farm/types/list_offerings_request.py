"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListOfferingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.pagination_token


class ListOfferingsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfferingsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOfferingsRequest:
    out: ListOfferingsRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
