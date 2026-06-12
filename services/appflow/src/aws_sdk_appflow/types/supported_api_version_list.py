"""Generated from Smithy shape ``com.amazonaws.appflow#SupportedApiVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.supported_api_version

SupportedApiVersionList: TypeAlias = list[
    "aws_sdk_appflow.types.supported_api_version.SupportedApiVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: SupportedApiVersionList) -> list:
    return list(value)


def deserialize_json(data: list) -> SupportedApiVersionList:
    return list(data)
