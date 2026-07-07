"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_error_account_id
    import aws_sdk_fis.types.experiment_error_code
    import aws_sdk_fis.types.experiment_error_location


class ExperimentError(TypedDict, closed=True):
    account_id: NotRequired[
        "aws_sdk_fis.types.experiment_error_account_id.ExperimentErrorAccountId"
    ]
    """<p>The Amazon Web Services Account ID where the experiment failure occurred.</p>"""
    code: NotRequired["aws_sdk_fis.types.experiment_error_code.ExperimentErrorCode"]
    """<p>The error code for the failed experiment.</p>"""
    location: NotRequired[
        "aws_sdk_fis.types.experiment_error_location.ExperimentErrorLocation"
    ]
    """<p>Context for the section of the experiment template that failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentError) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "code" in value:
        out["code"] = value["code"]
    if "location" in value:
        out["location"] = value["location"]
    return out


def deserialize_json(data: dict) -> ExperimentError:
    out: ExperimentError = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "code" in data:
        out["code"] = data["code"]
    if "location" in data:
        out["location"] = data["location"]
    return out
