"""Generated from Smithy shape ``com.amazonaws.grafana#SamlAuthentication``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_grafana.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_grafana.types.saml_configuration
    import aws_sdk_grafana.types.saml_configuration_status

class SamlAuthentication(TypedDict):
    status: "aws_sdk_grafana.types.saml_configuration_status.SamlConfigurationStatus"
    """<p>Specifies whether the workspace's SAML configuration is complete.</p>"""
    configuration: NotRequired["aws_sdk_grafana.types.saml_configuration.SamlConfiguration"]
    """<p>A structure containing details about how this workspace works with SAML. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: SamlAuthentication) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    if "configuration" in value:
        import aws_sdk_grafana.types.saml_configuration
        out["configuration"] = aws_sdk_grafana.types.saml_configuration.serialize_json(value["configuration"])
    return out


def deserialize_json(data: dict) -> SamlAuthentication:
    out: SamlAuthentication = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("SamlAuthentication.status required")
    if "configuration" in data:
        import aws_sdk_grafana.types.saml_configuration
        out["configuration"] = aws_sdk_grafana.types.saml_configuration.deserialize_json(data["configuration"])
    return out