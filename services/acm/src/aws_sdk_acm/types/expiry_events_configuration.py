"""Generated from Smithy shape ``com.amazonaws.acm#ExpiryEventsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_acm.types.positive_integer


class ExpiryEventsConfiguration(TypedDict, closed=True):
    days_before_expiry: NotRequired[
        "aws_sdk_acm.types.positive_integer.PositiveInteger"
    ]
    """<p>Specifies the number of days prior to certificate expiration when ACM starts generating <code>EventBridge</code> events. ACM sends one event per day per certificate until the certificate expires. By default, accounts receive events starting 45 days before certificate expiration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpiryEventsConfiguration) -> dict:
    out: dict = {}
    if "days_before_expiry" in value:
        out["DaysBeforeExpiry"] = value["days_before_expiry"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpiryEventsConfiguration:
    out: ExpiryEventsConfiguration = {}  # type: ignore[typeddict-item]
    if "DaysBeforeExpiry" in data:
        out["days_before_expiry"] = data["DaysBeforeExpiry"]
    return out
