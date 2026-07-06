"""Generated from Smithy shape ``com.amazonaws.securityhub#EnableImportFindingsForProductResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class EnableImportFindingsForProductResponse(TypedDict, closed=True):
    product_subscription_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of your subscription to the product to enable integrations for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableImportFindingsForProductResponse) -> dict:
    out: dict = {}
    if "product_subscription_arn" in value:
        out["ProductSubscriptionArn"] = value["product_subscription_arn"]
    return out


def deserialize_json(data: dict) -> EnableImportFindingsForProductResponse:
    out: EnableImportFindingsForProductResponse = {}  # type: ignore[typeddict-item]
    if "ProductSubscriptionArn" in data:
        out["product_subscription_arn"] = data["ProductSubscriptionArn"]
    return out
