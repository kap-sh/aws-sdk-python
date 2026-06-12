"""Generated from Smithy shape ``com.amazonaws.sesv2#Metric``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

"""<p>The metric to export, can be one of the following:</p> <ul> <li> <p> <code>SEND</code> - Emails sent eligible for tracking in the VDM dashboard. This excludes emails sent to the mailbox simulator and emails addressed to more than one recipient.</p> </li> <li> <p> <code>COMPLAINT</code> - Complaints received for your account. This excludes complaints from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those for emails addressed to more than one recipient</p> </li> <li> <p> <code>PERMANENT_BOUNCE</code> - Permanent bounces - i.e., feedback received for emails sent to non-existent mailboxes. Excludes bounces from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those for emails addressed to more than one recipient.</p> </li> <li> <p> <code>TRANSIENT_BOUNCE</code> - Transient bounces - i.e., feedback received for delivery failures excluding issues with non-existent mailboxes. Excludes bounces from the mailbox simulator, and those for emails addressed to more than one recipient.</p> </li> <li> <p> <code>OPEN</code> - Unique open events for emails including open trackers. Excludes opens for emails addressed to more than one recipient.</p> </li> <li> <p> <code>CLICK</code> - Unique click events for emails including wrapped links. Excludes clicks for emails addressed to more than one recipient.</p> </li> <li> <p> <code>DELIVERY</code> - Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator and for emails addressed to more than one recipient.</p> </li> <li> <p> <code>DELIVERY_OPEN</code> - Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails without open trackers.</p> </li> <li> <p> <code>DELIVERY_CLICK</code> - Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails without click trackers.</p> </li> <li> <p> <code>DELIVERY_COMPLAINT</code> - Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails addressed to recipients hosted by ISPs with which Amazon SES does not have a feedback loop agreement.</p> </li> </ul>"""
Metric: TypeAlias = Literal[
    "SEND",
    "COMPLAINT",
    "PERMANENT_BOUNCE",
    "TRANSIENT_BOUNCE",
    "OPEN",
    "CLICK",
    "DELIVERY",
    "DELIVERY_OPEN",
    "DELIVERY_CLICK",
    "DELIVERY_COMPLAINT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SEND",
        "COMPLAINT",
        "PERMANENT_BOUNCE",
        "TRANSIENT_BOUNCE",
        "OPEN",
        "CLICK",
        "DELIVERY",
        "DELIVERY_OPEN",
        "DELIVERY_CLICK",
        "DELIVERY_COMPLAINT",
    )
)


def serialize_json(value: Metric) -> str:
    return value


def deserialize_json(data: str) -> Metric:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Metric value: {data!r}")
    return cast(Metric, data)
