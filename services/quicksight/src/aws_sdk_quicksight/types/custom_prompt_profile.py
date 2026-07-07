"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomPromptProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.model_profile_id
    import aws_sdk_quicksight.types.qbs_aws_account_id
    import aws_sdk_quicksight.types.subscription_id


class CustomPromptProfile(TypedDict, closed=True):
    model_profile_id: "aws_sdk_quicksight.types.model_profile_id.ModelProfileId"
    """<p>The identifier of the model profile.</p>"""
    subscription_id: "aws_sdk_quicksight.types.subscription_id.SubscriptionId"
    """<p>The subscription identifier.</p>"""
    qbs_aws_account_id: "aws_sdk_quicksight.types.qbs_aws_account_id.QbsAwsAccountId"
    """<p>The Amazon Web Services account ID for the Q Business service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomPromptProfile) -> dict:
    out: dict = {}
    out["ModelProfileId"] = value["model_profile_id"]
    out["SubscriptionId"] = value["subscription_id"]
    out["QbsAwsAccountId"] = value["qbs_aws_account_id"]
    return out


def deserialize_json(data: dict) -> CustomPromptProfile:
    out: CustomPromptProfile = {}  # type: ignore[typeddict-item]
    if "ModelProfileId" in data:
        out["model_profile_id"] = data["ModelProfileId"]
    else:
        raise DeserializationError("CustomPromptProfile.model_profile_id required")
    if "SubscriptionId" in data:
        out["subscription_id"] = data["SubscriptionId"]
    else:
        raise DeserializationError("CustomPromptProfile.subscription_id required")
    if "QbsAwsAccountId" in data:
        out["qbs_aws_account_id"] = data["QbsAwsAccountId"]
    else:
        raise DeserializationError("CustomPromptProfile.qbs_aws_account_id required")
    return out
