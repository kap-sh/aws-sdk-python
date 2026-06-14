"""Generated from Smithy shape ``com.amazonaws.appintegrations#ApplicationApprovedOrigins``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.application_trusted_source

ApplicationApprovedOrigins: TypeAlias = list["aws_sdk_appintegrations.types.application_trusted_source.ApplicationTrustedSource"]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationApprovedOrigins) -> list:
    return list(value)


def deserialize_json(data: list) -> ApplicationApprovedOrigins:
    return list(data)