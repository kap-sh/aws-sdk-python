"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SalesActivities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.sales_activity

SalesActivities: TypeAlias = list[
    "capo_partnercentral_selling.types.sales_activity.SalesActivity"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SalesActivities) -> list:
    import capo_partnercentral_selling.types.sales_activity

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_selling.types.sales_activity.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SalesActivities:
    import capo_partnercentral_selling.types.sales_activity

    out: SalesActivities = []
    for item in data:
        out.append(
            capo_partnercentral_selling.types.sales_activity.deserialize_aws_json_1_0(
                item
            )
        )
    return out
