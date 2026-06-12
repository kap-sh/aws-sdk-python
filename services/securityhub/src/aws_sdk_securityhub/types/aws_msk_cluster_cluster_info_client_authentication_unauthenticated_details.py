"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean


class AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetails(TypedDict):
    enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether unauthenticated is allowed or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetails,
) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(
    data: dict,
) -> AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetails:
    out: AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetails = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
