"""Generated from Smithy shape ``com.amazonaws.iot#ListDomainConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.domain_configurations
    import aws_sdk_iot.types.marker


class ListDomainConfigurationsResponse(TypedDict, closed=True):
    domain_configurations: NotRequired[
        "aws_sdk_iot.types.domain_configurations.DomainConfigurations"
    ]
    """<p>A list of objects that contain summary information about the user's domain configurations.</p>"""
    next_marker: NotRequired["aws_sdk_iot.types.marker.Marker"]
    """<p>The marker for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainConfigurationsResponse) -> dict:
    out: dict = {}
    if "domain_configurations" in value:
        import aws_sdk_iot.types.domain_configurations

        out["domainConfigurations"] = (
            aws_sdk_iot.types.domain_configurations.serialize_json(
                value["domain_configurations"]
            )
        )
    if "next_marker" in value:
        out["nextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListDomainConfigurationsResponse:
    out: ListDomainConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "domainConfigurations" in data:
        import aws_sdk_iot.types.domain_configurations

        out["domain_configurations"] = (
            aws_sdk_iot.types.domain_configurations.deserialize_json(
                data["domainConfigurations"]
            )
        )
    if "nextMarker" in data:
        out["next_marker"] = data["nextMarker"]
    return out
