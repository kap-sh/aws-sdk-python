"""Generated from Smithy shape ``com.amazonaws.ssm#DescribePatchGroupStateResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.instances_count
    import aws_sdk_ssm.types.integer


class DescribePatchGroupStateResult(TypedDict):
    instances: "aws_sdk_ssm.types.integer.Integer"
    """<p>The number of managed nodes in the patch group.</p>"""
    instances_with_installed_patches: "aws_sdk_ssm.types.integer.Integer"
    """<p>The number of managed nodes with installed patches.</p>"""
    instances_with_installed_other_patches: "aws_sdk_ssm.types.integer.Integer"
    """<p>The number of managed nodes with patches installed that aren't defined in the patch baseline.</p>"""
    instances_with_installed_pending_reboot_patches: NotRequired[
        "aws_sdk_ssm.types.instances_count.InstancesCount"
    ]
    """<p>The number of managed nodes with patches installed by Patch Manager that haven't been rebooted after the patch installation. The status of these managed nodes is <code>NON_COMPLIANT</code>.</p>"""
    instances_with_installed_rejected_patches: NotRequired[
        "aws_sdk_ssm.types.instances_count.InstancesCount"
    ]
    """<p>The number of managed nodes with patches installed that are specified in a <code>RejectedPatches</code> list. Patches with a status of <code>INSTALLED_REJECTED</code> were typically installed before they were added to a <code>RejectedPatches</code> list.</p> <note> <p>If <code>ALLOW_AS_DEPENDENCY</code> is the specified option for <code>RejectedPatchesAction</code>, the value of <code>InstancesWithInstalledRejectedPatches</code> will always be <code>0</code> (zero).</p> </note>"""
    instances_with_missing_patches: "aws_sdk_ssm.types.integer.Integer"
    """<p>The number of managed nodes with missing patches from the patch baseline.</p>"""
    instances_with_failed_patches: "aws_sdk_ssm.types.integer.Integer"
    """<p>The number of managed nodes with patches from the patch baseline that failed to install.</p>"""
    instances_with_not_applicable_patches: "aws_sdk_ssm.types.integer.Integer"
    """<p>The number of managed nodes with patches that aren't applicable.</p>"""
    instances_with_unreported_not_applicable_patches: NotRequired[
        "aws_sdk_ssm.types.integer.Integer"
    ]
    """<p>The number of managed nodes with <code>NotApplicable</code> patches beyond the supported limit, which aren't reported by name to Inventory. Inventory is a tool in Amazon Web Services Systems Manager.</p>"""
    instances_with_critical_non_compliant_patches: NotRequired[
        "aws_sdk_ssm.types.instances_count.InstancesCount"
    ]
    """<p>The number of managed nodes where patches that are specified as <code>Critical</code> for compliance reporting in the patch baseline aren't installed. These patches might be missing, have failed installation, were rejected, or were installed but awaiting a required managed node reboot. The status of these managed nodes is <code>NON_COMPLIANT</code>.</p>"""
    instances_with_security_non_compliant_patches: NotRequired[
        "aws_sdk_ssm.types.instances_count.InstancesCount"
    ]
    """<p>The number of managed nodes where patches that are specified as <code>Security</code> in a patch advisory aren't installed. These patches might be missing, have failed installation, were rejected, or were installed but awaiting a required managed node reboot. The status of these managed nodes is <code>NON_COMPLIANT</code>.</p>"""
    instances_with_other_non_compliant_patches: NotRequired[
        "aws_sdk_ssm.types.instances_count.InstancesCount"
    ]
    """<p>The number of managed nodes with patches installed that are specified as other than <code>Critical</code> or <code>Security</code> but aren't compliant with the patch baseline. The status of these managed nodes is <code>NON_COMPLIANT</code>.</p>"""
    instances_with_available_security_updates: NotRequired[
        "aws_sdk_ssm.types.integer.Integer"
    ]
    """<p>The number of managed nodes for which security-related patches are available but not approved because because they didn't meet the patch baseline requirements. For example, an updated version of a patch might have been released before the specified auto-approval period was over.</p> <p>Applies to Windows Server managed nodes only.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePatchGroupStateResult) -> dict:
    out: dict = {}
    out["Instances"] = value.get("instances", 0)
    out["InstancesWithInstalledPatches"] = value.get(
        "instances_with_installed_patches", 0
    )
    out["InstancesWithInstalledOtherPatches"] = value.get(
        "instances_with_installed_other_patches", 0
    )
    if "instances_with_installed_pending_reboot_patches" in value:
        out["InstancesWithInstalledPendingRebootPatches"] = value[
            "instances_with_installed_pending_reboot_patches"
        ]
    if "instances_with_installed_rejected_patches" in value:
        out["InstancesWithInstalledRejectedPatches"] = value[
            "instances_with_installed_rejected_patches"
        ]
    out["InstancesWithMissingPatches"] = value.get("instances_with_missing_patches", 0)
    out["InstancesWithFailedPatches"] = value.get("instances_with_failed_patches", 0)
    out["InstancesWithNotApplicablePatches"] = value.get(
        "instances_with_not_applicable_patches", 0
    )
    if "instances_with_unreported_not_applicable_patches" in value:
        out["InstancesWithUnreportedNotApplicablePatches"] = value[
            "instances_with_unreported_not_applicable_patches"
        ]
    if "instances_with_critical_non_compliant_patches" in value:
        out["InstancesWithCriticalNonCompliantPatches"] = value[
            "instances_with_critical_non_compliant_patches"
        ]
    if "instances_with_security_non_compliant_patches" in value:
        out["InstancesWithSecurityNonCompliantPatches"] = value[
            "instances_with_security_non_compliant_patches"
        ]
    if "instances_with_other_non_compliant_patches" in value:
        out["InstancesWithOtherNonCompliantPatches"] = value[
            "instances_with_other_non_compliant_patches"
        ]
    if "instances_with_available_security_updates" in value:
        out["InstancesWithAvailableSecurityUpdates"] = value[
            "instances_with_available_security_updates"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePatchGroupStateResult:
    out: DescribePatchGroupStateResult = {}  # type: ignore[typeddict-item]
    if "Instances" in data:
        out["instances"] = data["Instances"]
    else:
        out["instances"] = 0
    if "InstancesWithInstalledPatches" in data:
        out["instances_with_installed_patches"] = data["InstancesWithInstalledPatches"]
    else:
        out["instances_with_installed_patches"] = 0
    if "InstancesWithInstalledOtherPatches" in data:
        out["instances_with_installed_other_patches"] = data[
            "InstancesWithInstalledOtherPatches"
        ]
    else:
        out["instances_with_installed_other_patches"] = 0
    if "InstancesWithInstalledPendingRebootPatches" in data:
        out["instances_with_installed_pending_reboot_patches"] = data[
            "InstancesWithInstalledPendingRebootPatches"
        ]
    if "InstancesWithInstalledRejectedPatches" in data:
        out["instances_with_installed_rejected_patches"] = data[
            "InstancesWithInstalledRejectedPatches"
        ]
    if "InstancesWithMissingPatches" in data:
        out["instances_with_missing_patches"] = data["InstancesWithMissingPatches"]
    else:
        out["instances_with_missing_patches"] = 0
    if "InstancesWithFailedPatches" in data:
        out["instances_with_failed_patches"] = data["InstancesWithFailedPatches"]
    else:
        out["instances_with_failed_patches"] = 0
    if "InstancesWithNotApplicablePatches" in data:
        out["instances_with_not_applicable_patches"] = data[
            "InstancesWithNotApplicablePatches"
        ]
    else:
        out["instances_with_not_applicable_patches"] = 0
    if "InstancesWithUnreportedNotApplicablePatches" in data:
        out["instances_with_unreported_not_applicable_patches"] = data[
            "InstancesWithUnreportedNotApplicablePatches"
        ]
    if "InstancesWithCriticalNonCompliantPatches" in data:
        out["instances_with_critical_non_compliant_patches"] = data[
            "InstancesWithCriticalNonCompliantPatches"
        ]
    if "InstancesWithSecurityNonCompliantPatches" in data:
        out["instances_with_security_non_compliant_patches"] = data[
            "InstancesWithSecurityNonCompliantPatches"
        ]
    if "InstancesWithOtherNonCompliantPatches" in data:
        out["instances_with_other_non_compliant_patches"] = data[
            "InstancesWithOtherNonCompliantPatches"
        ]
    if "InstancesWithAvailableSecurityUpdates" in data:
        out["instances_with_available_security_updates"] = data[
            "InstancesWithAvailableSecurityUpdates"
        ]
    return out
