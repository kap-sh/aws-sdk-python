"""Generated from Smithy shape ``com.amazonaws.transfer#ListProfilesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transfer.types.max_results
    import aws_sdk_transfer.types.next_token
    import aws_sdk_transfer.types.profile_type


class ListProfilesRequest(TypedDict):
    max_results: NotRequired["aws_sdk_transfer.types.max_results.MaxResults"]
    """<p>The maximum number of items to return.</p>"""
    next_token: NotRequired["aws_sdk_transfer.types.next_token.NextToken"]
    """<p>When there are additional results that were not returned, a <code>NextToken</code> parameter is returned. You can use that value for a subsequent call to <code>ListProfiles</code> to continue listing results.</p>"""
    profile_type: NotRequired["aws_sdk_transfer.types.profile_type.ProfileType"]
    """<p>Indicates whether to list only <code>LOCAL</code> type profiles or only <code>PARTNER</code> type profiles. If not supplied in the request, the command lists all types of profiles.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProfilesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "profile_type" in value:
        import aws_sdk_transfer.types.profile_type

        out["ProfileType"] = aws_sdk_transfer.types.profile_type.serialize_aws_json_1_1(
            value["profile_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProfilesRequest:
    out: ListProfilesRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ProfileType" in data:
        import aws_sdk_transfer.types.profile_type

        out["profile_type"] = (
            aws_sdk_transfer.types.profile_type.deserialize_aws_json_1_1(
                data["ProfileType"]
            )
        )
    return out
