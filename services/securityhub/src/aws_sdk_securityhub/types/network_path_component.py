"""Generated from Smithy shape ``com.amazonaws.securityhub#NetworkPathComponent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.network_header
    import aws_sdk_securityhub.types.non_empty_string


class NetworkPathComponent(TypedDict, closed=True):
    component_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of a component in the network path.</p> <p>Length Constraints: Minimum of 1. Maximum of 32.</p>"""
    component_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The type of component.</p> <p>Length Constraints: Minimum of 1. Maximum of 32.</p>"""
    egress: NotRequired["aws_sdk_securityhub.types.network_header.NetworkHeader"]
    """<p>Information about the component that comes after the current component in the network path.</p>"""
    ingress: NotRequired["aws_sdk_securityhub.types.network_header.NetworkHeader"]
    """<p>Information about the component that comes before the current node in the network path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkPathComponent) -> dict:
    out: dict = {}
    if "component_id" in value:
        out["ComponentId"] = value["component_id"]
    if "component_type" in value:
        out["ComponentType"] = value["component_type"]
    if "egress" in value:
        import aws_sdk_securityhub.types.network_header

        out["Egress"] = aws_sdk_securityhub.types.network_header.serialize_json(
            value["egress"]
        )
    if "ingress" in value:
        import aws_sdk_securityhub.types.network_header

        out["Ingress"] = aws_sdk_securityhub.types.network_header.serialize_json(
            value["ingress"]
        )
    return out


def deserialize_json(data: dict) -> NetworkPathComponent:
    out: NetworkPathComponent = {}  # type: ignore[typeddict-item]
    if "ComponentId" in data:
        out["component_id"] = data["ComponentId"]
    if "ComponentType" in data:
        out["component_type"] = data["ComponentType"]
    if "Egress" in data:
        import aws_sdk_securityhub.types.network_header

        out["egress"] = aws_sdk_securityhub.types.network_header.deserialize_json(
            data["Egress"]
        )
    if "Ingress" in data:
        import aws_sdk_securityhub.types.network_header

        out["ingress"] = aws_sdk_securityhub.types.network_header.deserialize_json(
            data["Ingress"]
        )
    return out
