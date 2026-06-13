"""Generated from Smithy shape ``com.amazonaws.freetier#ListAccountActivitiesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_freetier.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_freetier.types.activities
    import aws_sdk_freetier.types.next_page_token


class ListAccountActivitiesResponse(TypedDict):
    activities: "aws_sdk_freetier.types.activities.Activities"
    """<p> A brief information about the activities. </p>"""
    next_token: NotRequired["aws_sdk_freetier.types.next_page_token.NextPageToken"]
    """<p> The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAccountActivitiesResponse) -> dict:
    out: dict = {}
    import aws_sdk_freetier.types.activities

    out["activities"] = aws_sdk_freetier.types.activities.serialize_aws_json_1_0(
        value["activities"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAccountActivitiesResponse:
    out: ListAccountActivitiesResponse = {}  # type: ignore[typeddict-item]
    if "activities" in data:
        import aws_sdk_freetier.types.activities

        out["activities"] = aws_sdk_freetier.types.activities.deserialize_aws_json_1_0(
            data["activities"]
        )
    else:
        raise DeserializationError("ListAccountActivitiesResponse.activities required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
