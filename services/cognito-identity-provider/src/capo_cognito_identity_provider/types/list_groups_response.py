"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ListGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.group_list_type
    import capo_cognito_identity_provider.types.pagination_key


class ListGroupsResponse(TypedDict, closed=True):
    groups: NotRequired[
        "capo_cognito_identity_provider.types.group_list_type.GroupListType"
    ]
    """<p>An array of groups and their details. Each entry that's returned includes description, precedence, and IAM role values.</p>"""
    next_token: NotRequired[
        "capo_cognito_identity_provider.types.pagination_key.PaginationKey"
    ]
    """<p>The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGroupsResponse) -> dict:
    out: dict = {}
    if "groups" in value:
        import capo_cognito_identity_provider.types.group_list_type

        out["Groups"] = (
            capo_cognito_identity_provider.types.group_list_type.serialize_aws_json_1_1(
                value["groups"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGroupsResponse:
    out: ListGroupsResponse = {}  # type: ignore[typeddict-item]
    if "Groups" in data:
        import capo_cognito_identity_provider.types.group_list_type

        out["groups"] = (
            capo_cognito_identity_provider.types.group_list_type.deserialize_aws_json_1_1(
                data["Groups"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
