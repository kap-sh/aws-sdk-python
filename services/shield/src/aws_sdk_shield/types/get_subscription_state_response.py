"""Generated from Smithy shape ``com.amazonaws.shield#GetSubscriptionStateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_shield.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_shield.types.subscription_state


class GetSubscriptionStateResponse(TypedDict):
    subscription_state: "aws_sdk_shield.types.subscription_state.SubscriptionState"
    """<p>The status of the subscription.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSubscriptionStateResponse) -> dict:
    out: dict = {}
    import aws_sdk_shield.types.subscription_state

    out["SubscriptionState"] = (
        aws_sdk_shield.types.subscription_state.serialize_aws_json_1_1(
            value["subscription_state"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSubscriptionStateResponse:
    out: GetSubscriptionStateResponse = {}  # type: ignore[typeddict-item]
    if "SubscriptionState" in data:
        import aws_sdk_shield.types.subscription_state

        out["subscription_state"] = (
            aws_sdk_shield.types.subscription_state.deserialize_aws_json_1_1(
                data["SubscriptionState"]
            )
        )
    else:
        raise DeserializationError(
            "GetSubscriptionStateResponse.subscription_state required"
        )
    return out
