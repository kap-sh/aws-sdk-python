"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#GetAccountSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.account_settings_detail


class GetAccountSettingsResponse(TypedDict, closed=True):
    account_settings_detail: NotRequired[
        "capo_opensearchserverless.types.account_settings_detail.AccountSettingsDetail"
    ]
    """<p>OpenSearch Serverless-related details for the current account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAccountSettingsResponse) -> dict:
    out: dict = {}
    if "account_settings_detail" in value:
        import capo_opensearchserverless.types.account_settings_detail

        out["accountSettingsDetail"] = (
            capo_opensearchserverless.types.account_settings_detail.serialize_aws_json_1_0(
                value["account_settings_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAccountSettingsResponse:
    out: GetAccountSettingsResponse = {}  # type: ignore[typeddict-item]
    if "accountSettingsDetail" in data:
        import capo_opensearchserverless.types.account_settings_detail

        out["account_settings_detail"] = (
            capo_opensearchserverless.types.account_settings_detail.deserialize_aws_json_1_0(
                data["accountSettingsDetail"]
            )
        )
    return out
