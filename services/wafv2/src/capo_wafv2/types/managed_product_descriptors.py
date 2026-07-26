"""Generated from Smithy shape ``com.amazonaws.wafv2#ManagedProductDescriptors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.managed_product_descriptor

ManagedProductDescriptors: TypeAlias = list[
    "capo_wafv2.types.managed_product_descriptor.ManagedProductDescriptor"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedProductDescriptors) -> list:
    import capo_wafv2.types.managed_product_descriptor

    out: list = []
    for item in value:
        out.append(
            capo_wafv2.types.managed_product_descriptor.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ManagedProductDescriptors:
    import capo_wafv2.types.managed_product_descriptor

    out: ManagedProductDescriptors = []
    for item in data:
        out.append(
            capo_wafv2.types.managed_product_descriptor.deserialize_aws_json_1_1(item)
        )
    return out
