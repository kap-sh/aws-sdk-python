"""Generated from Smithy shape ``com.amazonaws.pinpointemail#PinpointDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.amazon_resource_name


class PinpointDestination(TypedDict, closed=True):
    application_arn: NotRequired[
        "capo_pinpoint_email.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Pinpoint project that you want to send email events to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PinpointDestination) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_json(data: dict) -> PinpointDestination:
    out: PinpointDestination = {}  # type: ignore[typeddict-item]
    if "ApplicationArn" in data:
        out["application_arn"] = data["ApplicationArn"]
    return out
