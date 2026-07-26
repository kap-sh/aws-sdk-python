"""Generated from Smithy shape ``com.amazonaws.appstream#ApplicationAttribute``."""

from typing import Literal, TypeAlias, cast

ApplicationAttribute: TypeAlias = Literal[
    "LAUNCH_PARAMETERS",
    "WORKING_DIRECTORY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApplicationAttribute:
    return cast(ApplicationAttribute, data)
