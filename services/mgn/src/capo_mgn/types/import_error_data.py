"""Generated from Smithy shape ``com.amazonaws.mgn#ImportErrorData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.application_id
    import capo_mgn.types.bounded_string
    import capo_mgn.types.large_bounded_string
    import capo_mgn.types.positive_integer
    import capo_mgn.types.source_server_id
    import capo_mgn.types.wave_id


class ImportErrorData(TypedDict, closed=True):
    source_server_id: NotRequired["capo_mgn.types.source_server_id.SourceServerID"]
    """<p>Import error data source server ID.</p>"""
    application_id: NotRequired["capo_mgn.types.application_id.ApplicationID"]
    """<p>Import error data application ID.</p>"""
    wave_id: NotRequired["capo_mgn.types.wave_id.WaveID"]
    """<p>Import error data wave id.</p>"""
    ec2_launch_template_id: NotRequired["capo_mgn.types.bounded_string.BoundedString"]
    """<p>Import error data ec2 LaunchTemplate ID.</p>"""
    row_number: "capo_mgn.types.positive_integer.PositiveInteger"
    """<p>Import error data row number.</p>"""
    raw_error: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    """<p>Import error data raw error.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Import error data source account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportErrorData) -> dict:
    out: dict = {}
    if "source_server_id" in value:
        out["sourceServerID"] = value["source_server_id"]
    if "application_id" in value:
        out["applicationID"] = value["application_id"]
    if "wave_id" in value:
        out["waveID"] = value["wave_id"]
    if "ec2_launch_template_id" in value:
        out["ec2LaunchTemplateID"] = value["ec2_launch_template_id"]
    out["rowNumber"] = value.get("row_number", 0)
    if "raw_error" in value:
        out["rawError"] = value["raw_error"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> ImportErrorData:
    out: ImportErrorData = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    if "applicationID" in data:
        out["application_id"] = data["applicationID"]
    if "waveID" in data:
        out["wave_id"] = data["waveID"]
    if "ec2LaunchTemplateID" in data:
        out["ec2_launch_template_id"] = data["ec2LaunchTemplateID"]
    if "rowNumber" in data:
        out["row_number"] = data["rowNumber"]
    else:
        out["row_number"] = 0
    if "rawError" in data:
        out["raw_error"] = data["rawError"]
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
