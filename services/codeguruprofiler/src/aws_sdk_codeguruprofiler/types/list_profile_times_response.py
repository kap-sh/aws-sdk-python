"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ListProfileTimesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.pagination_token
    import aws_sdk_codeguruprofiler.types.profile_times


class ListProfileTimesResponse(TypedDict):
    profile_times: "aws_sdk_codeguruprofiler.types.profile_times.ProfileTimes"
    """<p>The list of start times of the available profiles for the aggregation period in the specified time range. </p>"""
    next_token: NotRequired[
        "aws_sdk_codeguruprofiler.types.pagination_token.PaginationToken"
    ]
    """<p>The <code>nextToken</code> value to include in a future <code>ListProfileTimes</code> request. When the results of a <code>ListProfileTimes</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfileTimesResponse) -> dict:
    out: dict = {}
    import aws_sdk_codeguruprofiler.types.profile_times

    out["profileTimes"] = aws_sdk_codeguruprofiler.types.profile_times.serialize_json(
        value["profile_times"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProfileTimesResponse:
    out: ListProfileTimesResponse = {}  # type: ignore[typeddict-item]
    if "profileTimes" in data:
        import aws_sdk_codeguruprofiler.types.profile_times

        out["profile_times"] = (
            aws_sdk_codeguruprofiler.types.profile_times.deserialize_json(
                data["profileTimes"]
            )
        )
    else:
        raise DeserializationError("ListProfileTimesResponse.profile_times required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
