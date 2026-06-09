"""Generated from Smithy shape ``com.amazonaws.ec2#PacketHeaderStatement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.protocol_list
    import aws_sdk_ec2.types.value_string_list


class PacketHeaderStatement(TypedDict):
    source_addresses: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The source addresses.</p>"""
    destination_addresses: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The destination addresses.</p>"""
    source_ports: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The source ports.</p>"""
    destination_ports: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The destination ports.</p>"""
    source_prefix_lists: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The source prefix lists.</p>"""
    destination_prefix_lists: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The destination prefix lists.</p>"""
    protocols: NotRequired["aws_sdk_ec2.types.protocol_list.ProtocolList"]
    """<p>The protocols.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PacketHeaderStatement, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source_addresses" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["source_addresses"], pairs, f"{prefix}.SourceAddressSet"
        )
    if "destination_addresses" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["destination_addresses"], pairs, f"{prefix}.DestinationAddressSet"
        )
    if "source_ports" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["source_ports"], pairs, f"{prefix}.SourcePortSet"
        )
    if "destination_ports" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["destination_ports"], pairs, f"{prefix}.DestinationPortSet"
        )
    if "source_prefix_lists" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["source_prefix_lists"], pairs, f"{prefix}.SourcePrefixListSet"
        )
    if "destination_prefix_lists" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["destination_prefix_lists"],
            pairs,
            f"{prefix}.DestinationPrefixListSet",
        )
    if "protocols" in value:
        import aws_sdk_ec2.types.protocol_list

        aws_sdk_ec2.types.protocol_list.serialize_ec2_query(
            value["protocols"], pairs, f"{prefix}.ProtocolSet"
        )


def deserialize_ec2_query(el: Element) -> PacketHeaderStatement:
    out: PacketHeaderStatement = {}  # type: ignore[typeddict-item]
    if el.find("SourceAddressSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["source_addresses"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "SourceAddressSet"
            )
        )
    if el.find("DestinationAddressSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["destination_addresses"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "DestinationAddressSet"
            )
        )
    if el.find("SourcePortSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["source_ports"] = aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
            el, "SourcePortSet"
        )
    if el.find("DestinationPortSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["destination_ports"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "DestinationPortSet"
            )
        )
    if el.find("SourcePrefixListSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["source_prefix_lists"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "SourcePrefixListSet"
            )
        )
    if el.find("DestinationPrefixListSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["destination_prefix_lists"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "DestinationPrefixListSet"
            )
        )
    if el.find("ProtocolSet") is not None:
        import aws_sdk_ec2.types.protocol_list

        out["protocols"] = aws_sdk_ec2.types.protocol_list.deserialize_ec2_query(
            el, "ProtocolSet"
        )
    return out
