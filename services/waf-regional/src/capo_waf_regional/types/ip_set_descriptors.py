"""Generated from Smithy shape ``com.amazonaws.wafregional#IPSetDescriptors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf_regional.types.ip_set_descriptor

IPSetDescriptors: TypeAlias = list[
    "capo_waf_regional.types.ip_set_descriptor.IPSetDescriptor"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IPSetDescriptors) -> list:
    import capo_waf_regional.types.ip_set_descriptor

    out: list = []
    for item in value:
        out.append(
            capo_waf_regional.types.ip_set_descriptor.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IPSetDescriptors:
    import capo_waf_regional.types.ip_set_descriptor

    out: IPSetDescriptors = []
    for item in data:
        out.append(
            capo_waf_regional.types.ip_set_descriptor.deserialize_aws_json_1_1(item)
        )
    return out
