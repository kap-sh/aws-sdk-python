"""Generated from Smithy shape ``com.amazonaws.sagemaker#IdleResourceSharing``."""

from typing import Literal, TypeAlias, cast

IdleResourceSharing: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdleResourceSharing) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IdleResourceSharing:
    return cast(IdleResourceSharing, data)
