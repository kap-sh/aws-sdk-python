"""Generated from Smithy shape ``com.amazonaws.macie2#UnprocessedAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.error_code


class UnprocessedAccount(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Web Services account ID for the account that the request applies to.</p>"""
    error_code: NotRequired["aws_sdk_macie2.types.error_code.ErrorCode"]
    """<p>The source of the issue or delay in processing the request.</p>"""
    error_message: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The reason why the request hasn't been processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedAccount) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "error_code" in value:
        import aws_sdk_macie2.types.error_code

        out["errorCode"] = aws_sdk_macie2.types.error_code.serialize_json(
            value["error_code"]
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> UnprocessedAccount:
    out: UnprocessedAccount = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "errorCode" in data:
        import aws_sdk_macie2.types.error_code

        out["error_code"] = aws_sdk_macie2.types.error_code.deserialize_json(
            data["errorCode"]
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
