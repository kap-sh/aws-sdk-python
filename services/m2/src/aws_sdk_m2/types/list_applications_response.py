"""Generated from Smithy shape ``com.amazonaws.m2#ListApplicationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.application_summary_list
    import aws_sdk_m2.types.next_token


class ListApplicationsResponse(TypedDict, closed=True):
    applications: "aws_sdk_m2.types.application_summary_list.ApplicationSummaryList"
    """<p>Returns a list of summary details for all the applications in a runtime environment.</p>"""
    next_token: NotRequired["aws_sdk_m2.types.next_token.NextToken"]
    """<p>A pagination token that's returned when the response doesn't contain all applications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_m2.types.application_summary_list

    out["applications"] = aws_sdk_m2.types.application_summary_list.serialize_json(
        value["applications"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationsResponse:
    out: ListApplicationsResponse = {}  # type: ignore[typeddict-item]
    if "applications" in data:
        import aws_sdk_m2.types.application_summary_list

        out["applications"] = (
            aws_sdk_m2.types.application_summary_list.deserialize_json(
                data["applications"]
            )
        )
    else:
        raise DeserializationError("ListApplicationsResponse.applications required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
