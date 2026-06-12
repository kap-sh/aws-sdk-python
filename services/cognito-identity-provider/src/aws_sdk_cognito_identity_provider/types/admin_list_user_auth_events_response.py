"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminListUserAuthEventsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.auth_events_type
    import aws_sdk_cognito_identity_provider.types.pagination_key


class AdminListUserAuthEventsResponse(TypedDict):
    auth_events: NotRequired[
        "aws_sdk_cognito_identity_provider.types.auth_events_type.AuthEventsType"
    ]
    """<p>The response object. It includes the <code>EventID</code>, <code>EventType</code>, <code>CreationDate</code>, <code>EventRisk</code>, and <code>EventResponse</code>.</p>"""
    next_token: NotRequired[
        "aws_sdk_cognito_identity_provider.types.pagination_key.PaginationKey"
    ]
    """<p>The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminListUserAuthEventsResponse) -> dict:
    out: dict = {}
    if "auth_events" in value:
        import aws_sdk_cognito_identity_provider.types.auth_events_type

        out["AuthEvents"] = (
            aws_sdk_cognito_identity_provider.types.auth_events_type.serialize_aws_json_1_1(
                value["auth_events"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminListUserAuthEventsResponse:
    out: AdminListUserAuthEventsResponse = {}  # type: ignore[typeddict-item]
    if "AuthEvents" in data:
        import aws_sdk_cognito_identity_provider.types.auth_events_type

        out["auth_events"] = (
            aws_sdk_cognito_identity_provider.types.auth_events_type.deserialize_aws_json_1_1(
                data["AuthEvents"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
