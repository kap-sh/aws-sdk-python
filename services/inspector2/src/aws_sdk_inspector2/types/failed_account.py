"""Generated from Smithy shape ``com.amazonaws.inspector2#FailedAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id
    import aws_sdk_inspector2.types.error_code
    import aws_sdk_inspector2.types.non_empty_string
    import aws_sdk_inspector2.types.resource_status
    import aws_sdk_inspector2.types.status


class FailedAccount(TypedDict, closed=True):
    account_id: "aws_sdk_inspector2.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    status: NotRequired["aws_sdk_inspector2.types.status.Status"]
    """<p>The status of Amazon Inspector for the account.</p>"""
    resource_status: NotRequired[
        "aws_sdk_inspector2.types.resource_status.ResourceStatus"
    ]
    """<p>An object detailing which resources Amazon Inspector is enabled to scan for the account.</p>"""
    error_code: "aws_sdk_inspector2.types.error_code.ErrorCode"
    """<p>The error code explaining why the account failed to enable Amazon Inspector.</p>"""
    error_message: "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The error message received when the account failed to enable Amazon Inspector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedAccount) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    if "status" in value:
        out["status"] = value["status"]
    if "resource_status" in value:
        import aws_sdk_inspector2.types.resource_status

        out["resourceStatus"] = aws_sdk_inspector2.types.resource_status.serialize_json(
            value["resource_status"]
        )
    out["errorCode"] = value["error_code"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> FailedAccount:
    out: FailedAccount = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("FailedAccount.account_id required")
    if "status" in data:
        out["status"] = data["status"]
    if "resourceStatus" in data:
        import aws_sdk_inspector2.types.resource_status

        out["resource_status"] = (
            aws_sdk_inspector2.types.resource_status.deserialize_json(
                data["resourceStatus"]
            )
        )
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    else:
        raise DeserializationError("FailedAccount.error_code required")
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    else:
        raise DeserializationError("FailedAccount.error_message required")
    return out
