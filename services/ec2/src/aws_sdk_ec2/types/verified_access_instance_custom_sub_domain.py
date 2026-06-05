"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessInstanceCustomSubDomain``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.value_string_list


class VerifiedAccessInstanceCustomSubDomain(TypedDict):
    sub_domain: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The subdomain.</p>"""
    nameservers: NotRequired["aws_sdk_ec2.types.value_string_list.ValueStringList"]
    """<p>The name servers.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessInstanceCustomSubDomain,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "sub_domain" in value:
        pairs.append((f"{prefix}.SubDomain", str(value["sub_domain"])))
    if "nameservers" in value:
        import aws_sdk_ec2.types.value_string_list

        aws_sdk_ec2.types.value_string_list.serialize_ec2_query(
            value["nameservers"], pairs, f"{prefix}.NameserverSet"
        )


def deserialize_ec2_query(el: Element) -> VerifiedAccessInstanceCustomSubDomain:
    out: VerifiedAccessInstanceCustomSubDomain = {}  # type: ignore[typeddict-item]
    child_sub_domain = el.find("SubDomain")
    if child_sub_domain is not None:
        out["sub_domain"] = str(child_sub_domain.text or "")
    if el.find("NameserverSet") is not None:
        import aws_sdk_ec2.types.value_string_list

        out["nameservers"] = aws_sdk_ec2.types.value_string_list.deserialize_ec2_query(
            el, "NameserverSet"
        )
    return out
