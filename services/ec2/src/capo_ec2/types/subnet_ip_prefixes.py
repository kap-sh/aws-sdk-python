"""Generated from Smithy shape ``com.amazonaws.ec2#SubnetIpPrefixes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.value_string_list


class SubnetIpPrefixes(TypedDict, closed=True):
    subnet_id: NotRequired["capo_ec2.types.string.String"]
    """<p>ID of the subnet.</p>"""
    ip_prefixes: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>Array of SubnetIpPrefixes objects.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SubnetIpPrefixes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "ip_prefixes" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["ip_prefixes"], pairs, f"{key_prefix}IpPrefixSet"
        )


def deserialize_ec2_query(el: Element) -> SubnetIpPrefixes:
    out: SubnetIpPrefixes = {}  # type: ignore[typeddict-item]
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    if el.find("IpPrefixSet") is not None:
        import capo_ec2.types.value_string_list

        out["ip_prefixes"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            el, "IpPrefixSet"
        )
    return out
