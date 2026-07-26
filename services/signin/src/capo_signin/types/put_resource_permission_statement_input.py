"""Generated from Smithy shape ``com.amazonaws.signin#PutResourcePermissionStatementInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signin.types.client_token
    import capo_signin.types.excluded_principal
    import capo_signin.types.requested_region
    import capo_signin.types.source_ip
    import capo_signin.types.source_vpc
    import capo_signin.types.source_vpce
    import capo_signin.types.vpc_source_ip


class PutResourcePermissionStatementInput(TypedDict, closed=True):
    source_vpc: NotRequired["capo_signin.types.source_vpc.SourceVpc"]
    """VPC identifier to restrict console access"""
    signin_source_vpce: NotRequired["capo_signin.types.source_vpce.SourceVpce"]
    """SignIn VPC endpoint identifier"""
    console_source_vpce: NotRequired["capo_signin.types.source_vpce.SourceVpce"]
    """Console VPC endpoint identifier"""
    vpc_source_ip: NotRequired["capo_signin.types.vpc_source_ip.VpcSourceIp"]
    """Source IP address within VPC"""
    source_ip: NotRequired["capo_signin.types.source_ip.SourceIp"]
    """Source IP address"""
    requested_region: NotRequired["capo_signin.types.requested_region.RequestedRegion"]
    """AWS region where the VPC and VPC endpoint reside Required when sourceVpc or signinSourceVpce/consoleSourceVpce is provided"""
    excluded_principal: NotRequired[
        "capo_signin.types.excluded_principal.ExcludedPrincipal"
    ]
    """Principal to exclude from the permission statement"""
    client_token: NotRequired["capo_signin.types.client_token.ClientToken"]
    """Idempotency token for the request"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourcePermissionStatementInput) -> dict:
    out: dict = {}
    if "source_vpc" in value:
        out["sourceVpc"] = value["source_vpc"]
    if "signin_source_vpce" in value:
        out["signinSourceVpce"] = value["signin_source_vpce"]
    if "console_source_vpce" in value:
        out["consoleSourceVpce"] = value["console_source_vpce"]
    if "vpc_source_ip" in value:
        out["vpcSourceIp"] = value["vpc_source_ip"]
    if "source_ip" in value:
        out["sourceIp"] = value["source_ip"]
    if "requested_region" in value:
        out["requestedRegion"] = value["requested_region"]
    if "excluded_principal" in value:
        out["excludedPrincipal"] = value["excluded_principal"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> PutResourcePermissionStatementInput:
    out: PutResourcePermissionStatementInput = {}  # type: ignore[typeddict-item]
    if "sourceVpc" in data:
        out["source_vpc"] = data["sourceVpc"]
    if "signinSourceVpce" in data:
        out["signin_source_vpce"] = data["signinSourceVpce"]
    if "consoleSourceVpce" in data:
        out["console_source_vpce"] = data["consoleSourceVpce"]
    if "vpcSourceIp" in data:
        out["vpc_source_ip"] = data["vpcSourceIp"]
    if "sourceIp" in data:
        out["source_ip"] = data["sourceIp"]
    if "requestedRegion" in data:
        out["requested_region"] = data["requestedRegion"]
    if "excludedPrincipal" in data:
        out["excluded_principal"] = data["excludedPrincipal"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
