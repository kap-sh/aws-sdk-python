"""Generated from Smithy shape ``com.amazonaws.datazone#ListNotificationsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.notification_subjects
    import aws_sdk_datazone.types.notification_type
    import aws_sdk_datazone.types.pagination_token
    import aws_sdk_datazone.types.task_status


class ListNotificationsInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    type: "aws_sdk_datazone.types.notification_type.NotificationType"
    """<p>The type of notifications.</p>"""
    after_timestamp: NotRequired["datetime.datetime"]
    """<p>The time after which you want to list notifications.</p>"""
    before_timestamp: NotRequired["datetime.datetime"]
    """<p>The time before which you want to list notifications.</p>"""
    subjects: NotRequired[
        "aws_sdk_datazone.types.notification_subjects.NotificationSubjects"
    ]
    """<p>The subjects of notifications.</p>"""
    task_status: NotRequired["aws_sdk_datazone.types.task_status.TaskStatus"]
    """<p>The task status of notifications.</p>"""
    max_results: NotRequired["aws_sdk_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of notifications to return in a single call to <code>ListNotifications</code>. When the number of notifications to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListNotifications</code> to list the next set of notifications.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of notifications is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of notifications, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListNotifications</code> to list the next set of notifications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotificationsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNotificationsInput:
    out: ListNotificationsInput = {}  # type: ignore[typeddict-item]
    return out
