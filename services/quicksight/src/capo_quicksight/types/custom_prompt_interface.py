"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomPromptInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.model_profile_id
    import capo_quicksight.types.qbs_aws_account_id
    import capo_quicksight.types.sensitive_text
    import capo_quicksight.types.style_description
    import capo_quicksight.types.subscription_id


class CustomPromptInterface(TypedDict, closed=True):
    model_profile_id: "capo_quicksight.types.model_profile_id.ModelProfileId"
    """<p>The identifier of the model profile.</p>"""
    subscription_id: "capo_quicksight.types.subscription_id.SubscriptionId"
    """<p>The subscription identifier.</p>"""
    qbs_aws_account_id: "capo_quicksight.types.qbs_aws_account_id.QbsAwsAccountId"
    """<p>The Amazon Web Services account ID for the Q Business service.</p>"""
    response_length: NotRequired[
        "capo_quicksight.types.style_description.StyleDescription"
    ]
    """<p>Instructions for the desired response length.</p>"""
    output_style: NotRequired[
        "capo_quicksight.types.style_description.StyleDescription"
    ]
    """<p>Instructions for the desired output style.</p>"""
    identity: NotRequired["capo_quicksight.types.style_description.StyleDescription"]
    """<p>Instructions that define the agent's identity and persona.</p>"""
    tone: NotRequired["capo_quicksight.types.style_description.StyleDescription"]
    """<p>Instructions for the desired tone of responses.</p>"""
    custom_instructions: NotRequired[
        "capo_quicksight.types.style_description.StyleDescription"
    ]
    """<p>Custom instructions for the agent's behavior.</p>"""
    prompt_summary: NotRequired["capo_quicksight.types.sensitive_text.SensitiveText"]
    """<p>A summary of the custom prompt configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomPromptInterface) -> dict:
    out: dict = {}
    out["ModelProfileId"] = value["model_profile_id"]
    out["SubscriptionId"] = value["subscription_id"]
    out["QbsAwsAccountId"] = value["qbs_aws_account_id"]
    if "response_length" in value:
        out["ResponseLength"] = value["response_length"]
    if "output_style" in value:
        out["OutputStyle"] = value["output_style"]
    if "identity" in value:
        out["Identity"] = value["identity"]
    if "tone" in value:
        out["Tone"] = value["tone"]
    if "custom_instructions" in value:
        out["CustomInstructions"] = value["custom_instructions"]
    if "prompt_summary" in value:
        out["promptSummary"] = value["prompt_summary"]
    return out


def deserialize_json(data: dict) -> CustomPromptInterface:
    out: CustomPromptInterface = {}  # type: ignore[typeddict-item]
    if "ModelProfileId" in data:
        out["model_profile_id"] = data["ModelProfileId"]
    else:
        raise DeserializationError("CustomPromptInterface.model_profile_id required")
    if "SubscriptionId" in data:
        out["subscription_id"] = data["SubscriptionId"]
    else:
        raise DeserializationError("CustomPromptInterface.subscription_id required")
    if "QbsAwsAccountId" in data:
        out["qbs_aws_account_id"] = data["QbsAwsAccountId"]
    else:
        raise DeserializationError("CustomPromptInterface.qbs_aws_account_id required")
    if "ResponseLength" in data:
        out["response_length"] = data["ResponseLength"]
    if "OutputStyle" in data:
        out["output_style"] = data["OutputStyle"]
    if "Identity" in data:
        out["identity"] = data["Identity"]
    if "Tone" in data:
        out["tone"] = data["Tone"]
    if "CustomInstructions" in data:
        out["custom_instructions"] = data["CustomInstructions"]
    if "promptSummary" in data:
        out["prompt_summary"] = data["promptSummary"]
    return out
