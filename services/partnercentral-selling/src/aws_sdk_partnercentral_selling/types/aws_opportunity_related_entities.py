"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsOpportunityRelatedEntities``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_product_identifiers
    import aws_sdk_partnercentral_selling.types.solution_identifiers


class AwsOpportunityRelatedEntities(TypedDict):
    aws_products: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_product_identifiers.AwsProductIdentifiers"
    ]
    """<p>Specifies the AWS products associated with the opportunity. This field helps track the specific products that are part of the proposed solution.</p>"""
    solutions: NotRequired[
        "aws_sdk_partnercentral_selling.types.solution_identifiers.SolutionIdentifiers"
    ]
    """<p>Specifies the partner solutions related to the opportunity. These solutions represent the partner's offerings that are being positioned as part of the overall AWS opportunity.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsOpportunityRelatedEntities) -> dict:
    out: dict = {}
    if "aws_products" in value:
        import aws_sdk_partnercentral_selling.types.aws_product_identifiers

        out["AwsProducts"] = (
            aws_sdk_partnercentral_selling.types.aws_product_identifiers.serialize_aws_json_1_0(
                value["aws_products"]
            )
        )
    if "solutions" in value:
        import aws_sdk_partnercentral_selling.types.solution_identifiers

        out["Solutions"] = (
            aws_sdk_partnercentral_selling.types.solution_identifiers.serialize_aws_json_1_0(
                value["solutions"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsOpportunityRelatedEntities:
    out: AwsOpportunityRelatedEntities = {}  # type: ignore[typeddict-item]
    if "AwsProducts" in data:
        import aws_sdk_partnercentral_selling.types.aws_product_identifiers

        out["aws_products"] = (
            aws_sdk_partnercentral_selling.types.aws_product_identifiers.deserialize_aws_json_1_0(
                data["AwsProducts"]
            )
        )
    if "Solutions" in data:
        import aws_sdk_partnercentral_selling.types.solution_identifiers

        out["solutions"] = (
            aws_sdk_partnercentral_selling.types.solution_identifiers.deserialize_aws_json_1_0(
                data["Solutions"]
            )
        )
    return out
