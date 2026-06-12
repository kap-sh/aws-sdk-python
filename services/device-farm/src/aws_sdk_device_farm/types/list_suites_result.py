"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListSuitesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.pagination_token
    import aws_sdk_device_farm.types.suites


class ListSuitesResult(TypedDict):
    suites: NotRequired["aws_sdk_device_farm.types.suites.Suites"]
    """<p>Information about the suites.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSuitesResult) -> dict:
    out: dict = {}
    if "suites" in value:
        import aws_sdk_device_farm.types.suites

        out["suites"] = aws_sdk_device_farm.types.suites.serialize_aws_json_1_1(
            value["suites"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSuitesResult:
    out: ListSuitesResult = {}  # type: ignore[typeddict-item]
    if "suites" in data:
        import aws_sdk_device_farm.types.suites

        out["suites"] = aws_sdk_device_farm.types.suites.deserialize_aws_json_1_1(
            data["suites"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
