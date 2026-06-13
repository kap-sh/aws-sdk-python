"""Generated from Smithy shape ``com.amazonaws.emr#EnvironmentVariablesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.xml_string
    import aws_sdk_emr.types.xml_string_max_len256

EnvironmentVariablesMap: TypeAlias = dict[
    "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256",
    "aws_sdk_emr.types.xml_string.XmlString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: EnvironmentVariablesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentVariablesMap:
    out: EnvironmentVariablesMap = {}
    for key, value in data.items():
        out[key] = value
    return out
