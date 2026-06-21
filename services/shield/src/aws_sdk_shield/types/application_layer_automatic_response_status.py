"""Generated from Smithy shape ``com.amazonaws.shield#ApplicationLayerAutomaticResponseStatus``."""

from typing import Literal, TypeAlias, cast

ApplicationLayerAutomaticResponseStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationLayerAutomaticResponseStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationLayerAutomaticResponseStatus:
    return cast(ApplicationLayerAutomaticResponseStatus, data)
