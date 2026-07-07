"""Generated from Smithy shape ``com.amazonaws.devicefarm#ListTestGridSessionActionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.pagination_token
    import aws_sdk_device_farm.types.test_grid_session_actions


class ListTestGridSessionActionsResult(TypedDict, closed=True):
    actions: NotRequired[
        "aws_sdk_device_farm.types.test_grid_session_actions.TestGridSessionActions"
    ]
    """<p>The action taken by the session.</p>"""
    next_token: NotRequired[
        "aws_sdk_device_farm.types.pagination_token.PaginationToken"
    ]
    """<p>Pagination token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTestGridSessionActionsResult) -> dict:
    out: dict = {}
    if "actions" in value:
        import aws_sdk_device_farm.types.test_grid_session_actions

        out["actions"] = (
            aws_sdk_device_farm.types.test_grid_session_actions.serialize_aws_json_1_1(
                value["actions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTestGridSessionActionsResult:
    out: ListTestGridSessionActionsResult = {}  # type: ignore[typeddict-item]
    if "actions" in data:
        import aws_sdk_device_farm.types.test_grid_session_actions

        out["actions"] = (
            aws_sdk_device_farm.types.test_grid_session_actions.deserialize_aws_json_1_1(
                data["actions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
