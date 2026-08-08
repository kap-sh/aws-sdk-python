"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessInstanceCustomSubDomain``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.value_string_list


class VerifiedAccessInstanceCustomSubDomain(TypedDict, closed=True):
    sub_domain: NotRequired["capo_ec2.types.string.String"]
    """<p>The subdomain.</p>"""
    nameservers: NotRequired["capo_ec2.types.value_string_list.ValueStringList"]
    """<p>The name servers.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessInstanceCustomSubDomain,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "sub_domain" in value:
        pairs.append((f"{key_prefix}SubDomain", str(value["sub_domain"])))
    if "nameservers" in value:
        import capo_ec2.types.value_string_list

        capo_ec2.types.value_string_list.serialize_ec2_query(
            value["nameservers"], pairs, f"{key_prefix}NameserverSet"
        )


def deserialize_ec2_query(el: Element) -> VerifiedAccessInstanceCustomSubDomain:
    out: VerifiedAccessInstanceCustomSubDomain = {}  # type: ignore[typeddict-item]
    child_sub_domain = el.find("subDomain")
    if child_sub_domain is not None:
        out["sub_domain"] = str(child_sub_domain.text or "")
    if el.find("nameserverSet") is not None:
        import capo_ec2.types.value_string_list

        out["nameservers"] = capo_ec2.types.value_string_list.deserialize_ec2_query(
            el, "nameserverSet"
        )
    return out
