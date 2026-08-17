"""Generated from Smithy shape ``com.amazonaws.kms#MacAlgorithmSpecList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kms.types.mac_algorithm_spec

MacAlgorithmSpecList: TypeAlias = list[
    "capo_kms.types.mac_algorithm_spec.MacAlgorithmSpec"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MacAlgorithmSpecList) -> list:
    import capo_kms.types.mac_algorithm_spec

    out: list = []
    for item in value:
        out.append(capo_kms.types.mac_algorithm_spec.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MacAlgorithmSpecList:
    import capo_kms.types.mac_algorithm_spec

    out: MacAlgorithmSpecList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_kms.types.mac_algorithm_spec.deserialize_aws_json_1_1(item))
    return out
