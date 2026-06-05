"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamExternalResourceVerificationTokenRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateIpamExternalResourceVerificationTokenRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_id: NotRequired["aws_sdk_ec2.types.ipam_id.IpamId"]
    """<p>The ID of the IPAM that will create the token.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>Token tags.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateIpamExternalResourceVerificationTokenRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_id" in value:
        pairs.append((f"{prefix}.IpamId", str(value["ipam_id"])))
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(
    el: Element,
) -> CreateIpamExternalResourceVerificationTokenRequest:
    out: CreateIpamExternalResourceVerificationTokenRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_id = el.find("IpamId")
    if child_ipam_id is not None:
        out["ipam_id"] = str(child_ipam_id.text or "")
    if el.find("TagSpecifications") is not None:
        import aws_sdk_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            aws_sdk_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
