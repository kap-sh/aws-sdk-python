"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsProductsSpendInsightsBySource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_product_insights


class AwsProductsSpendInsightsBySource(TypedDict):
    partner: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_product_insights.AwsProductInsights"
    ]
    """<p>Partner-sourced insights derived from Pricing Calculator URLs.</p>"""
    aws: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_product_insights.AwsProductInsights"
    ]
    """<p>AI-generated insights including recommended products from AWS.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsProductsSpendInsightsBySource) -> dict:
    out: dict = {}
    if "partner" in value:
        import aws_sdk_partnercentral_selling.types.aws_product_insights

        out["Partner"] = (
            aws_sdk_partnercentral_selling.types.aws_product_insights.serialize_aws_json_1_0(
                value["partner"]
            )
        )
    if "aws" in value:
        import aws_sdk_partnercentral_selling.types.aws_product_insights

        out["AWS"] = (
            aws_sdk_partnercentral_selling.types.aws_product_insights.serialize_aws_json_1_0(
                value["aws"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsProductsSpendInsightsBySource:
    out: AwsProductsSpendInsightsBySource = {}  # type: ignore[typeddict-item]
    if "Partner" in data:
        import aws_sdk_partnercentral_selling.types.aws_product_insights

        out["partner"] = (
            aws_sdk_partnercentral_selling.types.aws_product_insights.deserialize_aws_json_1_0(
                data["Partner"]
            )
        )
    if "AWS" in data:
        import aws_sdk_partnercentral_selling.types.aws_product_insights

        out["aws"] = (
            aws_sdk_partnercentral_selling.types.aws_product_insights.deserialize_aws_json_1_0(
                data["AWS"]
            )
        )
    return out
