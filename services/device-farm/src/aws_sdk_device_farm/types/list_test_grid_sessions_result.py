"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListTestGridSessionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.pagination_token
    import aws_sdk_device_farm.types.test_grid_sessions


class ListTestGridSessionsResult(TypedDict):
    test_grid_sessions: NotRequired[
        "aws_sdk_device_farm.types.test_grid_sessions.TestGridSessions"
    ]
    """<p>The sessions that match the criteria in a <a>ListTestGridSessionsRequest</a>. </p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>Pagination token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTestGridSessionsResult) -> dict:
    out: dict = {}
    if "test_grid_sessions" in value:
        import aws_sdk_device_farm.types.test_grid_sessions

        out["testGridSessions"] = (
            aws_sdk_device_farm.types.test_grid_sessions.serialize_aws_json_1_1(
                value["test_grid_sessions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTestGridSessionsResult:
    out: ListTestGridSessionsResult = {}  # type: ignore[typeddict-item]
    if "testGridSessions" in data:
        import aws_sdk_device_farm.types.test_grid_sessions

        out["test_grid_sessions"] = (
            aws_sdk_device_farm.types.test_grid_sessions.deserialize_aws_json_1_1(
                data["testGridSessions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
