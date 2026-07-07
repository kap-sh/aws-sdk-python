"""Generated from Smithy shape ``com.amazonaws.b2bi#ListProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.page_token
    import aws_sdk_b2bi.types.profile_list


class ListProfilesResponse(TypedDict, closed=True):
    profiles: "aws_sdk_b2bi.types.profile_list.ProfileList"
    """<p>Returns an array of <code>ProfileSummary</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_b2bi.types.page_token.PageToken"]
    """<p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListProfilesResponse) -> dict:
    out: dict = {}
    import aws_sdk_b2bi.types.profile_list

    out["profiles"] = aws_sdk_b2bi.types.profile_list.serialize_aws_json_1_0(
        value["profiles"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListProfilesResponse:
    out: ListProfilesResponse = {}  # type: ignore[typeddict-item]
    if "profiles" in data:
        import aws_sdk_b2bi.types.profile_list

        out["profiles"] = aws_sdk_b2bi.types.profile_list.deserialize_aws_json_1_0(
            data["profiles"]
        )
    else:
        raise DeserializationError("ListProfilesResponse.profiles required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
