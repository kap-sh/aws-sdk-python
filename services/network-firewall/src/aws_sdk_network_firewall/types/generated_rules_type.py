"""Generated from Smithy shape ``com.amazonaws.networkfirewall#GeneratedRulesType``."""

from typing import Literal, TypeAlias, cast

GeneratedRulesType: TypeAlias = Literal[
    "ALLOWLIST",
    "DENYLIST",
    "REJECTLIST",
    "ALERTLIST",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GeneratedRulesType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> GeneratedRulesType:
    return cast(GeneratedRulesType, data)
