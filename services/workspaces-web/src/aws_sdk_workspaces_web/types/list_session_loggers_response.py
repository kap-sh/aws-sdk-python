"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ListSessionLoggersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.pagination_token
    import aws_sdk_workspaces_web.types.session_logger_list


class ListSessionLoggersResponse(TypedDict, closed=True):
    session_loggers: NotRequired[
        "aws_sdk_workspaces_web.types.session_logger_list.SessionLoggerList"
    ]
    """<p>The list of session loggers, including summaries of their details.</p>"""
    next_token: NotRequired[
        "aws_sdk_workspaces_web.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionLoggersResponse) -> dict:
    out: dict = {}
    if "session_loggers" in value:
        import aws_sdk_workspaces_web.types.session_logger_list

        out["sessionLoggers"] = (
            aws_sdk_workspaces_web.types.session_logger_list.serialize_json(
                value["session_loggers"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSessionLoggersResponse:
    out: ListSessionLoggersResponse = {}  # type: ignore[typeddict-item]
    if "sessionLoggers" in data:
        import aws_sdk_workspaces_web.types.session_logger_list

        out["session_loggers"] = (
            aws_sdk_workspaces_web.types.session_logger_list.deserialize_json(
                data["sessionLoggers"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
