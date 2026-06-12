"""Generated from Smithy shape ``com.amazonaws.iot#TlsConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.security_policy


class TlsConfig(TypedDict):
    security_policy: NotRequired["aws_sdk_iot.types.security_policy.SecurityPolicy"]
    """<p>The security policy for a domain configuration. For more information, see <a href=\"https://docs.aws.amazon.com/iot/latest/developerguide/transport-security.html#tls-policy-table\">Security policies </a> in the <i>Amazon Web Services IoT Core developer guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TlsConfig) -> dict:
    out: dict = {}
    if "security_policy" in value:
        out["securityPolicy"] = value["security_policy"]
    return out


def deserialize_json(data: dict) -> TlsConfig:
    out: TlsConfig = {}  # type: ignore[typeddict-item]
    if "securityPolicy" in data:
        out["security_policy"] = data["securityPolicy"]
    return out
