"""Generated from Smithy shape ``com.amazonaws.emr#SupportedProductsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.xml_string_max_len256

SupportedProductsList: TypeAlias = list[
    "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportedProductsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SupportedProductsList:
    return list(data)
