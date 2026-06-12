"""Generated from Smithy shape ``com.amazonaws.pricing#PriceList``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pricing.types.currency_code
    import aws_sdk_pricing.types.file_formats
    import aws_sdk_pricing.types.price_list_arn
    import aws_sdk_pricing.types.region_code


class PriceList(TypedDict):
    price_list_arn: NotRequired["aws_sdk_pricing.types.price_list_arn.PriceListArn"]
    """<p>The unique identifier that maps to where your Price List files are located. <code>PriceListArn</code> can be obtained from the <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists.html\"> <code>ListPriceList</code> </a> response. </p>"""
    region_code: NotRequired["aws_sdk_pricing.types.region_code.RegionCode"]
    """<p>This is used to filter the Price List by Amazon Web Services Region. For example, to get the price list only for the <code>US East (N. Virginia)</code> Region, use <code>us-east-1</code>. If nothing is specified, you retrieve price lists for all applicable Regions. The available <code>RegionCode</code> list can be retrieved from <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetAttributeValues.html\"> <code>GetAttributeValues</code> </a> API. </p>"""
    currency_code: NotRequired["aws_sdk_pricing.types.currency_code.CurrencyCode"]
    """<p>The three alphabetical character ISO-4217 currency code the Price List files are denominated in. </p>"""
    file_formats: NotRequired["aws_sdk_pricing.types.file_formats.FileFormats"]
    """<p>The format you want to retrieve your Price List files. The <code>FileFormat</code> can be obtained from the <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists.html\"> <code>ListPriceList</code> </a> response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PriceList) -> dict:
    out: dict = {}
    if "price_list_arn" in value:
        out["PriceListArn"] = value["price_list_arn"]
    if "region_code" in value:
        out["RegionCode"] = value["region_code"]
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
    if "file_formats" in value:
        import aws_sdk_pricing.types.file_formats

        out["FileFormats"] = aws_sdk_pricing.types.file_formats.serialize_aws_json_1_1(
            value["file_formats"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PriceList:
    out: PriceList = {}  # type: ignore[typeddict-item]
    if "PriceListArn" in data:
        out["price_list_arn"] = data["PriceListArn"]
    if "RegionCode" in data:
        out["region_code"] = data["RegionCode"]
    if "CurrencyCode" in data:
        out["currency_code"] = data["CurrencyCode"]
    if "FileFormats" in data:
        import aws_sdk_pricing.types.file_formats

        out["file_formats"] = (
            aws_sdk_pricing.types.file_formats.deserialize_aws_json_1_1(
                data["FileFormats"]
            )
        )
    return out
