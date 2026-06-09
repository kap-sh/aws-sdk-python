"""Generated from Smithy shape ``com.amazonaws.ec2#PathRequestFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ip_address
    import aws_sdk_ec2.types.request_filter_port_range


class PathRequestFilter(TypedDict):
    source_address: NotRequired["aws_sdk_ec2.types.ip_address.IpAddress"]
    """<p>The source IPv4 address.</p>"""
    source_port_range: NotRequired[
        "aws_sdk_ec2.types.request_filter_port_range.RequestFilterPortRange"
    ]
    """<p>The source port range.</p>"""
    destination_address: NotRequired["aws_sdk_ec2.types.ip_address.IpAddress"]
    """<p>The destination IPv4 address.</p>"""
    destination_port_range: NotRequired[
        "aws_sdk_ec2.types.request_filter_port_range.RequestFilterPortRange"
    ]
    """<p>The destination port range.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PathRequestFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source_address" in value:
        pairs.append((f"{prefix}.SourceAddress", str(value["source_address"])))
    if "source_port_range" in value:
        import aws_sdk_ec2.types.request_filter_port_range

        aws_sdk_ec2.types.request_filter_port_range.serialize_ec2_query(
            value["source_port_range"], pairs, f"{prefix}.SourcePortRange"
        )
    if "destination_address" in value:
        pairs.append(
            (f"{prefix}.DestinationAddress", str(value["destination_address"]))
        )
    if "destination_port_range" in value:
        import aws_sdk_ec2.types.request_filter_port_range

        aws_sdk_ec2.types.request_filter_port_range.serialize_ec2_query(
            value["destination_port_range"], pairs, f"{prefix}.DestinationPortRange"
        )


def deserialize_ec2_query(el: Element) -> PathRequestFilter:
    out: PathRequestFilter = {}  # type: ignore[typeddict-item]
    child_source_address = el.find("SourceAddress")
    if child_source_address is not None:
        out["source_address"] = str(child_source_address.text or "")
    child_source_port_range = el.find("SourcePortRange")
    if child_source_port_range is not None:
        import aws_sdk_ec2.types.request_filter_port_range

        out["source_port_range"] = (
            aws_sdk_ec2.types.request_filter_port_range.deserialize_ec2_query(
                child_source_port_range
            )
        )
    child_destination_address = el.find("DestinationAddress")
    if child_destination_address is not None:
        out["destination_address"] = str(child_destination_address.text or "")
    child_destination_port_range = el.find("DestinationPortRange")
    if child_destination_port_range is not None:
        import aws_sdk_ec2.types.request_filter_port_range

        out["destination_port_range"] = (
            aws_sdk_ec2.types.request_filter_port_range.deserialize_ec2_query(
                child_destination_port_range
            )
        )
    return out
