"""Generated from Smithy shape ``com.amazonaws.securityhub#NetworkPathComponentDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.port_range_list
    import aws_sdk_securityhub.types.string_list


class NetworkPathComponentDetails(TypedDict):
    address: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p>The IP addresses of the destination.</p>"""
    port_ranges: NotRequired["aws_sdk_securityhub.types.port_range_list.PortRangeList"]
    """<p>A list of port ranges for the destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkPathComponentDetails) -> dict:
    out: dict = {}
    if "address" in value:
        import aws_sdk_securityhub.types.string_list

        out["Address"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["address"]
        )
    if "port_ranges" in value:
        import aws_sdk_securityhub.types.port_range_list

        out["PortRanges"] = aws_sdk_securityhub.types.port_range_list.serialize_json(
            value["port_ranges"]
        )
    return out


def deserialize_json(data: dict) -> NetworkPathComponentDetails:
    out: NetworkPathComponentDetails = {}  # type: ignore[typeddict-item]
    if "Address" in data:
        import aws_sdk_securityhub.types.string_list

        out["address"] = aws_sdk_securityhub.types.string_list.deserialize_json(
            data["Address"]
        )
    if "PortRanges" in data:
        import aws_sdk_securityhub.types.port_range_list

        out["port_ranges"] = aws_sdk_securityhub.types.port_range_list.deserialize_json(
            data["PortRanges"]
        )
    return out
