"""Generated from Smithy shape ``com.amazonaws.appconfig#ValidateConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.version


class ValidateConfigurationRequest(TypedDict):
    application_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The application ID.</p>"""
    configuration_profile_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The configuration profile ID.</p>"""
    configuration_version: "aws_sdk_appconfig.types.version.Version"
    """<p>The version of the configuration to validate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ValidateConfigurationRequest:
    out: ValidateConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
