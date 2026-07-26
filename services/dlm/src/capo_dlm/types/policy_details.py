"""Generated from Smithy shape ``com.amazonaws.dlm#PolicyDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dlm.types.action_list
    import capo_dlm.types.copy_tags_nullable
    import capo_dlm.types.create_interval
    import capo_dlm.types.cross_region_copy_target_list
    import capo_dlm.types.event_source
    import capo_dlm.types.exclusions
    import capo_dlm.types.extend_deletion
    import capo_dlm.types.parameters
    import capo_dlm.types.policy_language_values
    import capo_dlm.types.policy_type_values
    import capo_dlm.types.resource_location_list
    import capo_dlm.types.resource_type_values
    import capo_dlm.types.resource_type_values_list
    import capo_dlm.types.retain_interval
    import capo_dlm.types.schedule_list
    import capo_dlm.types.target_tag_list


class PolicyDetails(TypedDict, closed=True):
    policy_type: NotRequired["capo_dlm.types.policy_type_values.PolicyTypeValues"]
    """<p>The type of policy. Specify <code>EBS_SNAPSHOT_MANAGEMENT</code> to create a lifecycle policy that manages the lifecycle of Amazon EBS snapshots. Specify <code>IMAGE_MANAGEMENT</code> to create a lifecycle policy that manages the lifecycle of EBS-backed AMIs. Specify <code>EVENT_BASED_POLICY </code> to create an event-based policy that performs specific actions when a defined event occurs in your Amazon Web Services account.</p> <p>The default is <code>EBS_SNAPSHOT_MANAGEMENT</code>.</p>"""
    resource_types: NotRequired[
        "capo_dlm.types.resource_type_values_list.ResourceTypeValuesList"
    ]
    """<p> <b>[Custom snapshot policies only]</b> The target resource type for snapshot and AMI lifecycle policies. Use <code>VOLUME </code>to create snapshots of individual volumes or use <code>INSTANCE</code> to create multi-volume snapshots from the volumes for an instance.</p>"""
    resource_locations: NotRequired[
        "capo_dlm.types.resource_location_list.ResourceLocationList"
    ]
    """<p> <b>[Custom snapshot and AMI policies only]</b> The location of the resources to backup.</p> <ul> <li> <p>If the source resources are located in a Region, specify <code>CLOUD</code>. In this case, the policy targets all resources of the specified type with matching target tags across all Availability Zones in the Region.</p> </li> <li> <p> <b>[Custom snapshot policies only]</b> If the source resources are located in a Local Zone, specify <code>LOCAL_ZONE</code>. In this case, the policy targets all resources of the specified type with matching target tags across all Local Zones in the Region.</p> </li> <li> <p>If the source resources are located on an Outpost in your account, specify <code>OUTPOST</code>. In this case, the policy targets all resources of the specified type with matching target tags across all of the Outposts in your account.</p> </li> </ul> <p></p>"""
    target_tags: NotRequired["capo_dlm.types.target_tag_list.TargetTagList"]
    """<p> <b>[Custom snapshot and AMI policies only]</b> The single tag that identifies targeted resources for this policy.</p>"""
    schedules: NotRequired["capo_dlm.types.schedule_list.ScheduleList"]
    """<p> <b>[Custom snapshot and AMI policies only]</b> The schedules of policy-defined actions for snapshot and AMI lifecycle policies. A policy can have up to four schedules—one mandatory schedule and up to three optional schedules.</p>"""
    parameters: NotRequired["capo_dlm.types.parameters.Parameters"]
    """<p> <b>[Custom snapshot and AMI policies only]</b> A set of optional parameters for snapshot and AMI lifecycle policies. </p> <note> <p>If you are modifying a policy that was created or previously modified using the Amazon Data Lifecycle Manager console, then you must include this parameter and specify either the default values or the new values that you require. You can't omit this parameter or set its values to null.</p> </note>"""
    event_source: NotRequired["capo_dlm.types.event_source.EventSource"]
    """<p> <b>[Event-based policies only]</b> The event that activates the event-based policy.</p>"""
    actions: NotRequired["capo_dlm.types.action_list.ActionList"]
    """<p> <b>[Event-based policies only]</b> The actions to be performed when the event-based policy is activated. You can specify only one action per policy.</p>"""
    policy_language: NotRequired[
        "capo_dlm.types.policy_language_values.PolicyLanguageValues"
    ]
    """<p>The type of policy to create. Specify one of the following:</p> <ul> <li> <p> <code>SIMPLIFIED</code> To create a default policy.</p> </li> <li> <p> <code>STANDARD</code> To create a custom policy.</p> </li> </ul>"""
    resource_type: NotRequired["capo_dlm.types.resource_type_values.ResourceTypeValues"]
    """<p> <b>[Default policies only]</b> Specify the type of default policy to create.</p> <ul> <li> <p>To create a default policy for EBS snapshots, that creates snapshots of all volumes in the Region that do not have recent backups, specify <code>VOLUME</code>.</p> </li> <li> <p>To create a default policy for EBS-backed AMIs, that creates EBS-backed AMIs from all instances in the Region that do not have recent backups, specify <code>INSTANCE</code>.</p> </li> </ul>"""
    create_interval: NotRequired["capo_dlm.types.create_interval.CreateInterval"]
    """<p> <b>[Default policies only]</b> Specifies how often the policy should run and create snapshots or AMIs. The creation frequency can range from 1 to 7 days. If you do not specify a value, the default is 1.</p> <p>Default: 1</p>"""
    retain_interval: NotRequired["capo_dlm.types.retain_interval.RetainInterval"]
    """<p> <b>[Default policies only]</b> Specifies how long the policy should retain snapshots or AMIs before deleting them. The retention period can range from 2 to 14 days, but it must be greater than the creation frequency to ensure that the policy retains at least 1 snapshot or AMI at any given time. If you do not specify a value, the default is 7.</p> <p>Default: 7</p>"""
    copy_tags: NotRequired["capo_dlm.types.copy_tags_nullable.CopyTagsNullable"]
    """<p> <b>[Default policies only]</b> Indicates whether the policy should copy tags from the source resource to the snapshot or AMI. If you do not specify a value, the default is <code>false</code>.</p> <p>Default: false</p>"""
    cross_region_copy_targets: NotRequired[
        "capo_dlm.types.cross_region_copy_target_list.CrossRegionCopyTargetList"
    ]
    """<p> <b>[Default policies only]</b> Specifies destination Regions for snapshot or AMI copies. You can specify up to 3 destination Regions. If you do not want to create cross-Region copies, omit this parameter.</p>"""
    extend_deletion: NotRequired["capo_dlm.types.extend_deletion.ExtendDeletion"]
    """<p> <b>[Default policies only]</b> Defines the snapshot or AMI retention behavior for the policy if the source volume or instance is deleted, or if the policy enters the error, disabled, or deleted state.</p> <p>By default (<b>ExtendDeletion=false</b>):</p> <ul> <li> <p>If a source resource is deleted, Amazon Data Lifecycle Manager will continue to delete previously created snapshots or AMIs, up to but not including the last one, based on the specified retention period. If you want Amazon Data Lifecycle Manager to delete all snapshots or AMIs, including the last one, specify <code>true</code>.</p> </li> <li> <p>If a policy enters the error, disabled, or deleted state, Amazon Data Lifecycle Manager stops deleting snapshots and AMIs. If you want Amazon Data Lifecycle Manager to continue deleting snapshots or AMIs, including the last one, if the policy enters one of these states, specify <code>true</code>.</p> </li> </ul> <p>If you enable extended deletion (<b>ExtendDeletion=true</b>), you override both default behaviors simultaneously.</p> <p>If you do not specify a value, the default is <code>false</code>.</p> <p>Default: false</p>"""
    exclusions: NotRequired["capo_dlm.types.exclusions.Exclusions"]
    """<p> <b>[Default policies only]</b> Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs. The policy will not create snapshots or AMIs for target resources that match any of the specified exclusion parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyDetails) -> dict:
    out: dict = {}
    if "policy_type" in value:
        import capo_dlm.types.policy_type_values

        out["PolicyType"] = capo_dlm.types.policy_type_values.serialize_json(
            value["policy_type"]
        )
    if "resource_types" in value:
        import capo_dlm.types.resource_type_values_list

        out["ResourceTypes"] = capo_dlm.types.resource_type_values_list.serialize_json(
            value["resource_types"]
        )
    if "resource_locations" in value:
        import capo_dlm.types.resource_location_list

        out["ResourceLocations"] = capo_dlm.types.resource_location_list.serialize_json(
            value["resource_locations"]
        )
    if "target_tags" in value:
        import capo_dlm.types.target_tag_list

        out["TargetTags"] = capo_dlm.types.target_tag_list.serialize_json(
            value["target_tags"]
        )
    if "schedules" in value:
        import capo_dlm.types.schedule_list

        out["Schedules"] = capo_dlm.types.schedule_list.serialize_json(
            value["schedules"]
        )
    if "parameters" in value:
        import capo_dlm.types.parameters

        out["Parameters"] = capo_dlm.types.parameters.serialize_json(
            value["parameters"]
        )
    if "event_source" in value:
        import capo_dlm.types.event_source

        out["EventSource"] = capo_dlm.types.event_source.serialize_json(
            value["event_source"]
        )
    if "actions" in value:
        import capo_dlm.types.action_list

        out["Actions"] = capo_dlm.types.action_list.serialize_json(value["actions"])
    if "policy_language" in value:
        import capo_dlm.types.policy_language_values

        out["PolicyLanguage"] = capo_dlm.types.policy_language_values.serialize_json(
            value["policy_language"]
        )
    if "resource_type" in value:
        import capo_dlm.types.resource_type_values

        out["ResourceType"] = capo_dlm.types.resource_type_values.serialize_json(
            value["resource_type"]
        )
    if "create_interval" in value:
        out["CreateInterval"] = value["create_interval"]
    if "retain_interval" in value:
        out["RetainInterval"] = value["retain_interval"]
    if "copy_tags" in value:
        out["CopyTags"] = value["copy_tags"]
    if "cross_region_copy_targets" in value:
        import capo_dlm.types.cross_region_copy_target_list

        out["CrossRegionCopyTargets"] = (
            capo_dlm.types.cross_region_copy_target_list.serialize_json(
                value["cross_region_copy_targets"]
            )
        )
    if "extend_deletion" in value:
        out["ExtendDeletion"] = value["extend_deletion"]
    if "exclusions" in value:
        import capo_dlm.types.exclusions

        out["Exclusions"] = capo_dlm.types.exclusions.serialize_json(
            value["exclusions"]
        )
    return out


def deserialize_json(data: dict) -> PolicyDetails:
    out: PolicyDetails = {}  # type: ignore[typeddict-item]
    if "PolicyType" in data:
        import capo_dlm.types.policy_type_values

        out["policy_type"] = capo_dlm.types.policy_type_values.deserialize_json(
            data["PolicyType"]
        )
    if "ResourceTypes" in data:
        import capo_dlm.types.resource_type_values_list

        out["resource_types"] = (
            capo_dlm.types.resource_type_values_list.deserialize_json(
                data["ResourceTypes"]
            )
        )
    if "ResourceLocations" in data:
        import capo_dlm.types.resource_location_list

        out["resource_locations"] = (
            capo_dlm.types.resource_location_list.deserialize_json(
                data["ResourceLocations"]
            )
        )
    if "TargetTags" in data:
        import capo_dlm.types.target_tag_list

        out["target_tags"] = capo_dlm.types.target_tag_list.deserialize_json(
            data["TargetTags"]
        )
    if "Schedules" in data:
        import capo_dlm.types.schedule_list

        out["schedules"] = capo_dlm.types.schedule_list.deserialize_json(
            data["Schedules"]
        )
    if "Parameters" in data:
        import capo_dlm.types.parameters

        out["parameters"] = capo_dlm.types.parameters.deserialize_json(
            data["Parameters"]
        )
    if "EventSource" in data:
        import capo_dlm.types.event_source

        out["event_source"] = capo_dlm.types.event_source.deserialize_json(
            data["EventSource"]
        )
    if "Actions" in data:
        import capo_dlm.types.action_list

        out["actions"] = capo_dlm.types.action_list.deserialize_json(data["Actions"])
    if "PolicyLanguage" in data:
        import capo_dlm.types.policy_language_values

        out["policy_language"] = capo_dlm.types.policy_language_values.deserialize_json(
            data["PolicyLanguage"]
        )
    if "ResourceType" in data:
        import capo_dlm.types.resource_type_values

        out["resource_type"] = capo_dlm.types.resource_type_values.deserialize_json(
            data["ResourceType"]
        )
    if "CreateInterval" in data:
        out["create_interval"] = data["CreateInterval"]
    if "RetainInterval" in data:
        out["retain_interval"] = data["RetainInterval"]
    if "CopyTags" in data:
        out["copy_tags"] = data["CopyTags"]
    if "CrossRegionCopyTargets" in data:
        import capo_dlm.types.cross_region_copy_target_list

        out["cross_region_copy_targets"] = (
            capo_dlm.types.cross_region_copy_target_list.deserialize_json(
                data["CrossRegionCopyTargets"]
            )
        )
    if "ExtendDeletion" in data:
        out["extend_deletion"] = data["ExtendDeletion"]
    if "Exclusions" in data:
        import capo_dlm.types.exclusions

        out["exclusions"] = capo_dlm.types.exclusions.deserialize_json(
            data["Exclusions"]
        )
    return out
