"""Generated from Smithy shape ``com.amazonaws.kendra#AdditionalResultAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.additional_result_attribute

AdditionalResultAttributeList: TypeAlias = list[
    "aws_sdk_kendra.types.additional_result_attribute.AdditionalResultAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalResultAttributeList) -> list:
    import aws_sdk_kendra.types.additional_result_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.additional_result_attribute.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AdditionalResultAttributeList:
    import aws_sdk_kendra.types.additional_result_attribute

    out: AdditionalResultAttributeList = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.additional_result_attribute.deserialize_aws_json_1_1(
                item
            )
        )
    return out
