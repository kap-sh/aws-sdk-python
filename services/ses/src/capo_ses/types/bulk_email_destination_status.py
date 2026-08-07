"""Generated from Smithy shape ``com.amazonaws.ses#BulkEmailDestinationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.bulk_email_status
    import capo_ses.types.error
    import capo_ses.types.message_id


class BulkEmailDestinationStatus(TypedDict, closed=True):
    status: NotRequired["capo_ses.types.bulk_email_status.BulkEmailStatus"]
    """<p>The status of a message sent using the <code>SendBulkTemplatedEmail</code> operation.</p> <p>Possible values for this parameter include:</p> <ul> <li> <p> <code>Success</code>: Amazon SES accepted the message, and attempts to deliver it to the recipients.</p> </li> <li> <p> <code>MessageRejected</code>: The message was rejected because it contained a virus.</p> </li> <li> <p> <code>MailFromDomainNotVerified</code>: The sender's email address or domain was not verified.</p> </li> <li> <p> <code>ConfigurationSetDoesNotExist</code>: The configuration set you specified does not exist.</p> </li> <li> <p> <code>TemplateDoesNotExist</code>: The template you specified does not exist.</p> </li> <li> <p> <code>AccountSuspended</code>: Your account has been shut down because of issues related to your email sending practices.</p> </li> <li> <p> <code>AccountThrottled</code>: The number of emails you can send has been reduced because your account has exceeded its allocated sending limit.</p> </li> <li> <p> <code>AccountDailyQuotaExceeded</code>: You have reached or exceeded the maximum number of emails you can send from your account in a 24-hour period.</p> </li> <li> <p> <code>InvalidSendingPoolName</code>: The configuration set you specified refers to an IP pool that does not exist.</p> </li> <li> <p> <code>AccountSendingPaused</code>: Email sending for the Amazon SES account was disabled using the <a>UpdateAccountSendingEnabled</a> operation.</p> </li> <li> <p> <code>ConfigurationSetSendingPaused</code>: Email sending for this configuration set was disabled using the <a>UpdateConfigurationSetSendingEnabled</a> operation.</p> </li> <li> <p> <code>InvalidParameterValue</code>: One or more of the parameters you specified when calling this operation was invalid. See the error message for additional information.</p> </li> <li> <p> <code>TransientFailure</code>: Amazon SES was unable to process your request because of a temporary issue.</p> </li> <li> <p> <code>Failed</code>: Amazon SES was unable to process your request. See the error message for additional information.</p> </li> </ul>"""
    error: NotRequired["capo_ses.types.error.Error"]
    """<p>A description of an error that prevented a message being sent using the <code>SendBulkTemplatedEmail</code> operation.</p>"""
    message_id: NotRequired["capo_ses.types.message_id.MessageId"]
    """<p>The unique message identifier returned from the <code>SendBulkTemplatedEmail</code> operation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BulkEmailDestinationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "status" in value:
        import capo_ses.types.bulk_email_status

        capo_ses.types.bulk_email_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "error" in value:
        pairs.append((f"{key_prefix}Error", str(value["error"])))
    if "message_id" in value:
        pairs.append((f"{key_prefix}MessageId", str(value["message_id"])))


def deserialize_query(el: Element) -> BulkEmailDestinationStatus:
    out: BulkEmailDestinationStatus = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_ses.types.bulk_email_status

        out["status"] = capo_ses.types.bulk_email_status.deserialize_query(child_status)
    child_error = el.find("Error")
    if child_error is not None:
        out["error"] = str(child_error.text or "")
    child_message_id = el.find("MessageId")
    if child_message_id is not None:
        out["message_id"] = str(child_message_id.text or "")
    return out
