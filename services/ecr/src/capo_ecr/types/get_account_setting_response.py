"""Generated from Smithy shape ``com.amazonaws.ecr#GetAccountSettingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.account_setting_name


class GetAccountSettingResponse(TypedDict, closed=True):
    name: NotRequired["capo_ecr.types.account_setting_name.AccountSettingName"]
    """<p>Retrieves the name of the account setting.</p>"""
    value: NotRequired["capo_ecr.types.account_setting_name.AccountSettingName"]
    """<p>The setting value for the setting name. Valid value for basic scan type: <code>AWS_NATIVE</code>. Valid values for registry policy scope: <code>V2</code>. Valid values for blob mounting: <code>ENABLED</code> or <code>DISABLED</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccountSettingResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccountSettingResponse:
    out: GetAccountSettingResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out
