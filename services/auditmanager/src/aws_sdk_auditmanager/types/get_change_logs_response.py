"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetChangeLogsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.change_logs
    import aws_sdk_auditmanager.types.token


class GetChangeLogsResponse(TypedDict):
    change_logs: NotRequired["aws_sdk_auditmanager.types.change_logs.ChangeLogs"]
    """<p>The list of user activity for the control. </p>"""
    next_token: NotRequired["aws_sdk_auditmanager.types.token.Token"]
    """<p>The pagination token that's used to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetChangeLogsResponse) -> dict:
    out: dict = {}
    if "change_logs" in value:
        import aws_sdk_auditmanager.types.change_logs

        out["changeLogs"] = aws_sdk_auditmanager.types.change_logs.serialize_json(
            value["change_logs"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetChangeLogsResponse:
    out: GetChangeLogsResponse = {}  # type: ignore[typeddict-item]
    if "changeLogs" in data:
        import aws_sdk_auditmanager.types.change_logs

        out["change_logs"] = aws_sdk_auditmanager.types.change_logs.deserialize_json(
            data["changeLogs"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
