"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainEndpointOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.domain_endpoint_options
    import capo_opensearch.types.option_status


class DomainEndpointOptionsStatus(TypedDict, closed=True):
    options: "capo_opensearch.types.domain_endpoint_options.DomainEndpointOptions"
    """<p>Options to configure the endpoint for a domain.</p>"""
    status: "capo_opensearch.types.option_status.OptionStatus"
    """<p>The status of the endpoint options for a domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainEndpointOptionsStatus) -> dict:
    out: dict = {}
    import capo_opensearch.types.domain_endpoint_options

    out["Options"] = capo_opensearch.types.domain_endpoint_options.serialize_json(
        value["options"]
    )
    import capo_opensearch.types.option_status

    out["Status"] = capo_opensearch.types.option_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> DomainEndpointOptionsStatus:
    out: DomainEndpointOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import capo_opensearch.types.domain_endpoint_options

        out["options"] = capo_opensearch.types.domain_endpoint_options.deserialize_json(
            data["Options"]
        )
    else:
        raise DeserializationError("DomainEndpointOptionsStatus.options required")
    if "Status" in data:
        import capo_opensearch.types.option_status

        out["status"] = capo_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("DomainEndpointOptionsStatus.status required")
    return out
