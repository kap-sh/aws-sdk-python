"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEncryptionControlsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.vpc_encryption_control_list


class DescribeVpcEncryptionControlsResult(TypedDict, closed=True):
    vpc_encryption_controls: NotRequired[
        "capo_ec2.types.vpc_encryption_control_list.VpcEncryptionControlList"
    ]
    """<p>Information about the VPC Encryption Control configurations.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcEncryptionControlsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpc_encryption_controls" in value:
        import capo_ec2.types.vpc_encryption_control_list

        capo_ec2.types.vpc_encryption_control_list.serialize_ec2_query(
            value["vpc_encryption_controls"],
            pairs,
            f"{key_prefix}VpcEncryptionControlSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVpcEncryptionControlsResult:
    out: DescribeVpcEncryptionControlsResult = {}  # type: ignore[typeddict-item]
    child_vpc_encryption_controls = el.find("vpcEncryptionControlSet")
    if child_vpc_encryption_controls is not None:
        import capo_ec2.types.vpc_encryption_control_list

        out["vpc_encryption_controls"] = (
            capo_ec2.types.vpc_encryption_control_list.deserialize_ec2_query(
                child_vpc_encryption_controls
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
