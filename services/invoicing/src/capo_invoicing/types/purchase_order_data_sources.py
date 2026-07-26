"""Generated from Smithy shape ``com.amazonaws.invoicing#PurchaseOrderDataSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_invoicing.types.purchase_order_data_source

PurchaseOrderDataSources: TypeAlias = list[
    "capo_invoicing.types.purchase_order_data_source.PurchaseOrderDataSource"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PurchaseOrderDataSources) -> list:
    import capo_invoicing.types.purchase_order_data_source

    out: list = []
    for item in value:
        out.append(
            capo_invoicing.types.purchase_order_data_source.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PurchaseOrderDataSources:
    import capo_invoicing.types.purchase_order_data_source

    out: PurchaseOrderDataSources = []
    for item in data:
        out.append(
            capo_invoicing.types.purchase_order_data_source.deserialize_aws_json_1_0(
                item
            )
        )
    return out
