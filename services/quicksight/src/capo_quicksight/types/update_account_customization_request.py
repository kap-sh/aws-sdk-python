"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAccountCustomizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.account_customization
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.namespace


class UpdateAccountCustomizationRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that you want to update Quick Sight customizations for.</p>"""
    namespace: NotRequired["capo_quicksight.types.namespace.Namespace"]
    """<p>The namespace that you want to update Quick Sight customizations for.</p>"""
    account_customization: (
        "capo_quicksight.types.account_customization.AccountCustomization"
    )
    """<p>The Quick Sight customizations you're updating. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountCustomizationRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.account_customization

    out["AccountCustomization"] = (
        capo_quicksight.types.account_customization.serialize_json(
            value["account_customization"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAccountCustomizationRequest:
    out: UpdateAccountCustomizationRequest = {}  # type: ignore[typeddict-item]
    if "AccountCustomization" in data:
        import capo_quicksight.types.account_customization

        out["account_customization"] = (
            capo_quicksight.types.account_customization.deserialize_json(
                data["AccountCustomization"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAccountCustomizationRequest.account_customization required"
        )
    return out
