"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormConceptList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehendmedical.types.rx_norm_concept

RxNormConceptList: TypeAlias = list[
    "capo_comprehendmedical.types.rx_norm_concept.RxNormConcept"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RxNormConceptList) -> list:
    import capo_comprehendmedical.types.rx_norm_concept

    out: list = []
    for item in value:
        out.append(
            capo_comprehendmedical.types.rx_norm_concept.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RxNormConceptList:
    import capo_comprehendmedical.types.rx_norm_concept

    out: RxNormConceptList = []
    for item in data:
        out.append(
            capo_comprehendmedical.types.rx_norm_concept.deserialize_aws_json_1_1(item)
        )
    return out
