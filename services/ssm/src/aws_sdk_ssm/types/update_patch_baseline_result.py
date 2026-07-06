"""Generated from Smithy shape ``com.amazonaws.ssm#UpdatePatchBaselineResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.baseline_description
    import aws_sdk_ssm.types.baseline_id
    import aws_sdk_ssm.types.baseline_name
    import aws_sdk_ssm.types.boolean
    import aws_sdk_ssm.types.date_time
    import aws_sdk_ssm.types.operating_system
    import aws_sdk_ssm.types.patch_action
    import aws_sdk_ssm.types.patch_compliance_level
    import aws_sdk_ssm.types.patch_compliance_status
    import aws_sdk_ssm.types.patch_filter_group
    import aws_sdk_ssm.types.patch_id_list
    import aws_sdk_ssm.types.patch_rule_group
    import aws_sdk_ssm.types.patch_source_list


class UpdatePatchBaselineResult(TypedDict, closed=True):
    baseline_id: NotRequired["aws_sdk_ssm.types.baseline_id.BaselineId"]
    """<p>The ID of the deleted patch baseline.</p>"""
    name: NotRequired["aws_sdk_ssm.types.baseline_name.BaselineName"]
    """<p>The name of the patch baseline.</p>"""
    operating_system: NotRequired["aws_sdk_ssm.types.operating_system.OperatingSystem"]
    """<p>The operating system rule used by the updated patch baseline.</p>"""
    global_filters: NotRequired["aws_sdk_ssm.types.patch_filter_group.PatchFilterGroup"]
    """<p>A set of global filters used to exclude patches from the baseline.</p>"""
    approval_rules: NotRequired["aws_sdk_ssm.types.patch_rule_group.PatchRuleGroup"]
    """<p>A set of rules used to include patches in the baseline.</p>"""
    approved_patches: NotRequired["aws_sdk_ssm.types.patch_id_list.PatchIdList"]
    """<p>A list of explicitly approved patches for the baseline.</p>"""
    approved_patches_compliance_level: NotRequired[
        "aws_sdk_ssm.types.patch_compliance_level.PatchComplianceLevel"
    ]
    """<p>The compliance severity level assigned to the patch baseline after the update completed.</p>"""
    approved_patches_enable_non_security: NotRequired[
        "aws_sdk_ssm.types.boolean.Boolean"
    ]
    """<p>Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is <code>false</code>. Applies to Linux managed nodes only.</p>"""
    rejected_patches: NotRequired["aws_sdk_ssm.types.patch_id_list.PatchIdList"]
    """<p>A list of explicitly rejected patches for the baseline.</p>"""
    rejected_patches_action: NotRequired["aws_sdk_ssm.types.patch_action.PatchAction"]
    """<p>The action specified to take on patches included in the <code>RejectedPatches</code> list. A patch can be allowed only if it is a dependency of another package, or blocked entirely along with packages that include it as a dependency.</p>"""
    created_date: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The date when the patch baseline was created.</p>"""
    modified_date: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The date when the patch baseline was last modified.</p>"""
    description: NotRequired[
        "aws_sdk_ssm.types.baseline_description.BaselineDescription"
    ]
    """<p>A description of the patch baseline.</p>"""
    sources: NotRequired["aws_sdk_ssm.types.patch_source_list.PatchSourceList"]
    """<p>Information about the patches to use to update the managed nodes, including target operating systems and source repositories. Applies to Linux managed nodes only.</p>"""
    available_security_updates_compliance_status: NotRequired[
        "aws_sdk_ssm.types.patch_compliance_status.PatchComplianceStatus"
    ]
    """<p>Indicates the compliance status of managed nodes for which security-related patches are available but were not approved. This preference is specified when the <code>CreatePatchBaseline</code> or <code>UpdatePatchBaseline</code> commands are run.</p> <p>Applies to Windows Server managed nodes only.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePatchBaselineResult) -> dict:
    out: dict = {}
    if "baseline_id" in value:
        out["BaselineId"] = value["baseline_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "operating_system" in value:
        import aws_sdk_ssm.types.operating_system

        out["OperatingSystem"] = (
            aws_sdk_ssm.types.operating_system.serialize_aws_json_1_1(
                value["operating_system"]
            )
        )
    if "global_filters" in value:
        import aws_sdk_ssm.types.patch_filter_group

        out["GlobalFilters"] = (
            aws_sdk_ssm.types.patch_filter_group.serialize_aws_json_1_1(
                value["global_filters"]
            )
        )
    if "approval_rules" in value:
        import aws_sdk_ssm.types.patch_rule_group

        out["ApprovalRules"] = (
            aws_sdk_ssm.types.patch_rule_group.serialize_aws_json_1_1(
                value["approval_rules"]
            )
        )
    if "approved_patches" in value:
        import aws_sdk_ssm.types.patch_id_list

        out["ApprovedPatches"] = aws_sdk_ssm.types.patch_id_list.serialize_aws_json_1_1(
            value["approved_patches"]
        )
    if "approved_patches_compliance_level" in value:
        import aws_sdk_ssm.types.patch_compliance_level

        out["ApprovedPatchesComplianceLevel"] = (
            aws_sdk_ssm.types.patch_compliance_level.serialize_aws_json_1_1(
                value["approved_patches_compliance_level"]
            )
        )
    if "approved_patches_enable_non_security" in value:
        out["ApprovedPatchesEnableNonSecurity"] = value[
            "approved_patches_enable_non_security"
        ]
    if "rejected_patches" in value:
        import aws_sdk_ssm.types.patch_id_list

        out["RejectedPatches"] = aws_sdk_ssm.types.patch_id_list.serialize_aws_json_1_1(
            value["rejected_patches"]
        )
    if "rejected_patches_action" in value:
        import aws_sdk_ssm.types.patch_action

        out["RejectedPatchesAction"] = (
            aws_sdk_ssm.types.patch_action.serialize_aws_json_1_1(
                value["rejected_patches_action"]
            )
        )
    if "created_date" in value:
        import aws_sdk_ssm.types.date_time

        out["CreatedDate"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["created_date"]
        )
    if "modified_date" in value:
        import aws_sdk_ssm.types.date_time

        out["ModifiedDate"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["modified_date"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "sources" in value:
        import aws_sdk_ssm.types.patch_source_list

        out["Sources"] = aws_sdk_ssm.types.patch_source_list.serialize_aws_json_1_1(
            value["sources"]
        )
    if "available_security_updates_compliance_status" in value:
        import aws_sdk_ssm.types.patch_compliance_status

        out["AvailableSecurityUpdatesComplianceStatus"] = (
            aws_sdk_ssm.types.patch_compliance_status.serialize_aws_json_1_1(
                value["available_security_updates_compliance_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePatchBaselineResult:
    out: UpdatePatchBaselineResult = {}  # type: ignore[typeddict-item]
    if "BaselineId" in data:
        out["baseline_id"] = data["BaselineId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "OperatingSystem" in data:
        import aws_sdk_ssm.types.operating_system

        out["operating_system"] = (
            aws_sdk_ssm.types.operating_system.deserialize_aws_json_1_1(
                data["OperatingSystem"]
            )
        )
    if "GlobalFilters" in data:
        import aws_sdk_ssm.types.patch_filter_group

        out["global_filters"] = (
            aws_sdk_ssm.types.patch_filter_group.deserialize_aws_json_1_1(
                data["GlobalFilters"]
            )
        )
    if "ApprovalRules" in data:
        import aws_sdk_ssm.types.patch_rule_group

        out["approval_rules"] = (
            aws_sdk_ssm.types.patch_rule_group.deserialize_aws_json_1_1(
                data["ApprovalRules"]
            )
        )
    if "ApprovedPatches" in data:
        import aws_sdk_ssm.types.patch_id_list

        out["approved_patches"] = (
            aws_sdk_ssm.types.patch_id_list.deserialize_aws_json_1_1(
                data["ApprovedPatches"]
            )
        )
    if "ApprovedPatchesComplianceLevel" in data:
        import aws_sdk_ssm.types.patch_compliance_level

        out["approved_patches_compliance_level"] = (
            aws_sdk_ssm.types.patch_compliance_level.deserialize_aws_json_1_1(
                data["ApprovedPatchesComplianceLevel"]
            )
        )
    if "ApprovedPatchesEnableNonSecurity" in data:
        out["approved_patches_enable_non_security"] = data[
            "ApprovedPatchesEnableNonSecurity"
        ]
    if "RejectedPatches" in data:
        import aws_sdk_ssm.types.patch_id_list

        out["rejected_patches"] = (
            aws_sdk_ssm.types.patch_id_list.deserialize_aws_json_1_1(
                data["RejectedPatches"]
            )
        )
    if "RejectedPatchesAction" in data:
        import aws_sdk_ssm.types.patch_action

        out["rejected_patches_action"] = (
            aws_sdk_ssm.types.patch_action.deserialize_aws_json_1_1(
                data["RejectedPatchesAction"]
            )
        )
    if "CreatedDate" in data:
        import aws_sdk_ssm.types.date_time

        out["created_date"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreatedDate"]
        )
    if "ModifiedDate" in data:
        import aws_sdk_ssm.types.date_time

        out["modified_date"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ModifiedDate"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Sources" in data:
        import aws_sdk_ssm.types.patch_source_list

        out["sources"] = aws_sdk_ssm.types.patch_source_list.deserialize_aws_json_1_1(
            data["Sources"]
        )
    if "AvailableSecurityUpdatesComplianceStatus" in data:
        import aws_sdk_ssm.types.patch_compliance_status

        out["available_security_updates_compliance_status"] = (
            aws_sdk_ssm.types.patch_compliance_status.deserialize_aws_json_1_1(
                data["AvailableSecurityUpdatesComplianceStatus"]
            )
        )
    return out
