"""Generated from Smithy shape ``com.amazonaws.connect#ListSecurityProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.security_profile_summary_list


class ListSecurityProfilesResponse(TypedDict, closed=True):
    security_profile_summary_list: NotRequired[
        "aws_sdk_connect.types.security_profile_summary_list.SecurityProfileSummaryList"
    ]
    """<p>Information about the security profiles.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityProfilesResponse) -> dict:
    out: dict = {}
    if "security_profile_summary_list" in value:
        import aws_sdk_connect.types.security_profile_summary_list

        out["SecurityProfileSummaryList"] = (
            aws_sdk_connect.types.security_profile_summary_list.serialize_json(
                value["security_profile_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSecurityProfilesResponse:
    out: ListSecurityProfilesResponse = {}  # type: ignore[typeddict-item]
    if "SecurityProfileSummaryList" in data:
        import aws_sdk_connect.types.security_profile_summary_list

        out["security_profile_summary_list"] = (
            aws_sdk_connect.types.security_profile_summary_list.deserialize_json(
                data["SecurityProfileSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
