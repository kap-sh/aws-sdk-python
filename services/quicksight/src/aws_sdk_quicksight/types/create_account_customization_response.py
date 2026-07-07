"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateAccountCustomizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.account_customization
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.namespace
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class CreateAccountCustomizationResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the customization that you created for this Amazon Web Services account.</p>"""
    aws_account_id: NotRequired["aws_sdk_quicksight.types.aws_account_id.AwsAccountId"]
    """<p>The ID for the Amazon Web Services account that you want to customize Quick Sight for.</p>"""
    namespace: NotRequired["aws_sdk_quicksight.types.namespace.Namespace"]
    """<p>The namespace associated with the customization you're creating. </p>"""
    account_customization: NotRequired[
        "aws_sdk_quicksight.types.account_customization.AccountCustomization"
    ]
    """<p>The Quick Sight customizations you're adding. </p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccountCustomizationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "aws_account_id" in value:
        out["AwsAccountId"] = value["aws_account_id"]
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "account_customization" in value:
        import aws_sdk_quicksight.types.account_customization

        out["AccountCustomization"] = (
            aws_sdk_quicksight.types.account_customization.serialize_json(
                value["account_customization"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateAccountCustomizationResponse:
    out: CreateAccountCustomizationResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AwsAccountId" in data:
        out["aws_account_id"] = data["AwsAccountId"]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    if "AccountCustomization" in data:
        import aws_sdk_quicksight.types.account_customization

        out["account_customization"] = (
            aws_sdk_quicksight.types.account_customization.deserialize_json(
                data["AccountCustomization"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
