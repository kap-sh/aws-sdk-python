"""Generated from Smithy shape ``com.amazonaws.securityhub#Result``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.account_id
    import capo_securityhub.types.non_empty_string


class Result(TypedDict, closed=True):
    account_id: NotRequired["capo_securityhub.types.account_id.AccountId"]
    """<p>An Amazon Web Services account ID of the account that was not processed.</p>"""
    processing_result: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The reason that the account was not processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Result) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "processing_result" in value:
        out["ProcessingResult"] = value["processing_result"]
    return out


def deserialize_json(data: dict) -> Result:
    out: Result = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "ProcessingResult" in data:
        out["processing_result"] = data["ProcessingResult"]
    return out
