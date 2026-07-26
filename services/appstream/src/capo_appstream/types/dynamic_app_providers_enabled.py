"""Generated from Smithy shape ``com.amazonaws.appstream#DynamicAppProvidersEnabled``."""

from typing import Literal, TypeAlias, cast

DynamicAppProvidersEnabled: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DynamicAppProvidersEnabled) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DynamicAppProvidersEnabled:
    return cast(DynamicAppProvidersEnabled, data)
