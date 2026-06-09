"""Generated from Smithy shape ``com.amazonaws.ec2#PacketHeaderStatementRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.protocol_list
    import aws_sdk_ec2.types.value_string_list


class PacketHeaderStatementRequest(TypedDict):
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
    value: PacketHeaderStatementRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source_addresses" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["source_addresses"], pairs, f"{prefix}.SourceAddresses"
        )
    if "destination_addresses" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["destination_addresses"], pairs, f"{prefix}.DestinationAddresses"
        )
    if "source_ports" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["source_ports"], pairs, f"{prefix}.SourcePorts"
        )
    if "destination_ports" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["destination_ports"], pairs, f"{prefix}.DestinationPorts"
        )
    if "source_prefix_lists" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["source_prefix_lists"], pairs, f"{prefix}.SourcePrefixLists"
        )
    if "destination_prefix_lists" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["destination_prefix_lists"], pairs, f"{prefix}.DestinationPrefixLists"
        )
    if "protocols" in value:
        import aws_sdk_ec2.types.protocol_list

        aws_sdk_ec2.types.protocol_list.serialize_ec2_query(
            value["protocols"], pairs, f"{prefix}.Protocols"
        )


def deserialize_ec2_query(el: Element) -> PacketHeaderStatementRequest:
    out: PacketHeaderStatementRequest = {}  # type: ignore[typeddict-item]
    if el.find("SourceAddresses") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["source_addresses"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "SourceAddresses"
            )
        )
    if el.find("DestinationAddresses") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["destination_addresses"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "DestinationAddresses"
            )
        )
    if el.find("SourcePorts") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["source_ports"] = aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
            el, "SourcePorts"
        )
    if el.find("DestinationPorts") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["destination_ports"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "DestinationPorts"
            )
        )
    if el.find("SourcePrefixLists") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["source_prefix_lists"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "SourcePrefixLists"
            )
        )
    if el.find("DestinationPrefixLists") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["destination_prefix_lists"] = (
            aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
                el, "DestinationPrefixLists"
            )
        )
    if el.find("Protocols") is not None:
        import aws_sdk_ec2.types.protocol_list

        out["protocols"] = aws_sdk_ec2.types.protocol_list.deserialize_ec2_query(
            el, "Protocols"
        )
    return out
