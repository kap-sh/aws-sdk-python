"""Generated from Smithy shape ``com.amazonaws.notifications#ListOrganizationalUnitsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_notifications.types.next_token
    import aws_sdk_notifications.types.notification_configuration_arn


class ListOrganizationalUnitsRequest(TypedDict, closed=True):
    notification_configuration_arn: "aws_sdk_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the notification configuration used to filter the organizational units.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of organizational units to return in a single call. Valid values are 1-100.</p>"""
    next_token: NotRequired["aws_sdk_notifications.types.next_token.NextToken"]
    """<p>The token for the next page of results. Use the value returned in the previous response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrganizationalUnitsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListOrganizationalUnitsRequest:
    out: ListOrganizationalUnitsRequest = {}  # type: ignore[typeddict-item]
    return out
