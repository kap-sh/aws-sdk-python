"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchGetFreeTrialInfoRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.metering_account_id_list


class BatchGetFreeTrialInfoRequest(TypedDict, closed=True):
    account_ids: "capo_inspector2.types.metering_account_id_list.MeteringAccountIdList"
    """<p>The account IDs to get free trial status for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFreeTrialInfoRequest) -> dict:
    out: dict = {}
    import capo_inspector2.types.metering_account_id_list

    out["accountIds"] = capo_inspector2.types.metering_account_id_list.serialize_json(
        value["account_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetFreeTrialInfoRequest:
    out: BatchGetFreeTrialInfoRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import capo_inspector2.types.metering_account_id_list

        out["account_ids"] = (
            capo_inspector2.types.metering_account_id_list.deserialize_json(
                data["accountIds"]
            )
        )
    else:
        raise DeserializationError("BatchGetFreeTrialInfoRequest.account_ids required")
    return out
