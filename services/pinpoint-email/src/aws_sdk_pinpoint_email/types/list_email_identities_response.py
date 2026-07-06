"""Generated from Smithy shape ``com.amazonaws.pinpointemail#ListEmailIdentitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.identity_info_list
    import aws_sdk_pinpoint_email.types.next_token


class ListEmailIdentitiesResponse(TypedDict, closed=True):
    email_identities: NotRequired[
        "aws_sdk_pinpoint_email.types.identity_info_list.IdentityInfoList"
    ]
    """<p>An array that includes all of the identities associated with your Amazon Pinpoint account.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_email.types.next_token.NextToken"]
    """<p>A token that indicates that there are additional configuration sets to list. To view additional configuration sets, issue another request to <code>ListEmailIdentities</code>, and pass this token in the <code>NextToken</code> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEmailIdentitiesResponse) -> dict:
    out: dict = {}
    if "email_identities" in value:
        import aws_sdk_pinpoint_email.types.identity_info_list

        out["EmailIdentities"] = (
            aws_sdk_pinpoint_email.types.identity_info_list.serialize_json(
                value["email_identities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEmailIdentitiesResponse:
    out: ListEmailIdentitiesResponse = {}  # type: ignore[typeddict-item]
    if "EmailIdentities" in data:
        import aws_sdk_pinpoint_email.types.identity_info_list

        out["email_identities"] = (
            aws_sdk_pinpoint_email.types.identity_info_list.deserialize_json(
                data["EmailIdentities"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
