"""Generated from Smithy shape ``com.amazonaws.dlm#CreateLifecyclePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dlm.types.copy_tags_nullable
    import capo_dlm.types.create_interval
    import capo_dlm.types.cross_region_copy_target_list
    import capo_dlm.types.default_policy_type_values
    import capo_dlm.types.exclusions
    import capo_dlm.types.execution_role_arn
    import capo_dlm.types.extend_deletion
    import capo_dlm.types.policy_description
    import capo_dlm.types.policy_details
    import capo_dlm.types.retain_interval
    import capo_dlm.types.settable_policy_state_values
    import capo_dlm.types.tag_map


class CreateLifecyclePolicyRequest(TypedDict, closed=True):
    execution_role_arn: NotRequired[
        "capo_dlm.types.execution_role_arn.ExecutionRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.</p>"""
    description: NotRequired["capo_dlm.types.policy_description.PolicyDescription"]
    """<p>A description of the lifecycle policy. The characters ^[0-9A-Za-z _-]+$ are supported.</p>"""
    state: NotRequired[
        "capo_dlm.types.settable_policy_state_values.SettablePolicyStateValues"
    ]
    """<p>The activation state of the lifecycle policy after creation.</p>"""
    policy_details: NotRequired["capo_dlm.types.policy_details.PolicyDetails"]
    """<p>The configuration details of the lifecycle policy.</p> <important> <p>If you create a default policy, you can specify the request parameters either in the request body, or in the PolicyDetails request structure, but not both.</p> </important>"""
    tags: NotRequired["capo_dlm.types.tag_map.TagMap"]
    """<p>The tags to apply to the lifecycle policy during creation.</p>"""
    default_policy: NotRequired[
        "capo_dlm.types.default_policy_type_values.DefaultPolicyTypeValues"
    ]
    """<p> <b>[Default policies only]</b> Specify the type of default policy to create.</p> <ul> <li> <p>To create a default policy for EBS snapshots, that creates snapshots of all volumes in the Region that do not have recent backups, specify <code>VOLUME</code>.</p> </li> <li> <p>To create a default policy for EBS-backed AMIs, that creates EBS-backed AMIs from all instances in the Region that do not have recent backups, specify <code>INSTANCE</code>.</p> </li> </ul>"""
    create_interval: NotRequired["capo_dlm.types.create_interval.CreateInterval"]
    """<p> <b>[Default policies only]</b> Specifies how often the policy should run and create snapshots or AMIs. The creation frequency can range from 1 to 7 days. If you do not specify a value, the default is 1.</p> <p>Default: 1</p>"""
    retain_interval: NotRequired["capo_dlm.types.retain_interval.RetainInterval"]
    """<p> <b>[Default policies only]</b> Specifies how long the policy should retain snapshots or AMIs before deleting them. The retention period can range from 2 to 14 days, but it must be greater than the creation frequency to ensure that the policy retains at least 1 snapshot or AMI at any given time. If you do not specify a value, the default is 7.</p> <p>Default: 7</p>"""
    copy_tags: NotRequired["capo_dlm.types.copy_tags_nullable.CopyTagsNullable"]
    """<p> <b>[Default policies only]</b> Indicates whether the policy should copy tags from the source resource to the snapshot or AMI. If you do not specify a value, the default is <code>false</code>.</p> <p>Default: false</p>"""
    extend_deletion: NotRequired["capo_dlm.types.extend_deletion.ExtendDeletion"]
    """<p> <b>[Default policies only]</b> Defines the snapshot or AMI retention behavior for the policy if the source volume or instance is deleted, or if the policy enters the error, disabled, or deleted state.</p> <p>By default (<b>ExtendDeletion=false</b>):</p> <ul> <li> <p>If a source resource is deleted, Amazon Data Lifecycle Manager will continue to delete previously created snapshots or AMIs, up to but not including the last one, based on the specified retention period. If you want Amazon Data Lifecycle Manager to delete all snapshots or AMIs, including the last one, specify <code>true</code>.</p> </li> <li> <p>If a policy enters the error, disabled, or deleted state, Amazon Data Lifecycle Manager stops deleting snapshots and AMIs. If you want Amazon Data Lifecycle Manager to continue deleting snapshots or AMIs, including the last one, if the policy enters one of these states, specify <code>true</code>.</p> </li> </ul> <p>If you enable extended deletion (<b>ExtendDeletion=true</b>), you override both default behaviors simultaneously.</p> <p>If you do not specify a value, the default is <code>false</code>.</p> <p>Default: false</p>"""
    cross_region_copy_targets: NotRequired[
        "capo_dlm.types.cross_region_copy_target_list.CrossRegionCopyTargetList"
    ]
    """<p> <b>[Default policies only]</b> Specifies destination Regions for snapshot or AMI copies. You can specify up to 3 destination Regions. If you do not want to create cross-Region copies, omit this parameter.</p>"""
    exclusions: NotRequired["capo_dlm.types.exclusions.Exclusions"]
    """<p> <b>[Default policies only]</b> Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs. The policy will not create snapshots or AMIs for target resources that match any of the specified exclusion parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLifecyclePolicyRequest) -> dict:
    out: dict = {}
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "state" in value:
        import capo_dlm.types.settable_policy_state_values

        out["State"] = capo_dlm.types.settable_policy_state_values.serialize_json(
            value["state"]
        )
    if "policy_details" in value:
        import capo_dlm.types.policy_details

        out["PolicyDetails"] = capo_dlm.types.policy_details.serialize_json(
            value["policy_details"]
        )
    if "tags" in value:
        import capo_dlm.types.tag_map

        out["Tags"] = capo_dlm.types.tag_map.serialize_json(value["tags"])
    if "default_policy" in value:
        import capo_dlm.types.default_policy_type_values

        out["DefaultPolicy"] = capo_dlm.types.default_policy_type_values.serialize_json(
            value["default_policy"]
        )
    if "create_interval" in value:
        out["CreateInterval"] = value["create_interval"]
    if "retain_interval" in value:
        out["RetainInterval"] = value["retain_interval"]
    if "copy_tags" in value:
        out["CopyTags"] = value["copy_tags"]
    if "extend_deletion" in value:
        out["ExtendDeletion"] = value["extend_deletion"]
    if "cross_region_copy_targets" in value:
        import capo_dlm.types.cross_region_copy_target_list

        out["CrossRegionCopyTargets"] = (
            capo_dlm.types.cross_region_copy_target_list.serialize_json(
                value["cross_region_copy_targets"]
            )
        )
    if "exclusions" in value:
        import capo_dlm.types.exclusions

        out["Exclusions"] = capo_dlm.types.exclusions.serialize_json(
            value["exclusions"]
        )
    return out


def deserialize_json(data: dict) -> CreateLifecyclePolicyRequest:
    out: CreateLifecyclePolicyRequest = {}  # type: ignore[typeddict-item]
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "State" in data:
        import capo_dlm.types.settable_policy_state_values

        out["state"] = capo_dlm.types.settable_policy_state_values.deserialize_json(
            data["State"]
        )
    if "PolicyDetails" in data:
        import capo_dlm.types.policy_details

        out["policy_details"] = capo_dlm.types.policy_details.deserialize_json(
            data["PolicyDetails"]
        )
    if "Tags" in data:
        import capo_dlm.types.tag_map

        out["tags"] = capo_dlm.types.tag_map.deserialize_json(data["Tags"])
    if "DefaultPolicy" in data:
        import capo_dlm.types.default_policy_type_values

        out["default_policy"] = (
            capo_dlm.types.default_policy_type_values.deserialize_json(
                data["DefaultPolicy"]
            )
        )
    if "CreateInterval" in data:
        out["create_interval"] = data["CreateInterval"]
    if "RetainInterval" in data:
        out["retain_interval"] = data["RetainInterval"]
    if "CopyTags" in data:
        out["copy_tags"] = data["CopyTags"]
    if "ExtendDeletion" in data:
        out["extend_deletion"] = data["ExtendDeletion"]
    if "CrossRegionCopyTargets" in data:
        import capo_dlm.types.cross_region_copy_target_list

        out["cross_region_copy_targets"] = (
            capo_dlm.types.cross_region_copy_target_list.deserialize_json(
                data["CrossRegionCopyTargets"]
            )
        )
    if "Exclusions" in data:
        import capo_dlm.types.exclusions

        out["exclusions"] = capo_dlm.types.exclusions.deserialize_json(
            data["Exclusions"]
        )
    return out
