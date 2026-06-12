"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductPlans``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.provisioned_product_plan_summary

ProvisionedProductPlans: TypeAlias = list[
    "aws_sdk_service_catalog.types.provisioned_product_plan_summary.ProvisionedProductPlanSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionedProductPlans) -> list:
    import aws_sdk_service_catalog.types.provisioned_product_plan_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.provisioned_product_plan_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProvisionedProductPlans:
    import aws_sdk_service_catalog.types.provisioned_product_plan_summary

    out: ProvisionedProductPlans = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.provisioned_product_plan_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
