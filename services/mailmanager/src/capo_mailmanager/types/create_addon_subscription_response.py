"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateAddonSubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.addon_subscription_id


class CreateAddonSubscriptionResponse(TypedDict, closed=True):
    addon_subscription_id: (
        "capo_mailmanager.types.addon_subscription_id.AddonSubscriptionId"
    )
    """<p>The unique ID of the Add On subscription created by this API.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAddonSubscriptionResponse) -> dict:
    out: dict = {}
    out["AddonSubscriptionId"] = value["addon_subscription_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAddonSubscriptionResponse:
    out: CreateAddonSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if "AddonSubscriptionId" in data:
        out["addon_subscription_id"] = data["AddonSubscriptionId"]
    else:
        raise DeserializationError(
            "CreateAddonSubscriptionResponse.addon_subscription_id required"
        )
    return out
