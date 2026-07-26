"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#DeliveryModels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.delivery_model

DeliveryModels: TypeAlias = list[
    "capo_partnercentral_selling.types.delivery_model.DeliveryModel"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeliveryModels) -> list:
    import capo_partnercentral_selling.types.delivery_model

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.delivery_model.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DeliveryModels:
    import capo_partnercentral_selling.types.delivery_model

    out: DeliveryModels = []
    for item in data:
        out.append(
            capo_partnercentral_selling.types.delivery_model.deserialize_aws_json_1_0(
                item
            )
        )
    return out
