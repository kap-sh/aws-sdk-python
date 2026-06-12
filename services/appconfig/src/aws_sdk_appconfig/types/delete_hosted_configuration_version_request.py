"""Generated from Smithy shape ``com.amazonaws.appconfig#DeleteHostedConfigurationVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.integer


class DeleteHostedConfigurationVersionRequest(TypedDict):
    application_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The application ID.</p>"""
    configuration_profile_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The configuration profile ID.</p>"""
    version_number: "aws_sdk_appconfig.types.integer.Integer"
    """<p>The versions number to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteHostedConfigurationVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteHostedConfigurationVersionRequest:
    out: DeleteHostedConfigurationVersionRequest = {}  # type: ignore[typeddict-item]
    return out
