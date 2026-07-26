"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#FulfillmentTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.fulfillment_type

FulfillmentTypes: TypeAlias = list[
    "capo_partnercentral_benefits.types.fulfillment_type.FulfillmentType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FulfillmentTypes) -> list:
    import capo_partnercentral_benefits.types.fulfillment_type

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_benefits.types.fulfillment_type.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FulfillmentTypes:
    import capo_partnercentral_benefits.types.fulfillment_type

    out: FulfillmentTypes = []
    for item in data:
        out.append(
            capo_partnercentral_benefits.types.fulfillment_type.deserialize_aws_json_1_0(
                item
            )
        )
    return out
