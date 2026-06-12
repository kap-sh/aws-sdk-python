"""Generated from Smithy shape ``com.amazonaws.notifications#ListMemberAccountsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_notifications.types.account_id
    import aws_sdk_notifications.types.member_account_notification_configuration_status
    import aws_sdk_notifications.types.next_token
    import aws_sdk_notifications.types.notification_configuration_arn
    import aws_sdk_notifications.types.organizational_unit_id

class ListMemberAccountsRequest(TypedDict):
    notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the notification configuration used to filter the member accounts.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single call. Valid values are 1-100.</p>"""
    next_token: NotRequired["aws_sdk_notifications.types.next_token.NextToken"]
    """<p>The token for the next page of results. Use the value returned in the previous response.</p>"""
    member_account: NotRequired["aws_sdk_notifications.types.account_id.AccountId"]
    """<p>The member account identifier used to filter the results.</p>"""
    status: NotRequired["aws_sdk_notifications.types.member_account_notification_configuration_status.MemberAccountNotificationConfigurationStatus"]
    """<p>The status used to filter the member accounts.</p>"""
    organizational_unit_id: NotRequired["aws_sdk_notifications.types.organizational_unit_id.OrganizationalUnitId"]
    """<p>The organizational unit ID used to filter the member accounts.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ListMemberAccountsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMemberAccountsRequest:
    out: ListMemberAccountsRequest = {}  # type: ignore[typeddict-item]
    return out