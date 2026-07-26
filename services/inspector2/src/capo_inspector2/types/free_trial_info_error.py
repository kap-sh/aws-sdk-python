"""Generated from Smithy shape ``com.amazonaws.inspector2#FreeTrialInfoError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.free_trial_info_error_code
    import capo_inspector2.types.metering_account_id


class FreeTrialInfoError(TypedDict, closed=True):
    account_id: "capo_inspector2.types.metering_account_id.MeteringAccountId"
    """<p>The account associated with the Amazon Inspector free trial information.</p>"""
    code: "capo_inspector2.types.free_trial_info_error_code.FreeTrialInfoErrorCode"
    """<p>The error code.</p>"""
    message: "str"
    """<p>The error message returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialInfoError) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> FreeTrialInfoError:
    out: FreeTrialInfoError = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("FreeTrialInfoError.account_id required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("FreeTrialInfoError.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("FreeTrialInfoError.message required")
    return out
