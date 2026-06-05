"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteSecondaryNetworkResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_network
    import aws_sdk_ec2.types.string


class DeleteSecondaryNetworkResult(TypedDict):
    secondary_network: NotRequired[
        "aws_sdk_ec2.types.secondary_network.SecondaryNetwork"
    ]
    """<p>Information about the secondary network.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteSecondaryNetworkResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "secondary_network" in value:
        import aws_sdk_ec2.types.secondary_network

        aws_sdk_ec2.types.secondary_network.serialize_ec2_query(
            value["secondary_network"], pairs, f"{prefix}.SecondaryNetwork"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> DeleteSecondaryNetworkResult:
    out: DeleteSecondaryNetworkResult = {}  # type: ignore[typeddict-item]
    child_secondary_network = el.find("SecondaryNetwork")
    if child_secondary_network is not None:
        import aws_sdk_ec2.types.secondary_network

        out["secondary_network"] = (
            aws_sdk_ec2.types.secondary_network.deserialize_ec2_query(
                child_secondary_network
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
