"""Generated from Smithy shape ``com.amazonaws.qbusiness#ListApplicationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.applications
    import aws_sdk_qbusiness.types.next_token


class ListApplicationsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_qbusiness.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon Q Business returns this token. You can use this token in a subsequent request to retrieve the next set of applications.</p>"""
    applications: NotRequired["aws_sdk_qbusiness.types.applications.Applications"]
    """<p>An array of summary information on the configuration of one or more Amazon Q Business applications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "applications" in value:
        import aws_sdk_qbusiness.types.applications

        out["applications"] = aws_sdk_qbusiness.types.applications.serialize_json(
            value["applications"]
        )
    return out


def deserialize_json(data: dict) -> ListApplicationsResponse:
    out: ListApplicationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "applications" in data:
        import aws_sdk_qbusiness.types.applications

        out["applications"] = aws_sdk_qbusiness.types.applications.deserialize_json(
            data["applications"]
        )
    return out
