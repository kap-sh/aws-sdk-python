"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean


class AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetails(
    TypedDict, closed=True
):
    enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
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
