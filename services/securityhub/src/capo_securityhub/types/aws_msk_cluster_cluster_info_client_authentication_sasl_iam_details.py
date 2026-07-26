"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsMskClusterClusterInfoClientAuthenticationSaslIamDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean


class AwsMskClusterClusterInfoClientAuthenticationSaslIamDetails(
    TypedDict, closed=True
):
    enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether SASL/IAM authentication is enabled or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsMskClusterClusterInfoClientAuthenticationSaslIamDetails,
) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(
    data: dict,
) -> AwsMskClusterClusterInfoClientAuthenticationSaslIamDetails:
    out: AwsMskClusterClusterInfoClientAuthenticationSaslIamDetails = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
