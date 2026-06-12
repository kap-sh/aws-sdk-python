"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTTraitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.snomedct_trait

SNOMEDCTTraitList: TypeAlias = list[
    "aws_sdk_comprehendmedical.types.snomedct_trait.SNOMEDCTTrait"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SNOMEDCTTraitList) -> list:
    import aws_sdk_comprehendmedical.types.snomedct_trait

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehendmedical.types.snomedct_trait.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SNOMEDCTTraitList:
    import aws_sdk_comprehendmedical.types.snomedct_trait

    out: SNOMEDCTTraitList = []
    for item in data:
        out.append(
            aws_sdk_comprehendmedical.types.snomedct_trait.deserialize_aws_json_1_1(
                item
            )
        )
    return out
