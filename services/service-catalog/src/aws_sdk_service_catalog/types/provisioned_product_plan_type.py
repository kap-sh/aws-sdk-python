"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductPlanType``."""

from typing import Literal, TypeAlias, cast

ProvisionedProductPlanType: TypeAlias = Literal["CLOUDFORMATION",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionedProductPlanType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProvisionedProductPlanType:
    return cast(ProvisionedProductPlanType, data)
