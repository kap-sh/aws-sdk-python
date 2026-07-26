"""Generated from Smithy shape ``com.amazonaws.securityhub#NetworkPathComponentDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.port_range_list
    import capo_securityhub.types.string_list


class NetworkPathComponentDetails(TypedDict, closed=True):
    address: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p>The IP addresses of the destination.</p>"""
    port_ranges: NotRequired["capo_securityhub.types.port_range_list.PortRangeList"]
    """<p>A list of port ranges for the destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkPathComponentDetails) -> dict:
    out: dict = {}
    if "address" in value:
        import capo_securityhub.types.string_list

        out["Address"] = capo_securityhub.types.string_list.serialize_json(
            value["address"]
        )
    if "port_ranges" in value:
        import capo_securityhub.types.port_range_list

        out["PortRanges"] = capo_securityhub.types.port_range_list.serialize_json(
            value["port_ranges"]
        )
    return out


def deserialize_json(data: dict) -> NetworkPathComponentDetails:
    out: NetworkPathComponentDetails = {}  # type: ignore[typeddict-item]
    if "Address" in data:
        import capo_securityhub.types.string_list

        out["address"] = capo_securityhub.types.string_list.deserialize_json(
            data["Address"]
        )
    if "PortRanges" in data:
        import capo_securityhub.types.port_range_list

        out["port_ranges"] = capo_securityhub.types.port_range_list.deserialize_json(
            data["PortRanges"]
        )
    return out
