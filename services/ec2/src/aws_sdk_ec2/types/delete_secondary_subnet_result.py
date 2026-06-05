"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteSecondarySubnetResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_subnet
    import aws_sdk_ec2.types.string


class DeleteSecondarySubnetResult(TypedDict):
    secondary_subnet: NotRequired["aws_sdk_ec2.types.secondary_subnet.SecondarySubnet"]
    """<p>Information about the secondary subnet being deleted.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteSecondarySubnetResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "secondary_subnet" in value:
        import aws_sdk_ec2.types.secondary_subnet

        aws_sdk_ec2.types.secondary_subnet.serialize_ec2_query(
            value["secondary_subnet"], pairs, f"{prefix}.SecondarySubnet"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> DeleteSecondarySubnetResult:
    out: DeleteSecondarySubnetResult = {}  # type: ignore[typeddict-item]
    child_secondary_subnet = el.find("SecondarySubnet")
    if child_secondary_subnet is not None:
        import aws_sdk_ec2.types.secondary_subnet

        out["secondary_subnet"] = (
            aws_sdk_ec2.types.secondary_subnet.deserialize_ec2_query(
                child_secondary_subnet
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
