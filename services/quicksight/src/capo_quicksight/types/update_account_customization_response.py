"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAccountCustomizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.account_customization
    import capo_quicksight.types.arn
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.namespace
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class UpdateAccountCustomizationResponse(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the updated customization for this Amazon Web Services account.</p>"""
    aws_account_id: NotRequired["capo_quicksight.types.aws_account_id.AwsAccountId"]
    """<p>The ID for the Amazon Web Services account that you want to update Quick Sight customizations for.</p>"""
    namespace: NotRequired["capo_quicksight.types.namespace.Namespace"]
    """<p>The namespace associated with the customization that you're updating.</p>"""
    account_customization: NotRequired[
        "capo_quicksight.types.account_customization.AccountCustomization"
    ]
    """<p>The Quick Sight customizations you're updating. </p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountCustomizationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "aws_account_id" in value:
        out["AwsAccountId"] = value["aws_account_id"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "account_customization" in value:
        import capo_quicksight.types.account_customization

        out["AccountCustomization"] = (
            capo_quicksight.types.account_customization.serialize_json(
                value["account_customization"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateAccountCustomizationResponse:
    out: UpdateAccountCustomizationResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AwsAccountId" in data:
        out["aws_account_id"] = data["AwsAccountId"]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    if "AccountCustomization" in data:
        import capo_quicksight.types.account_customization

        out["account_customization"] = (
            capo_quicksight.types.account_customization.deserialize_json(
                data["AccountCustomization"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
