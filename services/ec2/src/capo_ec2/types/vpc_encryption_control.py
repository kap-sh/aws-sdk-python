"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEncryptionControl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.vpc_encryption_control_exclusions
    import capo_ec2.types.vpc_encryption_control_id
    import capo_ec2.types.vpc_encryption_control_mode
    import capo_ec2.types.vpc_encryption_control_state
    import capo_ec2.types.vpc_id


class VpcEncryptionControl(TypedDict, closed=True):
    vpc_id: NotRequired["capo_ec2.types.vpc_id.VpcId"]
    """<p>The ID of the VPC associated with the encryption control configuration.</p>"""
    vpc_encryption_control_id: NotRequired[
        "capo_ec2.types.vpc_encryption_control_id.VpcEncryptionControlId"
    ]
    """<p>The ID of the VPC Encryption Control configuration.</p>"""
    mode: NotRequired[
        "capo_ec2.types.vpc_encryption_control_mode.VpcEncryptionControlMode"
    ]
    """<p>The encryption mode for the VPC Encryption Control configuration.</p>"""
    state: NotRequired[
        "capo_ec2.types.vpc_encryption_control_state.VpcEncryptionControlState"
    ]
    """<p>The current state of the VPC Encryption Control configuration.</p>"""
    state_message: NotRequired["capo_ec2.types.string.String"]
    """<p>A message providing additional information about the encryption control state.</p>"""
    resource_exclusions: NotRequired[
        "capo_ec2.types.vpc_encryption_control_exclusions.VpcEncryptionControlExclusions"
    ]
    """<p>Information about resource exclusions for the VPC Encryption Control configuration.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the VPC Encryption Control configuration.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcEncryptionControl, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "vpc_encryption_control_id" in value:
        pairs.append(
            (
                f"{key_prefix}VpcEncryptionControlId",
                str(value["vpc_encryption_control_id"]),
            )
        )
    if "mode" in value:
        import capo_ec2.types.vpc_encryption_control_mode

        capo_ec2.types.vpc_encryption_control_mode.serialize_ec2_query(
            value["mode"], pairs, f"{key_prefix}Mode"
        )
    if "state" in value:
        import capo_ec2.types.vpc_encryption_control_state

        capo_ec2.types.vpc_encryption_control_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "state_message" in value:
        pairs.append((f"{key_prefix}StateMessage", str(value["state_message"])))
    if "resource_exclusions" in value:
        import capo_ec2.types.vpc_encryption_control_exclusions

        capo_ec2.types.vpc_encryption_control_exclusions.serialize_ec2_query(
            value["resource_exclusions"], pairs, f"{key_prefix}ResourceExclusions"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
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
        import capo_ec2.types.vpc_encryption_control_mode

        out["mode"] = capo_ec2.types.vpc_encryption_control_mode.deserialize_ec2_query(
            child_mode
        )
    child_state = el.find("State")
    if child_state is not None:
        import capo_ec2.types.vpc_encryption_control_state

        out["state"] = (
            capo_ec2.types.vpc_encryption_control_state.deserialize_ec2_query(
                child_state
            )
        )
    child_state_message = el.find("StateMessage")
    if child_state_message is not None:
        out["state_message"] = str(child_state_message.text or "")
    child_resource_exclusions = el.find("ResourceExclusions")
    if child_resource_exclusions is not None:
        import capo_ec2.types.vpc_encryption_control_exclusions

        out["resource_exclusions"] = (
            capo_ec2.types.vpc_encryption_control_exclusions.deserialize_ec2_query(
                child_resource_exclusions
            )
        )
    if el.find("TagSet") is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
