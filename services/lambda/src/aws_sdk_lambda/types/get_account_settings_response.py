"""Generated from Smithy shape ``com.amazonaws.lambda#GetAccountSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.account_limit
    import aws_sdk_lambda.types.account_usage


class GetAccountSettingsResponse(TypedDict):
    account_limit: NotRequired["aws_sdk_lambda.types.account_limit.AccountLimit"]
    """<p>Limits that are related to concurrency and code storage.</p>"""
    account_usage: NotRequired["aws_sdk_lambda.types.account_usage.AccountUsage"]
    """<p>The number of functions and amount of storage in use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountSettingsResponse) -> dict:
    out: dict = {}
    if "account_limit" in value:
        import aws_sdk_lambda.types.account_limit

        out["AccountLimit"] = aws_sdk_lambda.types.account_limit.serialize_json(
            value["account_limit"]
        )
    if "account_usage" in value:
        import aws_sdk_lambda.types.account_usage

        out["AccountUsage"] = aws_sdk_lambda.types.account_usage.serialize_json(
            value["account_usage"]
        )
    return out


def deserialize_json(data: dict) -> GetAccountSettingsResponse:
    out: GetAccountSettingsResponse = {}  # type: ignore[typeddict-item]
    if "AccountLimit" in data:
        import aws_sdk_lambda.types.account_limit

        out["account_limit"] = aws_sdk_lambda.types.account_limit.deserialize_json(
            data["AccountLimit"]
        )
    if "AccountUsage" in data:
        import aws_sdk_lambda.types.account_usage

        out["account_usage"] = aws_sdk_lambda.types.account_usage.deserialize_json(
            data["AccountUsage"]
        )
    return out
