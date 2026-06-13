"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Charges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.charge

Charges: TypeAlias = list["aws_sdk_marketplace_agreement.types.charge.Charge"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Charges) -> list:
    import aws_sdk_marketplace_agreement.types.charge

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_agreement.types.charge.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> Charges:
    import aws_sdk_marketplace_agreement.types.charge

    out: Charges = []
    for item in data:
        out.append(
            aws_sdk_marketplace_agreement.types.charge.deserialize_aws_json_1_0(item)
        )
    return out
