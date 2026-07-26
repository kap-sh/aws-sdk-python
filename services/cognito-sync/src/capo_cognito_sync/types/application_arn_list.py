"""Generated from Smithy shape ``com.amazonaws.cognitosync#ApplicationArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_sync.types.application_arn

ApplicationArnList: TypeAlias = list[
    "capo_cognito_sync.types.application_arn.ApplicationArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ApplicationArnList:
    return list(data)
