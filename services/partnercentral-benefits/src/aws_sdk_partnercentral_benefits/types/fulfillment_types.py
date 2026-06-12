"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#FulfillmentTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_benefits.types.fulfillment_type

FulfillmentTypes: TypeAlias = list[
    "aws_sdk_partnercentral_benefits.types.fulfillment_type.FulfillmentType"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FulfillmentTypes) -> list:
    import aws_sdk_partnercentral_benefits.types.fulfillment_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_benefits.types.fulfillment_type.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FulfillmentTypes:
    import aws_sdk_partnercentral_benefits.types.fulfillment_type

    out: FulfillmentTypes = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_benefits.types.fulfillment_type.deserialize_aws_json_1_0(
                item
            )
        )
    return out
