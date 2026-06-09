"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkAclResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_acl
    import aws_sdk_ec2.types.string


class CreateNetworkAclResult(TypedDict):
    network_acl: NotRequired["aws_sdk_ec2.types.network_acl.NetworkAcl"]
    """<p>Information about the network ACL.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateNetworkAclResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "network_acl" in value:
        import aws_sdk_ec2.types.network_acl

        aws_sdk_ec2.types.network_acl.serialize_ec2_query(
            value["network_acl"], pairs, f"{prefix}.NetworkAcl"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CreateNetworkAclResult:
    out: CreateNetworkAclResult = {}  # type: ignore[typeddict-item]
    child_network_acl = el.find("NetworkAcl")
    if child_network_acl is not None:
        import aws_sdk_ec2.types.network_acl

        out["network_acl"] = aws_sdk_ec2.types.network_acl.deserialize_ec2_query(
            child_network_acl
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
