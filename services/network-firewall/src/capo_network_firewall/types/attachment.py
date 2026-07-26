"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Attachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.attachment_status
    import capo_network_firewall.types.az_subnet
    import capo_network_firewall.types.endpoint_id
    import capo_network_firewall.types.status_message


class Attachment(TypedDict, closed=True):
    subnet_id: NotRequired["capo_network_firewall.types.az_subnet.AzSubnet"]
    """<p>The unique identifier of the subnet that you've specified to be used for a firewall endpoint. </p>"""
    endpoint_id: NotRequired["capo_network_firewall.types.endpoint_id.EndpointId"]
    """<p>The identifier of the firewall endpoint that Network Firewall has instantiated in the subnet. You use this to identify the firewall endpoint in the VPC route tables, when you redirect the VPC traffic through the endpoint. </p>"""
    status: NotRequired[
        "capo_network_firewall.types.attachment_status.AttachmentStatus"
    ]
    """<p>The current status of the firewall endpoint instantiation in the subnet. </p> <p>When this value is <code>READY</code>, the endpoint is available to handle network traffic. Otherwise, this value reflects its state, for example <code>CREATING</code> or <code>DELETING</code>.</p>"""
    status_message: NotRequired[
        "capo_network_firewall.types.status_message.StatusMessage"
    ]
    r"""<p>If Network Firewall fails to create or delete the firewall endpoint in the subnet, it populates this with the reason for the error or failure and how to resolve it. A <code>FAILED</code> status indicates a non-recoverable state, and a <code>ERROR</code> status indicates an issue that you can fix. Depending on the error, it can take as many as 15 minutes to populate this field. For more information about the causes for failiure or errors and solutions available for this field, see <a href=\"https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-troubleshooting-endpoint-failures.html\">Troubleshooting firewall endpoint failures</a> in the <i>Network Firewall Developer Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Attachment) -> dict:
    out: dict = {}
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    if "status" in value:
        import capo_network_firewall.types.attachment_status

        out["Status"] = (
            capo_network_firewall.types.attachment_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Attachment:
    out: Attachment = {}  # type: ignore[typeddict-item]
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    if "Status" in data:
        import capo_network_firewall.types.attachment_status

        out["status"] = (
            capo_network_firewall.types.attachment_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
