"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.snomedct_entity

SNOMEDCTEntityList: TypeAlias = list[
    "aws_sdk_comprehendmedical.types.snomedct_entity.SNOMEDCTEntity"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SNOMEDCTEntityList) -> list:
    import aws_sdk_comprehendmedical.types.snomedct_entity

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehendmedical.types.snomedct_entity.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SNOMEDCTEntityList:
    import aws_sdk_comprehendmedical.types.snomedct_entity

    out: SNOMEDCTEntityList = []
    for item in data:
        out.append(
            aws_sdk_comprehendmedical.types.snomedct_entity.deserialize_aws_json_1_1(
                item
            )
        )
    return out
