"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetIpPrefixes``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class SubnetIpPrefixes(TypedDict):
    subnet_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>ID of the subnet.</p>"""
    ip_prefixes: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>Array of SubnetIpPrefixes objects.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SubnetIpPrefixes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "subnet_id" in value:
        pairs.append((f"{prefix}.SubnetId", str(value["subnet_id"])))
    if "ip_prefixes" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["ip_prefixes"], pairs, f"{prefix}.IpPrefixSet"
        )


def deserialize_ec2_query(el: Element) -> SubnetIpPrefixes:
    out: SubnetIpPrefixes = {}  # type: ignore[typeddict-item]
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    if el.find("IpPrefixSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["ip_prefixes"] = aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
            el, "IpPrefixSet"
        )
    return out
