"""Generated from Smithy shape ``com.amazonaws.ec2#PathStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.packet_header_statement
    import capo_ec2.types.resource_statement


class PathStatement(TypedDict, closed=True):
    packet_header_statement: NotRequired[
        "capo_ec2.types.packet_header_statement.PacketHeaderStatement"
    ]
    """<p>The packet header statement.</p>"""
    resource_statement: NotRequired[
        "capo_ec2.types.resource_statement.ResourceStatement"
    ]
    """<p>The resource statement.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PathStatement, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "packet_header_statement" in value:
        import capo_ec2.types.packet_header_statement

        capo_ec2.types.packet_header_statement.serialize_ec2_query(
            value["packet_header_statement"],
            pairs,
            f"{key_prefix}PacketHeaderStatement",
        )
    if "resource_statement" in value:
        import capo_ec2.types.resource_statement

        capo_ec2.types.resource_statement.serialize_ec2_query(
            value["resource_statement"], pairs, f"{key_prefix}ResourceStatement"
        )


def deserialize_ec2_query(el: Element) -> PathStatement:
    out: PathStatement = {}  # type: ignore[typeddict-item]
    child_packet_header_statement = el.find("PacketHeaderStatement")
    if child_packet_header_statement is not None:
        import capo_ec2.types.packet_header_statement

        out["packet_header_statement"] = (
            capo_ec2.types.packet_header_statement.deserialize_ec2_query(
                child_packet_header_statement
            )
        )
    child_resource_statement = el.find("ResourceStatement")
    if child_resource_statement is not None:
        import capo_ec2.types.resource_statement

        out["resource_statement"] = (
            capo_ec2.types.resource_statement.deserialize_ec2_query(
                child_resource_statement
            )
        )
    return out
