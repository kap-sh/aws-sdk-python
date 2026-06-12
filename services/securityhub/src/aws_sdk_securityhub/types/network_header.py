"""Generated from Smithy shape ``com.amazonaws.securityhub#NetworkHeader``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.network_path_component_details
    import aws_sdk_securityhub.types.non_empty_string


class NetworkHeader(TypedDict):
    protocol: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The protocol used for the component.</p> <p>Length Constraints: Minimum of 1. Maximum of 16.</p>"""
    destination: NotRequired[
        "aws_sdk_securityhub.types.network_path_component_details.NetworkPathComponentDetails"
    ]
    """<p>Information about the destination of the component.</p>"""
    source: NotRequired[
        "aws_sdk_securityhub.types.network_path_component_details.NetworkPathComponentDetails"
    ]
    """<p>Information about the origin of the component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkHeader) -> dict:
    out: dict = {}
    if "protocol" in value:
        out["Protocol"] = value["protocol"]
    if "destination" in value:
        import aws_sdk_securityhub.types.network_path_component_details

        out["Destination"] = (
            aws_sdk_securityhub.types.network_path_component_details.serialize_json(
                value["destination"]
            )
        )
    if "source" in value:
        import aws_sdk_securityhub.types.network_path_component_details

        out["Source"] = (
            aws_sdk_securityhub.types.network_path_component_details.serialize_json(
                value["source"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkHeader:
    out: NetworkHeader = {}  # type: ignore[typeddict-item]
    if "Protocol" in data:
        out["protocol"] = data["Protocol"]
    if "Destination" in data:
        import aws_sdk_securityhub.types.network_path_component_details

        out["destination"] = (
            aws_sdk_securityhub.types.network_path_component_details.deserialize_json(
                data["Destination"]
            )
        )
    if "Source" in data:
        import aws_sdk_securityhub.types.network_path_component_details

        out["source"] = (
            aws_sdk_securityhub.types.network_path_component_details.deserialize_json(
                data["Source"]
            )
        )
    return out
