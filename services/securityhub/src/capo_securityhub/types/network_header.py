"""Generated from Smithy shape ``com.amazonaws.securityhub#NetworkHeader``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.network_path_component_details
    import capo_securityhub.types.non_empty_string


class NetworkHeader(TypedDict, closed=True):
    protocol: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The protocol used for the component.</p> <p>Length Constraints: Minimum of 1. Maximum of 16.</p>"""
    destination: NotRequired[
        "capo_securityhub.types.network_path_component_details.NetworkPathComponentDetails"
    ]
    """<p>Information about the destination of the component.</p>"""
    source: NotRequired[
        "capo_securityhub.types.network_path_component_details.NetworkPathComponentDetails"
    ]
    """<p>Information about the origin of the component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkHeader) -> dict:
    out: dict = {}
    if "protocol" in value:
        out["Protocol"] = value["protocol"]
    if "destination" in value:
        import capo_securityhub.types.network_path_component_details

        out["Destination"] = (
            capo_securityhub.types.network_path_component_details.serialize_json(
                value["destination"]
            )
        )
    if "source" in value:
        import capo_securityhub.types.network_path_component_details

        out["Source"] = (
            capo_securityhub.types.network_path_component_details.serialize_json(
                value["source"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkHeader:
    out: NetworkHeader = {}  # type: ignore[typeddict-item]
    if "Protocol" in data:
        out["protocol"] = data["Protocol"]
    if "Destination" in data:
        import capo_securityhub.types.network_path_component_details

        out["destination"] = (
            capo_securityhub.types.network_path_component_details.deserialize_json(
                data["Destination"]
            )
        )
    if "Source" in data:
        import capo_securityhub.types.network_path_component_details

        out["source"] = (
            capo_securityhub.types.network_path_component_details.deserialize_json(
                data["Source"]
            )
        )
    return out
