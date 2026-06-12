"""Generated from Smithy shape ``com.amazonaws.lightsail#RegisteredDomainDelegationInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.name_servers_update_state
    import aws_sdk_lightsail.types.r53_hosted_zone_deletion_state


class RegisteredDomainDelegationInfo(TypedDict):
    name_servers_update_state: NotRequired[
        "aws_sdk_lightsail.types.name_servers_update_state.NameServersUpdateState"
    ]
    """<p>An object that describes the state of the name server records that are automatically added to the Route 53 domain by Lightsail.</p>"""
    r53_hosted_zone_deletion_state: NotRequired[
        "aws_sdk_lightsail.types.r53_hosted_zone_deletion_state.R53HostedZoneDeletionState"
    ]
    """<p>Describes the deletion state of an Amazon Route 53 hosted zone for a domain that is being automatically delegated to an Amazon Lightsail DNS zone.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisteredDomainDelegationInfo) -> dict:
    out: dict = {}
    if "name_servers_update_state" in value:
        import aws_sdk_lightsail.types.name_servers_update_state

        out["nameServersUpdateState"] = (
            aws_sdk_lightsail.types.name_servers_update_state.serialize_aws_json_1_1(
                value["name_servers_update_state"]
            )
        )
    if "r53_hosted_zone_deletion_state" in value:
        import aws_sdk_lightsail.types.r53_hosted_zone_deletion_state

        out["r53HostedZoneDeletionState"] = (
            aws_sdk_lightsail.types.r53_hosted_zone_deletion_state.serialize_aws_json_1_1(
                value["r53_hosted_zone_deletion_state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisteredDomainDelegationInfo:
    out: RegisteredDomainDelegationInfo = {}  # type: ignore[typeddict-item]
    if "nameServersUpdateState" in data:
        import aws_sdk_lightsail.types.name_servers_update_state

        out["name_servers_update_state"] = (
            aws_sdk_lightsail.types.name_servers_update_state.deserialize_aws_json_1_1(
                data["nameServersUpdateState"]
            )
        )
    if "r53HostedZoneDeletionState" in data:
        import aws_sdk_lightsail.types.r53_hosted_zone_deletion_state

        out["r53_hosted_zone_deletion_state"] = (
            aws_sdk_lightsail.types.r53_hosted_zone_deletion_state.deserialize_aws_json_1_1(
                data["r53HostedZoneDeletionState"]
            )
        )
    return out
