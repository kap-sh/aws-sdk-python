"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateSnaplockConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.autocommit_period
    import aws_sdk_fsx.types.flag
    import aws_sdk_fsx.types.privileged_delete
    import aws_sdk_fsx.types.snaplock_retention_period


class UpdateSnaplockConfiguration(TypedDict, closed=True):
    audit_log_volume: NotRequired["aws_sdk_fsx.types.flag.Flag"]
    r"""<p>Enables or disables the audit log volume for an FSx for ONTAP SnapLock volume. The default value is <code>false</code>. If you set <code>AuditLogVolume</code> to <code>true</code>, the SnapLock volume is created as an audit log volume. The minimum retention period for an audit log volume is six months. </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/how-snaplock-works.html#snaplock-audit-log-volume\"> SnapLock audit log volumes</a>. </p>"""
    autocommit_period: NotRequired[
        "aws_sdk_fsx.types.autocommit_period.AutocommitPeriod"
    ]
    """<p>The configuration object for setting the autocommit period of files in an FSx for ONTAP SnapLock volume. </p>"""
    privileged_delete: NotRequired[
        "aws_sdk_fsx.types.privileged_delete.PrivilegedDelete"
    ]
    r"""<p>Enables, disables, or permanently disables privileged delete on an FSx for ONTAP SnapLock Enterprise volume. Enabling privileged delete allows SnapLock administrators to delete write once, read many (WORM) files even if they have active retention periods. <code>PERMANENTLY_DISABLED</code> is a terminal state. If privileged delete is permanently disabled on a SnapLock volume, you can't re-enable it. The default value is <code>DISABLED</code>. </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-enterprise.html#privileged-delete\">Privileged delete</a>. </p>"""
    retention_period: NotRequired[
        "aws_sdk_fsx.types.snaplock_retention_period.SnaplockRetentionPeriod"
    ]
    """<p>Specifies the retention period of an FSx for ONTAP SnapLock volume. </p>"""
    volume_append_mode_enabled: NotRequired["aws_sdk_fsx.types.flag.Flag"]
    r"""<p>Enables or disables volume-append mode on an FSx for ONTAP SnapLock volume. Volume-append mode allows you to create WORM-appendable files and write data to them incrementally. The default value is <code>false</code>. </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/worm-state.html#worm-state-append\">Volume-append mode</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSnaplockConfiguration) -> dict:
    out: dict = {}
    if "audit_log_volume" in value:
        out["AuditLogVolume"] = value["audit_log_volume"]
    if "autocommit_period" in value:
        import aws_sdk_fsx.types.autocommit_period

        out["AutocommitPeriod"] = (
            aws_sdk_fsx.types.autocommit_period.serialize_aws_json_1_1(
                value["autocommit_period"]
            )
        )
    if "privileged_delete" in value:
        import aws_sdk_fsx.types.privileged_delete

        out["PrivilegedDelete"] = (
            aws_sdk_fsx.types.privileged_delete.serialize_aws_json_1_1(
                value["privileged_delete"]
            )
        )
    if "retention_period" in value:
        import aws_sdk_fsx.types.snaplock_retention_period

        out["RetentionPeriod"] = (
            aws_sdk_fsx.types.snaplock_retention_period.serialize_aws_json_1_1(
                value["retention_period"]
            )
        )
    if "volume_append_mode_enabled" in value:
        out["VolumeAppendModeEnabled"] = value["volume_append_mode_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSnaplockConfiguration:
    out: UpdateSnaplockConfiguration = {}  # type: ignore[typeddict-item]
    if "AuditLogVolume" in data:
        out["audit_log_volume"] = data["AuditLogVolume"]
    if "AutocommitPeriod" in data:
        import aws_sdk_fsx.types.autocommit_period

        out["autocommit_period"] = (
            aws_sdk_fsx.types.autocommit_period.deserialize_aws_json_1_1(
                data["AutocommitPeriod"]
            )
        )
    if "PrivilegedDelete" in data:
        import aws_sdk_fsx.types.privileged_delete

        out["privileged_delete"] = (
            aws_sdk_fsx.types.privileged_delete.deserialize_aws_json_1_1(
                data["PrivilegedDelete"]
            )
        )
    if "RetentionPeriod" in data:
        import aws_sdk_fsx.types.snaplock_retention_period

        out["retention_period"] = (
            aws_sdk_fsx.types.snaplock_retention_period.deserialize_aws_json_1_1(
                data["RetentionPeriod"]
            )
        )
    if "VolumeAppendModeEnabled" in data:
        out["volume_append_mode_enabled"] = data["VolumeAppendModeEnabled"]
    return out
