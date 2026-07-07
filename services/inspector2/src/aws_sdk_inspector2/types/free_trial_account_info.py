"""Generated from Smithy shape ``com.amazonaws.inspector2#FreeTrialAccountInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.free_trial_info_list
    import aws_sdk_inspector2.types.metering_account_id


class FreeTrialAccountInfo(TypedDict, closed=True):
    account_id: "aws_sdk_inspector2.types.metering_account_id.MeteringAccountId"
    """<p>The account associated with the Amazon Inspector free trial information.</p>"""
    free_trial_info: "aws_sdk_inspector2.types.free_trial_info_list.FreeTrialInfoList"
    """<p>Contains information about the Amazon Inspector free trial for an account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeTrialAccountInfo) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    import aws_sdk_inspector2.types.free_trial_info_list

    out["freeTrialInfo"] = aws_sdk_inspector2.types.free_trial_info_list.serialize_json(
        value["free_trial_info"]
    )
    return out


def deserialize_json(data: dict) -> FreeTrialAccountInfo:
    out: FreeTrialAccountInfo = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("FreeTrialAccountInfo.account_id required")
    if "freeTrialInfo" in data:
        import aws_sdk_inspector2.types.free_trial_info_list

        out["free_trial_info"] = (
            aws_sdk_inspector2.types.free_trial_info_list.deserialize_json(
                data["freeTrialInfo"]
            )
        )
    else:
        raise DeserializationError("FreeTrialAccountInfo.free_trial_info required")
    return out
