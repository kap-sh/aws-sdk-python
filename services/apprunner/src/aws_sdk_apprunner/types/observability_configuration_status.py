"""Generated from Smithy shape ``com.amazonaws.apprunner#ObservabilityConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

ObservabilityConfigurationStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ObservabilityConfigurationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ObservabilityConfigurationStatus:
    return cast(ObservabilityConfigurationStatus, data)
