"""Generated from Smithy shape ``com.amazonaws.emr#StepIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.xml_string_max_len256

StepIdsList: TypeAlias = list[
    "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepIdsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> StepIdsList:
    return list(data)
