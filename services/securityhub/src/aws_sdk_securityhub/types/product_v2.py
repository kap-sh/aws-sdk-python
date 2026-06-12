"""Generated from Smithy shape ``com.amazonaws.securityhub#ProductV2``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.category_list
    import aws_sdk_securityhub.types.integration_v2_type_list
    import aws_sdk_securityhub.types.non_empty_string


class ProductV2(TypedDict):
    product_v2_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the productV2.</p>"""
    company_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the organization or vendor that provides the productV2.</p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Detailed information about the productV2.</p>"""
    categories: NotRequired["aws_sdk_securityhub.types.category_list.CategoryList"]
    """<p>The domains or functional areas the productV2 addresses.</p>"""
    integration_v2_types: NotRequired[
        "aws_sdk_securityhub.types.integration_v2_type_list.IntegrationV2TypeList"
    ]
    """<p>The type of integration.</p>"""
    marketplace_url: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The console URL where you can purchase or subscribe to products.</p>"""
    activation_url: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The URL to the serviceV@ or productV2 documentation about the integration, which includes how to activate the integration.</p>"""
    marketplace_product_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier for the Amazon Web Services Marketplace product associated with this integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProductV2) -> dict:
    out: dict = {}
    if "product_v2_name" in value:
        out["ProductV2Name"] = value["product_v2_name"]
    if "company_name" in value:
        out["CompanyName"] = value["company_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "categories" in value:
        import aws_sdk_securityhub.types.category_list

        out["Categories"] = aws_sdk_securityhub.types.category_list.serialize_json(
            value["categories"]
        )
    if "integration_v2_types" in value:
        import aws_sdk_securityhub.types.integration_v2_type_list

        out["IntegrationV2Types"] = (
            aws_sdk_securityhub.types.integration_v2_type_list.serialize_json(
                value["integration_v2_types"]
            )
        )
    if "marketplace_url" in value:
        out["MarketplaceUrl"] = value["marketplace_url"]
    if "activation_url" in value:
        out["ActivationUrl"] = value["activation_url"]
    if "marketplace_product_id" in value:
        out["MarketplaceProductId"] = value["marketplace_product_id"]
    return out


def deserialize_json(data: dict) -> ProductV2:
    out: ProductV2 = {}  # type: ignore[typeddict-item]
    if "ProductV2Name" in data:
        out["product_v2_name"] = data["ProductV2Name"]
    if "CompanyName" in data:
        out["company_name"] = data["CompanyName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Categories" in data:
        import aws_sdk_securityhub.types.category_list

        out["categories"] = aws_sdk_securityhub.types.category_list.deserialize_json(
            data["Categories"]
        )
    if "IntegrationV2Types" in data:
        import aws_sdk_securityhub.types.integration_v2_type_list

        out["integration_v2_types"] = (
            aws_sdk_securityhub.types.integration_v2_type_list.deserialize_json(
                data["IntegrationV2Types"]
            )
        )
    if "MarketplaceUrl" in data:
        out["marketplace_url"] = data["MarketplaceUrl"]
    if "ActivationUrl" in data:
        out["activation_url"] = data["ActivationUrl"]
    if "MarketplaceProductId" in data:
        out["marketplace_product_id"] = data["MarketplaceProductId"]
    return out
