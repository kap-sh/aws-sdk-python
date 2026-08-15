"""Generated from Smithy shape ``com.amazonaws.ec2#IpamInternetRegistryAssociationAsn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class IpamInternetRegistryAssociationAsn(TypedDict, closed=True):
    asn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Autonomous System Number.</p>"""
    last_observed_at: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time when the ASN was last observed at the internet registry.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamInternetRegistryAssociationAsn, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "asn" in value:
        pairs.append((f"{key_prefix}Asn", str(value["asn"])))
    if "last_observed_at" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["last_observed_at"], pairs, f"{key_prefix}LastObservedAt"
        )


def deserialize_ec2_query(el: Element) -> IpamInternetRegistryAssociationAsn:
    out: IpamInternetRegistryAssociationAsn = {}  # type: ignore[typeddict-item]
    child_asn = el.find("asn")
    if child_asn is not None:
        out["asn"] = str(child_asn.text or "")
    child_last_observed_at = el.find("lastObservedAt")
    if child_last_observed_at is not None:
        import capo_ec2.types.millisecond_date_time

        out["last_observed_at"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_last_observed_at
            )
        )
    return out
