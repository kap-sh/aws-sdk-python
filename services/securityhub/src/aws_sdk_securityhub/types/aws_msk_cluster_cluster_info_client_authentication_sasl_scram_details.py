"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsMskClusterClusterInfoClientAuthenticationSaslScramDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean


class AwsMskClusterClusterInfoClientAuthenticationSaslScramDetails(TypedDict):
    enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether SASL/SCRAM authentication is enabled or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsMskClusterClusterInfoClientAuthenticationSaslScramDetails,
) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(
    data: dict,
) -> AwsMskClusterClusterInfoClientAuthenticationSaslScramDetails:
    out: AwsMskClusterClusterInfoClientAuthenticationSaslScramDetails = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
