"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSecondarySubnetResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.secondary_subnet
    import capo_ec2.types.string


class CreateSecondarySubnetResult(TypedDict, closed=True):
    secondary_subnet: NotRequired["capo_ec2.types.secondary_subnet.SecondarySubnet"]
    """<p>Information about the secondary subnet.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateSecondarySubnetResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "secondary_subnet" in value:
        import capo_ec2.types.secondary_subnet

        capo_ec2.types.secondary_subnet.serialize_ec2_query(
            value["secondary_subnet"], pairs, f"{prefix}.SecondarySubnet"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateSecondarySubnetResult:
    out: CreateSecondarySubnetResult = {}  # type: ignore[typeddict-item]
    child_secondary_subnet = el.find("SecondarySubnet")
    if child_secondary_subnet is not None:
        import capo_ec2.types.secondary_subnet

        out["secondary_subnet"] = capo_ec2.types.secondary_subnet.deserialize_ec2_query(
            child_secondary_subnet
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
