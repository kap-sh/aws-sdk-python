"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehendmedical.types.rx_norm_attribute

RxNormAttributeList: TypeAlias = list[
    "capo_comprehendmedical.types.rx_norm_attribute.RxNormAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RxNormAttributeList) -> list:
    import capo_comprehendmedical.types.rx_norm_attribute

    out: list = []
    for item in value:
        out.append(
            capo_comprehendmedical.types.rx_norm_attribute.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RxNormAttributeList:
    import capo_comprehendmedical.types.rx_norm_attribute

    out: RxNormAttributeList = []
    for item in data:
        out.append(
            capo_comprehendmedical.types.rx_norm_attribute.deserialize_aws_json_1_1(
                item
            )
        )
    return out
