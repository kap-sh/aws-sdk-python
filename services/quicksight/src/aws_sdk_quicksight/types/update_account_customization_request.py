"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAccountCustomizationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.account_customization
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.namespace


class UpdateAccountCustomizationRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that you want to update Quick Sight customizations for.</p>"""
    namespace: NotRequired["aws_sdk_quicksight.types.namespace.Namespace"]
    """<p>The namespace that you want to update Quick Sight customizations for.</p>"""
    account_customization: (
        "aws_sdk_quicksight.types.account_customization.AccountCustomization"
    )
    """<p>The Quick Sight customizations you're updating. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountCustomizationRequest) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.account_customization

    out["AccountCustomization"] = (
        aws_sdk_quicksight.types.account_customization.serialize_json(
            value["account_customization"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAccountCustomizationRequest:
    out: UpdateAccountCustomizationRequest = {}  # type: ignore[typeddict-item]
    if "AccountCustomization" in data:
        import aws_sdk_quicksight.types.account_customization

        out["account_customization"] = (
            aws_sdk_quicksight.types.account_customization.deserialize_json(
                data["AccountCustomization"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAccountCustomizationRequest.account_customization required"
        )
    return out
