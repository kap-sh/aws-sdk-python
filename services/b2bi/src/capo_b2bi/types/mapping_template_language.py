"""Generated from Smithy shape ``com.amazonaws.b2bi#MappingTemplateLanguage``."""

from typing import Literal, TypeAlias, cast

MappingTemplateLanguage: TypeAlias = Literal[
    "XSLT",
    "JSONATA",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MappingTemplateLanguage) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MappingTemplateLanguage:
    return cast(MappingTemplateLanguage, data)
