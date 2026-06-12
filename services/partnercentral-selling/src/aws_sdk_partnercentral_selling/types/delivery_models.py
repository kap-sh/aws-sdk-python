"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#DeliveryModels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.delivery_model

DeliveryModels: TypeAlias = list[
    "aws_sdk_partnercentral_selling.types.delivery_model.DeliveryModel"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeliveryModels) -> list:
    import aws_sdk_partnercentral_selling.types.delivery_model

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_selling.types.delivery_model.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DeliveryModels:
    import aws_sdk_partnercentral_selling.types.delivery_model

    out: DeliveryModels = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_selling.types.delivery_model.deserialize_aws_json_1_0(
                item
            )
        )
    return out
