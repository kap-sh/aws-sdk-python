"""Generated from Smithy shape ``com.amazonaws.workmail#ListMailboxPermissionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.next_token
    import aws_sdk_workmail.types.permissions


class ListMailboxPermissionsResponse(TypedDict):
    permissions: NotRequired["aws_sdk_workmail.types.permissions.Permissions"]
    """<p>One page of the user, group, or resource mailbox permissions.</p>"""
    next_token: NotRequired["aws_sdk_workmail.types.next_token.NextToken"]
    r"""<p>The token to use to retrieve the next page of results. The value is \"null\" when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMailboxPermissionsResponse) -> dict:
    out: dict = {}
    if "permissions" in value:
        import aws_sdk_workmail.types.permissions

        out["Permissions"] = aws_sdk_workmail.types.permissions.serialize_aws_json_1_1(
            value["permissions"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMailboxPermissionsResponse:
    out: ListMailboxPermissionsResponse = {}  # type: ignore[typeddict-item]
    if "Permissions" in data:
        import aws_sdk_workmail.types.permissions

        out["permissions"] = (
            aws_sdk_workmail.types.permissions.deserialize_aws_json_1_1(
                data["Permissions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
