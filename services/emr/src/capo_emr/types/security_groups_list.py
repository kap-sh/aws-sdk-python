"""Generated from Smithy shape ``com.amazonaws.emr#SecurityGroupsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.xml_string_max_len256

SecurityGroupsList: TypeAlias = list[
    "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroupsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SecurityGroupsList:
    return list(data)
