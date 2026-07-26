"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSecondaryNetworkResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.secondary_network
    import capo_ec2.types.string


class CreateSecondaryNetworkResult(TypedDict, closed=True):
    secondary_network: NotRequired["capo_ec2.types.secondary_network.SecondaryNetwork"]
    """<p>Information about the secondary network.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateSecondaryNetworkResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "secondary_network" in value:
        import capo_ec2.types.secondary_network

        capo_ec2.types.secondary_network.serialize_ec2_query(
            value["secondary_network"], pairs, f"{prefix}.SecondaryNetwork"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateSecondaryNetworkResult:
    out: CreateSecondaryNetworkResult = {}  # type: ignore[typeddict-item]
    child_secondary_network = el.find("SecondaryNetwork")
    if child_secondary_network is not None:
        import capo_ec2.types.secondary_network

        out["secondary_network"] = (
            capo_ec2.types.secondary_network.deserialize_ec2_query(
                child_secondary_network
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
