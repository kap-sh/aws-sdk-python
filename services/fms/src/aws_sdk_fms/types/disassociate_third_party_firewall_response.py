"""Generated from Smithy shape ``com.amazonaws.fms#DisassociateThirdPartyFirewallResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.third_party_firewall_association_status


class DisassociateThirdPartyFirewallResponse(TypedDict):
    third_party_firewall_status: NotRequired[
        "aws_sdk_fms.types.third_party_firewall_association_status.ThirdPartyFirewallAssociationStatus"
    ]
    """<p>The current status for the disassociation of a Firewall Manager administrators account with a third-party firewall.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateThirdPartyFirewallResponse) -> dict:
    out: dict = {}
    if "third_party_firewall_status" in value:
        import aws_sdk_fms.types.third_party_firewall_association_status

        out["ThirdPartyFirewallStatus"] = (
            aws_sdk_fms.types.third_party_firewall_association_status.serialize_aws_json_1_1(
                value["third_party_firewall_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateThirdPartyFirewallResponse:
    out: DisassociateThirdPartyFirewallResponse = {}  # type: ignore[typeddict-item]
    if "ThirdPartyFirewallStatus" in data:
        import aws_sdk_fms.types.third_party_firewall_association_status

        out["third_party_firewall_status"] = (
            aws_sdk_fms.types.third_party_firewall_association_status.deserialize_aws_json_1_1(
                data["ThirdPartyFirewallStatus"]
            )
        )
    return out
