"""Generated from Smithy shape ``com.amazonaws.kendra#AdditionalResultAttributeValueType``."""

from typing import Literal, TypeAlias, cast

AdditionalResultAttributeValueType: TypeAlias = Literal["TEXT_WITH_HIGHLIGHTS_VALUE",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalResultAttributeValueType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdditionalResultAttributeValueType:
    return cast(AdditionalResultAttributeValueType, data)
