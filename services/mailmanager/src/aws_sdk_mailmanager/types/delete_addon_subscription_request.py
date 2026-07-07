"""Generated from Smithy shape ``com.amazonaws.mailmanager#DeleteAddonSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.addon_subscription_id


class DeleteAddonSubscriptionRequest(TypedDict, closed=True):
    addon_subscription_id: (
        "aws_sdk_mailmanager.types.addon_subscription_id.AddonSubscriptionId"
    )
    """<p>The Add On subscription ID to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAddonSubscriptionRequest) -> dict:
    out: dict = {}
    out["AddonSubscriptionId"] = value["addon_subscription_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAddonSubscriptionRequest:
    out: DeleteAddonSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if "AddonSubscriptionId" in data:
        out["addon_subscription_id"] = data["AddonSubscriptionId"]
    else:
        raise DeserializationError(
            "DeleteAddonSubscriptionRequest.addon_subscription_id required"
        )
    return out
