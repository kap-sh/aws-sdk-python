"""Generated from Smithy shape ``com.amazonaws.transfer#ListProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.listed_profiles
    import aws_sdk_transfer.types.next_token


class ListProfilesResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_transfer.types.next_token.NextToken"]
    """<p>Returns a token that you can use to call <code>ListProfiles</code> again and receive additional results, if there are any.</p>"""
    profiles: "aws_sdk_transfer.types.listed_profiles.ListedProfiles"
    """<p>Returns an array, where each item contains the details of a profile.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProfilesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import aws_sdk_transfer.types.listed_profiles

    out["Profiles"] = aws_sdk_transfer.types.listed_profiles.serialize_aws_json_1_1(
        value["profiles"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProfilesResponse:
    out: ListProfilesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Profiles" in data:
        import aws_sdk_transfer.types.listed_profiles

        out["profiles"] = (
            aws_sdk_transfer.types.listed_profiles.deserialize_aws_json_1_1(
                data["Profiles"]
            )
        )
    else:
        raise DeserializationError("ListProfilesResponse.profiles required")
    return out
