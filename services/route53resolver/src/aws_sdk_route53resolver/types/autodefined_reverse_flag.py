"""Generated from Smithy shape ``com.amazonaws.route53resolver#AutodefinedReverseFlag``."""

from typing import Literal, TypeAlias, cast

AutodefinedReverseFlag: TypeAlias = Literal[
    "ENABLE",
    "DISABLE",
    "USE_LOCAL_RESOURCE_SETTING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutodefinedReverseFlag) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutodefinedReverseFlag:
    return cast(AutodefinedReverseFlag, data)
