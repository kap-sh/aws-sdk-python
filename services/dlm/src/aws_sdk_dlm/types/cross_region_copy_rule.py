"""Generated from Smithy shape ``com.amazonaws.dlm#CrossRegionCopyRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dlm.types.cmk_arn
    import aws_sdk_dlm.types.copy_tags_nullable
    import aws_sdk_dlm.types.cross_region_copy_deprecate_rule
    import aws_sdk_dlm.types.cross_region_copy_retain_rule
    import aws_sdk_dlm.types.encrypted
    import aws_sdk_dlm.types.target
    import aws_sdk_dlm.types.target_region


class CrossRegionCopyRule(TypedDict, closed=True):
    target_region: NotRequired["aws_sdk_dlm.types.target_region.TargetRegion"]
    """<note> <p>Use this parameter for AMI policies only. For snapshot policies, use <b>Target</b> instead. For snapshot policies created before the <b>Target</b> parameter was introduced, this parameter indicates the target Region for snapshot copies.</p> <p></p> </note> <p> <b>[Custom AMI policies only]</b> The target Region or the Amazon Resource Name (ARN) of the target Outpost for the snapshot copies.</p>"""
    target: NotRequired["aws_sdk_dlm.types.target.Target"]
    """<note> <p>Use this parameter for snapshot policies only. For AMI policies, use <b>TargetRegion</b> instead.</p> </note> <p> <b>[Custom snapshot policies only]</b> The target Region or the Amazon Resource Name (ARN) of the target Outpost for the snapshot copies.</p>"""
    encrypted: NotRequired["aws_sdk_dlm.types.encrypted.Encrypted"]
    """<p>To encrypt a copy of an unencrypted snapshot if encryption by default is not enabled, enable encryption using this parameter. Copies of encrypted snapshots are encrypted, even if this parameter is false or if encryption by default is not enabled.</p>"""
    cmk_arn: NotRequired["aws_sdk_dlm.types.cmk_arn.CmkArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key to use for EBS encryption. If this parameter is not specified, the default KMS key for the account is used.</p>"""
    copy_tags: NotRequired["aws_sdk_dlm.types.copy_tags_nullable.CopyTagsNullable"]
    """<p>Indicates whether to copy all user-defined tags from the source snapshot or AMI to the cross-Region copy.</p>"""
    retain_rule: NotRequired[
        "aws_sdk_dlm.types.cross_region_copy_retain_rule.CrossRegionCopyRetainRule"
    ]
    """<p>The retention rule that indicates how long the cross-Region snapshot or AMI copies are to be retained in the destination Region.</p>"""
    deprecate_rule: NotRequired[
        "aws_sdk_dlm.types.cross_region_copy_deprecate_rule.CrossRegionCopyDeprecateRule"
    ]
    """<p> <b>[Custom AMI policies only]</b> The AMI deprecation rule for cross-Region AMI copies created by the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CrossRegionCopyRule) -> dict:
    out: dict = {}
    if "target_region" in value:
        out["TargetRegion"] = value["target_region"]
    if "target" in value:
        out["Target"] = value["target"]
    if "encrypted" in value:
        out["Encrypted"] = value["encrypted"]
    if "cmk_arn" in value:
        out["CmkArn"] = value["cmk_arn"]
    if "copy_tags" in value:
        out["CopyTags"] = value["copy_tags"]
    if "retain_rule" in value:
        import aws_sdk_dlm.types.cross_region_copy_retain_rule

        out["RetainRule"] = (
            aws_sdk_dlm.types.cross_region_copy_retain_rule.serialize_json(
                value["retain_rule"]
            )
        )
    if "deprecate_rule" in value:
        import aws_sdk_dlm.types.cross_region_copy_deprecate_rule

        out["DeprecateRule"] = (
            aws_sdk_dlm.types.cross_region_copy_deprecate_rule.serialize_json(
                value["deprecate_rule"]
            )
        )
    return out


def deserialize_json(data: dict) -> CrossRegionCopyRule:
    out: CrossRegionCopyRule = {}  # type: ignore[typeddict-item]
    if "TargetRegion" in data:
        out["target_region"] = data["TargetRegion"]
    if "Target" in data:
        out["target"] = data["Target"]
    if "Encrypted" in data:
        out["encrypted"] = data["Encrypted"]
    if "CmkArn" in data:
        out["cmk_arn"] = data["CmkArn"]
    if "CopyTags" in data:
        out["copy_tags"] = data["CopyTags"]
    if "RetainRule" in data:
        import aws_sdk_dlm.types.cross_region_copy_retain_rule

        out["retain_rule"] = (
            aws_sdk_dlm.types.cross_region_copy_retain_rule.deserialize_json(
                data["RetainRule"]
            )
        )
    if "DeprecateRule" in data:
        import aws_sdk_dlm.types.cross_region_copy_deprecate_rule

        out["deprecate_rule"] = (
            aws_sdk_dlm.types.cross_region_copy_deprecate_rule.deserialize_json(
                data["DeprecateRule"]
            )
        )
    return out
