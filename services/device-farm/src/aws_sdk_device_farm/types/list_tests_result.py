"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListTestsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.pagination_token
    import aws_sdk_device_farm.types.tests


class ListTestsResult(TypedDict, closed=True):
    tests: NotRequired["aws_sdk_device_farm.types.tests.Tests"]
    """<p>Information about the tests.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTestsResult) -> dict:
    out: dict = {}
    if "tests" in value:
        import aws_sdk_device_farm.types.tests

        out["tests"] = aws_sdk_device_farm.types.tests.serialize_aws_json_1_1(
            value["tests"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTestsResult:
    out: ListTestsResult = {}  # type: ignore[typeddict-item]
    if "tests" in data:
        import aws_sdk_device_farm.types.tests

        out["tests"] = aws_sdk_device_farm.types.tests.deserialize_aws_json_1_1(
            data["tests"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
