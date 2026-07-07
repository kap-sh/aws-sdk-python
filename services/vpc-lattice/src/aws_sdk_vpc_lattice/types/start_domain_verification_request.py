"""Generated from Smithy shape ``com.amazonaws.vpclattice#StartDomainVerificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.client_token
    import aws_sdk_vpc_lattice.types.domain_name
    import aws_sdk_vpc_lattice.types.tag_map


class StartDomainVerificationRequest(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_vpc_lattice.types.client_token.ClientToken"]
    """<p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails. </p>"""
    domain_name: "aws_sdk_vpc_lattice.types.domain_name.DomainName"
    """<p> The domain name to verify ownership for. </p>"""
    tags: NotRequired["aws_sdk_vpc_lattice.types.tag_map.TagMap"]
    """<p> The tags for the domain verification. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDomainVerificationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["domainName"] = value["domain_name"]
    if "tags" in value:
        import aws_sdk_vpc_lattice.types.tag_map

        out["tags"] = aws_sdk_vpc_lattice.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartDomainVerificationRequest:
    out: StartDomainVerificationRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "domainName" in data:
        out["domain_name"] = data["domainName"]
    else:
        raise DeserializationError(
            "StartDomainVerificationRequest.domain_name required"
        )
    if "tags" in data:
        import aws_sdk_vpc_lattice.types.tag_map

        out["tags"] = aws_sdk_vpc_lattice.types.tag_map.deserialize_json(data["tags"])
    return out
