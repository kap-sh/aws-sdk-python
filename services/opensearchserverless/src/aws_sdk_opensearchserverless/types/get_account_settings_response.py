"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#GetAccountSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.account_settings_detail


class GetAccountSettingsResponse(TypedDict):
    account_settings_detail: NotRequired[
        "aws_sdk_opensearchserverless.types.account_settings_detail.AccountSettingsDetail"
    ]
    """<p>OpenSearch Serverless-related details for the current account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAccountSettingsResponse) -> dict:
    out: dict = {}
    if "account_settings_detail" in value:
        import aws_sdk_opensearchserverless.types.account_settings_detail

        out["accountSettingsDetail"] = (
            aws_sdk_opensearchserverless.types.account_settings_detail.serialize_aws_json_1_0(
                value["account_settings_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAccountSettingsResponse:
    out: GetAccountSettingsResponse = {}  # type: ignore[typeddict-item]
    if "accountSettingsDetail" in data:
        import aws_sdk_opensearchserverless.types.account_settings_detail

        out["account_settings_detail"] = (
            aws_sdk_opensearchserverless.types.account_settings_detail.deserialize_aws_json_1_0(
                data["accountSettingsDetail"]
            )
        )
    return out
