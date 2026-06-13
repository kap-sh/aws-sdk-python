"""Generated from Smithy shape ``com.amazonaws.backup#ReportSetting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup.types.integer
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.string_list


class ReportSetting(TypedDict):
    report_template: "aws_sdk_backup.types.string.string"
    """<p>Identifies the report template for the report. Reports are built using a report template. The report templates are:</p> <p> <code>RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT | SCAN_JOB_REPORT</code> </p>"""
    framework_arns: NotRequired["aws_sdk_backup.types.string_list.stringList"]
    """<p>The Amazon Resource Names (ARNs) of the frameworks a report covers.</p>"""
    number_of_frameworks: "aws_sdk_backup.types.integer.integer"
    """<p>The number of frameworks a report covers.</p>"""
    accounts: NotRequired["aws_sdk_backup.types.string_list.stringList"]
    """<p>These are the accounts to be included in the report.</p> <p>Use string value of <code>ROOT</code> to include all organizational units.</p>"""
    organization_units: NotRequired["aws_sdk_backup.types.string_list.stringList"]
    """<p>These are the Organizational Units to be included in the report.</p>"""
    regions: NotRequired["aws_sdk_backup.types.string_list.stringList"]
    """<p>These are the Regions to be included in the report.</p> <p>Use the wildcard as the string value to include all Regions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportSetting) -> dict:
    out: dict = {}
    out["ReportTemplate"] = value["report_template"]
    if "framework_arns" in value:
        import aws_sdk_backup.types.string_list

        out["FrameworkArns"] = aws_sdk_backup.types.string_list.serialize_json(
            value["framework_arns"]
        )
    out["NumberOfFrameworks"] = value.get("number_of_frameworks", 0)
    if "accounts" in value:
        import aws_sdk_backup.types.string_list

        out["Accounts"] = aws_sdk_backup.types.string_list.serialize_json(
            value["accounts"]
        )
    if "organization_units" in value:
        import aws_sdk_backup.types.string_list

        out["OrganizationUnits"] = aws_sdk_backup.types.string_list.serialize_json(
            value["organization_units"]
        )
    if "regions" in value:
        import aws_sdk_backup.types.string_list

        out["Regions"] = aws_sdk_backup.types.string_list.serialize_json(
            value["regions"]
        )
    return out


def deserialize_json(data: dict) -> ReportSetting:
    out: ReportSetting = {}  # type: ignore[typeddict-item]
    if "ReportTemplate" in data:
        out["report_template"] = data["ReportTemplate"]
    else:
        raise DeserializationError("ReportSetting.report_template required")
    if "FrameworkArns" in data:
        import aws_sdk_backup.types.string_list

        out["framework_arns"] = aws_sdk_backup.types.string_list.deserialize_json(
            data["FrameworkArns"]
        )
    if "NumberOfFrameworks" in data:
        out["number_of_frameworks"] = data["NumberOfFrameworks"]
    else:
        out["number_of_frameworks"] = 0
    if "Accounts" in data:
        import aws_sdk_backup.types.string_list

        out["accounts"] = aws_sdk_backup.types.string_list.deserialize_json(
            data["Accounts"]
        )
    if "OrganizationUnits" in data:
        import aws_sdk_backup.types.string_list

        out["organization_units"] = aws_sdk_backup.types.string_list.deserialize_json(
            data["OrganizationUnits"]
        )
    if "Regions" in data:
        import aws_sdk_backup.types.string_list

        out["regions"] = aws_sdk_backup.types.string_list.deserialize_json(
            data["Regions"]
        )
    return out
