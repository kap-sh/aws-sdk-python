"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Charges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.charge

Charges: TypeAlias = list["capo_marketplace_agreement.types.charge.Charge"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Charges) -> list:
    import capo_marketplace_agreement.types.charge

    out: list = []
    for item in value:
        out.append(capo_marketplace_agreement.types.charge.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Charges:
    import capo_marketplace_agreement.types.charge

    out: Charges = []
    for item in data:
        out.append(
            capo_marketplace_agreement.types.charge.deserialize_aws_json_1_0(item)
        )
    return out
