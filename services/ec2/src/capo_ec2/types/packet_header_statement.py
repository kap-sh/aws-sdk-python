"""Generated from Smithy shape ``com.amazonaws.ec2#PacketHeaderStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.protocol_list
    import capo_ec2.types.value_string_list


class PacketHeaderStatement(TypedDict, closed=True):
    source_addresses: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The source addresses.</p>"""
    destination_addresses: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The destination addresses.</p>"""
    source_ports: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The source ports.</p>"""
    destination_ports: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The destination ports.</p>"""
    source_prefix_lists: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The source prefix lists.</p>"""
    destination_prefix_lists: NotRequired[
        "capo_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The destination prefix lists.</p>"""
    protocols: NotRequired["capo_ec2.types.protocol_list.ProtocolList"]
    """<p>The protocols.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PacketHeaderStatement, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source_addresses" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["source_addresses"], pairs, f"{key_prefix}SourceAddressSet"
        )
    if "destination_addresses" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["destination_addresses"], pairs, f"{key_prefix}DestinationAddressSet"
        )
    if "source_ports" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["source_ports"], pairs, f"{key_prefix}SourcePortSet"
        )
    if "destination_ports" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["destination_ports"], pairs, f"{key_prefix}DestinationPortSet"
        )
    if "source_prefix_lists" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["source_prefix_lists"], pairs, f"{key_prefix}SourcePrefixListSet"
        )
    if "destination_prefix_lists" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["destination_prefix_lists"],
            pairs,
            f"{key_prefix}DestinationPrefixListSet",
        )
    if "protocols" in value:
        import capo_ec2.types.protocol_list

        capo_ec2.types.protocol_list.serialize_ec2_query(
            value["protocols"], pairs, f"{key_prefix}ProtocolSet"
        )


def deserialize_ec2_query(el: Element) -> PacketHeaderStatement:
    out: PacketHeaderStatement = {}  # type: ignore[typeddict-item]
    child_source_addresses = el.find("sourceAddressSet")
    if child_source_addresses is not None:
        import capo_ec2.types.value_string_list

        out["source_addresses"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                child_source_addresses
            )
        )
    child_destination_addresses = el.find("destinationAddressSet")
    if child_destination_addresses is not None:
        import capo_ec2.types.value_string_list

        out["destination_addresses"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                child_destination_addresses
            )
        )
    child_source_ports = el.find("sourcePortSet")
    if child_source_ports is not None:
        import capo_ec2.types.value_string_list

        out["source_ports"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            child_source_ports
        )
    child_destination_ports = el.find("destinationPortSet")
    if child_destination_ports is not None:
        import capo_ec2.types.value_string_list

        out["destination_ports"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                child_destination_ports
            )
        )
    child_source_prefix_lists = el.find("sourcePrefixListSet")
    if child_source_prefix_lists is not None:
        import capo_ec2.types.value_string_list

        out["source_prefix_lists"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                child_source_prefix_lists
            )
        )
    child_destination_prefix_lists = el.find("destinationPrefixListSet")
    if child_destination_prefix_lists is not None:
        import capo_ec2.types.value_string_list

        out["destination_prefix_lists"] = (
            capo_ec2.types.value_string_list.deserialize_ec2_query(
                child_destination_prefix_lists
            )
        )
    child_protocols = el.find("protocolSet")
    if child_protocols is not None:
        import capo_ec2.types.protocol_list

        out["protocols"] = capo_ec2.types.protocol_list.deserialize_ec2_query(
            child_protocols
        )
    return out
