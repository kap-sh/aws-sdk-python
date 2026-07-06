"""Generated from Smithy shape ``com.amazonaws.securityhub#Product``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.category_list
    import aws_sdk_securityhub.types.integration_type_list
    import aws_sdk_securityhub.types.non_empty_string


class Product(TypedDict, closed=True):
    product_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN assigned to the product.</p>"""
    product_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the product.</p>"""
    company_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the company that provides the product.</p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A description of the product.</p>"""
    categories: NotRequired["aws_sdk_securityhub.types.category_list.CategoryList"]
    """<p>The categories assigned to the product.</p>"""
    integration_types: NotRequired[
        "aws_sdk_securityhub.types.integration_type_list.IntegrationTypeList"
    ]
    """<p>The types of integration that the product supports. Available values are the following.</p> <ul> <li> <p> <code>SEND_FINDINGS_TO_SECURITY_HUB</code> - The integration sends findings to Security Hub CSPM.</p> </li> <li> <p> <code>RECEIVE_FINDINGS_FROM_SECURITY_HUB</code> - The integration receives findings from Security Hub CSPM.</p> </li> <li> <p> <code>UPDATE_FINDINGS_IN_SECURITY_HUB</code> - The integration does not send new findings to Security Hub CSPM, but does make updates to the findings that it receives from Security Hub CSPM.</p> </li> </ul>"""
    marketplace_url: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>For integrations with Amazon Web Services services, the Amazon Web Services Console URL from which to activate the service.</p> <p>For integrations with third-party products, the Amazon Web Services Marketplace URL from which to subscribe to or purchase the product.</p>"""
    activation_url: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The URL to the service or product documentation about the integration with Security Hub CSPM, including how to activate the integration.</p>"""
    product_subscription_resource_policy: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The resource policy associated with the product.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Product) -> dict:
    out: dict = {}
    if "product_arn" in value:
        out["ProductArn"] = value["product_arn"]
    if "product_name" in value:
        out["ProductName"] = value["product_name"]
    if "company_name" in value:
        out["CompanyName"] = value["company_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "categories" in value:
        import aws_sdk_securityhub.types.category_list

        out["Categories"] = aws_sdk_securityhub.types.category_list.serialize_json(
            value["categories"]
        )
    if "integration_types" in value:
        import aws_sdk_securityhub.types.integration_type_list

        out["IntegrationTypes"] = (
            aws_sdk_securityhub.types.integration_type_list.serialize_json(
                value["integration_types"]
            )
        )
    if "marketplace_url" in value:
        out["MarketplaceUrl"] = value["marketplace_url"]
    if "activation_url" in value:
        out["ActivationUrl"] = value["activation_url"]
    if "product_subscription_resource_policy" in value:
        out["ProductSubscriptionResourcePolicy"] = value[
            "product_subscription_resource_policy"
        ]
    return out


def deserialize_json(data: dict) -> Product:
    out: Product = {}  # type: ignore[typeddict-item]
    if "ProductArn" in data:
        out["product_arn"] = data["ProductArn"]
    if "ProductName" in data:
        out["product_name"] = data["ProductName"]
    if "CompanyName" in data:
        out["company_name"] = data["CompanyName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Categories" in data:
        import aws_sdk_securityhub.types.category_list

        out["categories"] = aws_sdk_securityhub.types.category_list.deserialize_json(
            data["Categories"]
        )
    if "IntegrationTypes" in data:
        import aws_sdk_securityhub.types.integration_type_list

        out["integration_types"] = (
            aws_sdk_securityhub.types.integration_type_list.deserialize_json(
                data["IntegrationTypes"]
            )
        )
    if "MarketplaceUrl" in data:
        out["marketplace_url"] = data["MarketplaceUrl"]
    if "ActivationUrl" in data:
        out["activation_url"] = data["ActivationUrl"]
    if "ProductSubscriptionResourcePolicy" in data:
        out["product_subscription_resource_policy"] = data[
            "ProductSubscriptionResourcePolicy"
        ]
    return out
