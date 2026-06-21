"""Generated from Smithy shape ``com.amazonaws.sesv2#DeliveryEventType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of delivery events:</p> <ul> <li> <p> <code>SEND</code> - The send request was successful and SES will attempt to deliver the message to the recipient’s mail server. (If account-level or global suppression is being used, SES will still count it as a send, but delivery is suppressed.)</p> </li> <li> <p> <code>DELIVERY</code> - SES successfully delivered the email to the recipient's mail server. Excludes deliveries to the mailbox simulator and emails addressed to more than one recipient.</p> </li> <li> <p> <code>TRANSIENT_BOUNCE</code> - Feedback received for delivery failures excluding issues with non-existent mailboxes. Excludes bounces from the mailbox simulator, and those from emails addressed to more than one recipient.</p> </li> <li> <p> <code>PERMANENT_BOUNCE</code> - Feedback received for emails sent to non-existent mailboxes. Excludes bounces from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those from emails addressed to more than one recipient.</p> </li> <li> <p> <code>UNDETERMINED_BOUNCE</code> - SES was unable to determine the bounce reason.</p> </li> <li> <p> <code>COMPLAINT</code> - Complaint received for the email. This excludes complaints from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those from emails addressed to more than one recipient.</p> </li> </ul>"""
DeliveryEventType: TypeAlias = Literal[
    "SEND",
    "DELIVERY",
    "TRANSIENT_BOUNCE",
    "PERMANENT_BOUNCE",
    "UNDETERMINED_BOUNCE",
    "COMPLAINT",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeliveryEventType) -> str:
    return value


def deserialize_json(data: str) -> DeliveryEventType:
    return cast(DeliveryEventType, data)
