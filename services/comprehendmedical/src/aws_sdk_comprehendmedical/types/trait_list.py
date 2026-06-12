"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#TraitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.trait

TraitList: TypeAlias = list["aws_sdk_comprehendmedical.types.trait.Trait"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TraitList) -> list:
    import aws_sdk_comprehendmedical.types.trait

    out: list = []
    for item in value:
        out.append(aws_sdk_comprehendmedical.types.trait.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TraitList:
    import aws_sdk_comprehendmedical.types.trait

    out: TraitList = []
    for item in data:
        out.append(aws_sdk_comprehendmedical.types.trait.deserialize_aws_json_1_1(item))
    return out
