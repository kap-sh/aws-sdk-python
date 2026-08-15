"""Generated from Smithy shape ``com.amazonaws.ec2#IpamInternetRegistryAssociationCidr``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class IpamInternetRegistryAssociationCidr(TypedDict, closed=True):
    cidr: NotRequired["capo_ec2.types.string.String"]
    """<p>The IP address prefix in CIDR notation.</p>"""
    last_observed_at: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time when the CIDR was last observed at the internet registry.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamInternetRegistryAssociationCidr,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cidr" in value:
        pairs.append((f"{key_prefix}Cidr", str(value["cidr"])))
    if "last_observed_at" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["last_observed_at"], pairs, f"{key_prefix}LastObservedAt"
        )


def deserialize_ec2_query(el: Element) -> IpamInternetRegistryAssociationCidr:
    out: IpamInternetRegistryAssociationCidr = {}  # type: ignore[typeddict-item]
    child_cidr = el.find("cidr")
    if child_cidr is not None:
        out["cidr"] = str(child_cidr.text or "")
    child_last_observed_at = el.find("lastObservedAt")
    if child_last_observed_at is not None:
        import capo_ec2.types.millisecond_date_time

        out["last_observed_at"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_last_observed_at
            )
        )
    return out
