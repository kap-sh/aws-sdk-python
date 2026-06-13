"""Generated from Smithy shape ``com.amazonaws.inspector2#BatchGetFreeTrialInfoRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.metering_account_id_list


class BatchGetFreeTrialInfoRequest(TypedDict):
    account_ids: (
        "aws_sdk_inspector2.types.metering_account_id_list.MeteringAccountIdList"
    )
    """<p>The account IDs to get free trial status for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFreeTrialInfoRequest) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.metering_account_id_list

    out["accountIds"] = (
        aws_sdk_inspector2.types.metering_account_id_list.serialize_json(
            value["account_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetFreeTrialInfoRequest:
    out: BatchGetFreeTrialInfoRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_inspector2.types.metering_account_id_list

        out["account_ids"] = (
            aws_sdk_inspector2.types.metering_account_id_list.deserialize_json(
                data["accountIds"]
            )
        )
    else:
        raise DeserializationError("BatchGetFreeTrialInfoRequest.account_ids required")
    return out
