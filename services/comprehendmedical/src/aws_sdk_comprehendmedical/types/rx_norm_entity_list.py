"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.rx_norm_entity

RxNormEntityList: TypeAlias = list[
    "aws_sdk_comprehendmedical.types.rx_norm_entity.RxNormEntity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RxNormEntityList) -> list:
    import aws_sdk_comprehendmedical.types.rx_norm_entity

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehendmedical.types.rx_norm_entity.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RxNormEntityList:
    import aws_sdk_comprehendmedical.types.rx_norm_entity

    out: RxNormEntityList = []
    for item in data:
        out.append(
            aws_sdk_comprehendmedical.types.rx_norm_entity.deserialize_aws_json_1_1(
                item
            )
        )
    return out
