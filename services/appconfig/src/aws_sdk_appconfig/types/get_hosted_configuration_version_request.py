"""Generated from Smithy shape ``com.amazonaws.appconfig#GetHostedConfigurationVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.integer


class GetHostedConfigurationVersionRequest(TypedDict, closed=True):
    application_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The application ID.</p>"""
    configuration_profile_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The configuration profile ID.</p>"""
    version_number: "aws_sdk_appconfig.types.integer.Integer"
    """<p>The version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetHostedConfigurationVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetHostedConfigurationVersionRequest:
    out: GetHostedConfigurationVersionRequest = {}  # type: ignore[typeddict-item]
    return out
