"""Generated from Smithy shape ``com.amazonaws.workdocs#CreateNotificationSubscriptionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.subscription


class CreateNotificationSubscriptionResponse(TypedDict):
    subscription: NotRequired["aws_sdk_workdocs.types.subscription.Subscription"]
    """<p>The subscription.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNotificationSubscriptionResponse) -> dict:
    out: dict = {}
    if "subscription" in value:
        import aws_sdk_workdocs.types.subscription

        out["Subscription"] = aws_sdk_workdocs.types.subscription.serialize_json(
            value["subscription"]
        )
    return out


def deserialize_json(data: dict) -> CreateNotificationSubscriptionResponse:
    out: CreateNotificationSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if "Subscription" in data:
        import aws_sdk_workdocs.types.subscription

        out["subscription"] = aws_sdk_workdocs.types.subscription.deserialize_json(
            data["Subscription"]
        )
    return out
