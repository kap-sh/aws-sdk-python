"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpcEncryptionControlsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpc_encryption_control_list


class DescribeVpcEncryptionControlsResult(TypedDict, closed=True):
    vpc_encryption_controls: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_list.VpcEncryptionControlList"
    ]
    """<p>Information about the VPC Encryption Control configurations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpcEncryptionControlsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "vpc_encryption_controls" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_list

        aws_sdk_ec2.types.vpc_encryption_control_list.serialize_ec2_query(
            value["vpc_encryption_controls"], pairs, f"{prefix}.VpcEncryptionControlSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeVpcEncryptionControlsResult:
    out: DescribeVpcEncryptionControlsResult = {}  # type: ignore[typeddict-item]
    if el.find("VpcEncryptionControlSet") is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_list

        out["vpc_encryption_controls"] = (
            aws_sdk_ec2.types.vpc_encryption_control_list.deserialize_ec2_query(
                el, "VpcEncryptionControlSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
