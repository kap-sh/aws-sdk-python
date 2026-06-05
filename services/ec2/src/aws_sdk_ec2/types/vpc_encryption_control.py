"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionControl``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.vpc_encryption_control_exclusions
    import aws_sdk_ec2.types.vpc_encryption_control_id
    import aws_sdk_ec2.types.vpc_encryption_control_mode
    import aws_sdk_ec2.types.vpc_encryption_control_state
    import aws_sdk_ec2.types.vpc_id


class VpcEncryptionControl(TypedDict):
    vpc_id: NotRequired["aws_sdk_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC associated with the encryption control configuration.</p>"""
    vpc_encryption_control_id: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_id.VpcEncryptionControlId"
    ]
    """<p>The ID of the VPC Encryption Control configuration.</p>"""
    mode: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_mode.VpcEncryptionControlMode"
    ]
    """<p>The encryption mode for the VPC Encryption Control configuration.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_state.VpcEncryptionControlState"
    ]
    """<p>The current state of the VPC Encryption Control configuration.</p>"""
    state_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message providing additional information about the encryption control state.</p>"""
    resource_exclusions: NotRequired[
        "aws_sdk_ec2.types.vpc_encryption_control_exclusions.VpcEncryptionControlExclusions"
    ]
    """<p>Information about resource exclusions for the VPC Encryption Control configuration.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the VPC Encryption Control configuration.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcEncryptionControl, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpc_id" in value:
        pairs.append((f"{prefix}.VpcId", str(value["vpc_id"])))
    if "vpc_encryption_control_id" in value:
        pairs.append(
            (
                f"{prefix}.VpcEncryptionControlId",
                str(value["vpc_encryption_control_id"]),
            )
        )
    if "mode" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_mode

        aws_sdk_ec2.types.vpc_encryption_control_mode.serialize_ec2_query(
            value["mode"], pairs, f"{prefix}.Mode"
        )
    if "state" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_state

        aws_sdk_ec2.types.vpc_encryption_control_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "state_message" in value:
        pairs.append((f"{prefix}.StateMessage", str(value["state_message"])))
    if "resource_exclusions" in value:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusions

        aws_sdk_ec2.types.vpc_encryption_control_exclusions.serialize_ec2_query(
            value["resource_exclusions"], pairs, f"{prefix}.ResourceExclusions"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> VpcEncryptionControl:
    out: VpcEncryptionControl = {}  # type: ignore[typeddict-item]
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_vpc_encryption_control_id = el.find("VpcEncryptionControlId")
    if child_vpc_encryption_control_id is not None:
        out["vpc_encryption_control_id"] = str(
            child_vpc_encryption_control_id.text or ""
        )
    child_mode = el.find("Mode")
    if child_mode is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_mode

        out["mode"] = (
            aws_sdk_ec2.types.vpc_encryption_control_mode.deserialize_ec2_query(
                child_mode
            )
        )
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_state

        out["state"] = (
            aws_sdk_ec2.types.vpc_encryption_control_state.deserialize_ec2_query(
                child_state
            )
        )
    child_state_message = el.find("StateMessage")
    if child_state_message is not None:
        out["state_message"] = str(child_state_message.text or "")
    child_resource_exclusions = el.find("ResourceExclusions")
    if child_resource_exclusions is not None:
        import aws_sdk_ec2.types.vpc_encryption_control_exclusions

        out["resource_exclusions"] = (
            aws_sdk_ec2.types.vpc_encryption_control_exclusions.deserialize_ec2_query(
                child_resource_exclusions
            )
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
