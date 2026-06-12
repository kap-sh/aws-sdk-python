"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.rx_norm_attribute

RxNormAttributeList: TypeAlias = list[
    "aws_sdk_comprehendmedical.types.rx_norm_attribute.RxNormAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RxNormAttributeList) -> list:
    import aws_sdk_comprehendmedical.types.rx_norm_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehendmedical.types.rx_norm_attribute.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RxNormAttributeList:
    import aws_sdk_comprehendmedical.types.rx_norm_attribute

    out: RxNormAttributeList = []
    for item in data:
        out.append(
            aws_sdk_comprehendmedical.types.rx_norm_attribute.deserialize_aws_json_1_1(
                item
            )
        )
    return out
