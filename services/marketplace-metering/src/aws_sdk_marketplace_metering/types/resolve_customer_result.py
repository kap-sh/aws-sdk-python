"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#ResolveCustomerResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_metering.types.customer_aws_account_id
    import aws_sdk_marketplace_metering.types.customer_identifier
    import aws_sdk_marketplace_metering.types.license_arn
    import aws_sdk_marketplace_metering.types.product_code


class ResolveCustomerResult(TypedDict):
    customer_identifier: NotRequired[
        "aws_sdk_marketplace_metering.types.customer_identifier.CustomerIdentifier"
    ]
    """<p>The <code>CustomerIdentifier</code> is used to identify an individual customer in your application.</p>"""
    product_code: NotRequired[
        "aws_sdk_marketplace_metering.types.product_code.ProductCode"
    ]
    """<p>The product code is returned to confirm that the buyer is registering for your product. Subsequent <code>BatchMeterUsage</code> calls should be made using this product code.</p>"""
    customer_aws_account_id: NotRequired[
        "aws_sdk_marketplace_metering.types.customer_aws_account_id.CustomerAWSAccountId"
    ]
    """<p>The <code>CustomerAWSAccountId</code> provides the Amazon Web Services account ID associated with the <code>CustomerIdentifier</code> for the individual customer. Calls to <code>BatchMeterUsage</code> require <code>CustomerAWSAccountId</code> for each <code>UsageRecord</code>.</p>"""
    license_arn: NotRequired[
        "aws_sdk_marketplace_metering.types.license_arn.LicenseArn"
    ]
    """<p>The <code>LicenseArn</code> is a unique identifier for a specific granted license. These are typically used for software purchased through Amazon Web Services Marketplace. Calls to <code>BatchMeterUsage</code> require <code>LicenseArn</code> for each <code>UsageRecord</code>.</p> <note> <p>Once you receive the <code>CustomerAWSAccountId</code> and <code>LicenseArn</code> in the response, store that for future purposes/API calls/integrations.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolveCustomerResult) -> dict:
    out: dict = {}
    if "customer_identifier" in value:
        out["CustomerIdentifier"] = value["customer_identifier"]
    if "product_code" in value:
        out["ProductCode"] = value["product_code"]
    if "customer_aws_account_id" in value:
        out["CustomerAWSAccountId"] = value["customer_aws_account_id"]
    if "license_arn" in value:
        out["LicenseArn"] = value["license_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolveCustomerResult:
    out: ResolveCustomerResult = {}  # type: ignore[typeddict-item]
    if "CustomerIdentifier" in data:
        out["customer_identifier"] = data["CustomerIdentifier"]
    if "ProductCode" in data:
        out["product_code"] = data["ProductCode"]
    if "CustomerAWSAccountId" in data:
        out["customer_aws_account_id"] = data["CustomerAWSAccountId"]
    if "LicenseArn" in data:
        out["license_arn"] = data["LicenseArn"]
    return out
