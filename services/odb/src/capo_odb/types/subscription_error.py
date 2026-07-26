"""Generated from Smithy shape ``com.amazonaws.odb#SubscriptionError``."""

from typing_extensions import NotRequired, TypedDict


class SubscriptionError(TypedDict, closed=True):
    error_message: NotRequired["str"]
    """<p>A human-readable message that describes the subscription error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SubscriptionError) -> dict:
    out: dict = {}
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SubscriptionError:
    out: SubscriptionError = {}  # type: ignore[typeddict-item]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
