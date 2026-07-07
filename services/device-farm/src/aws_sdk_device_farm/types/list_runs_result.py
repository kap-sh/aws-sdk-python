"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListRunsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.pagination_token
    import aws_sdk_device_farm.types.runs


class ListRunsResult(TypedDict, closed=True):
    runs: NotRequired["aws_sdk_device_farm.types.runs.Runs"]
    """<p>Information about the runs.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRunsResult) -> dict:
    out: dict = {}
    if "runs" in value:
        import aws_sdk_device_farm.types.runs

        out["runs"] = aws_sdk_device_farm.types.runs.serialize_aws_json_1_1(
            value["runs"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRunsResult:
    out: ListRunsResult = {}  # type: ignore[typeddict-item]
    if "runs" in data:
        import aws_sdk_device_farm.types.runs

        out["runs"] = aws_sdk_device_farm.types.runs.deserialize_aws_json_1_1(
            data["runs"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
