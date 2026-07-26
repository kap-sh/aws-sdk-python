"""Generated from Smithy shape ``com.amazonaws.drs#StagingArea``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.account_id
    import capo_drs.types.arn
    import capo_drs.types.extension_status
    import capo_drs.types.large_bounded_string


class StagingArea(TypedDict, closed=True):
    status: NotRequired["capo_drs.types.extension_status.ExtensionStatus"]
    """<p>Status of Source server extension. Possible values: (a) NOT_EXTENDED - This is a source server that is replicating in the current account. (b) EXTENDED - Source server is extended from a staging source server. In this case, the value of stagingSourceServerArn is pointing to the Arn of the source server in the staging account. (c) EXTENSION_ERROR - Some issue occurred when accessing staging source server. In this case, errorMessage field will contain an error message that explains what happened.</p>"""
    staging_account_id: NotRequired["capo_drs.types.account_id.AccountID"]
    """<p>Account ID of the account to which source server belongs. If this source server is extended - shows Account ID of staging source server.</p>"""
    staging_source_server_arn: NotRequired["capo_drs.types.arn.ARN"]
    """<p>Arn of the staging source server if this source server is extended</p>"""
    error_message: NotRequired["capo_drs.types.large_bounded_string.LargeBoundedString"]
    """<p>Shows an error message that occurred when DRS tried to access the staging source server. In this case StagingArea$status will have value EXTENSION_ERROR</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StagingArea) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "staging_account_id" in value:
        out["stagingAccountID"] = value["staging_account_id"]
    if "staging_source_server_arn" in value:
        out["stagingSourceServerArn"] = value["staging_source_server_arn"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> StagingArea:
    out: StagingArea = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "stagingAccountID" in data:
        out["staging_account_id"] = data["stagingAccountID"]
    if "stagingSourceServerArn" in data:
        out["staging_source_server_arn"] = data["stagingSourceServerArn"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
