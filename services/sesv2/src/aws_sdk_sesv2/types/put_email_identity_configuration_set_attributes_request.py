"""Generated from Smithy shape ``com.amazonaws.sesv2#PutEmailIdentityConfigurationSetAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.configuration_set_name
    import aws_sdk_sesv2.types.identity


class PutEmailIdentityConfigurationSetAttributesRequest(TypedDict, closed=True):
    email_identity: "aws_sdk_sesv2.types.identity.Identity"
    """<p>The email address or domain to associate with a configuration set.</p>"""
    configuration_set_name: NotRequired[
        "aws_sdk_sesv2.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The configuration set to associate with an email identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutEmailIdentityConfigurationSetAttributesRequest) -> dict:
    out: dict = {}
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    return out


def deserialize_json(data: dict) -> PutEmailIdentityConfigurationSetAttributesRequest:
    out: PutEmailIdentityConfigurationSetAttributesRequest = {}  # type: ignore[typeddict-item]
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    return out
