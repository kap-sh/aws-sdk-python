"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehendmedical.types.snomedct_attribute

SNOMEDCTAttributeList: TypeAlias = list[
    "capo_comprehendmedical.types.snomedct_attribute.SNOMEDCTAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SNOMEDCTAttributeList) -> list:
    import capo_comprehendmedical.types.snomedct_attribute

    out: list = []
    for item in value:
        out.append(
            capo_comprehendmedical.types.snomedct_attribute.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SNOMEDCTAttributeList:
    import capo_comprehendmedical.types.snomedct_attribute

    out: SNOMEDCTAttributeList = []
    for item in data:
        out.append(
            capo_comprehendmedical.types.snomedct_attribute.deserialize_aws_json_1_1(
                item
            )
        )
    return out
