"""Generated from Smithy shape ``com.amazonaws.ecr#PutAccountSettingResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.account_setting_name
    import aws_sdk_ecr.types.account_setting_value


class PutAccountSettingResponse(TypedDict):
    name: NotRequired["aws_sdk_ecr.types.account_setting_name.AccountSettingName"]
    """<p>Retrieves the name of the account setting.</p>"""
    value: NotRequired["aws_sdk_ecr.types.account_setting_value.AccountSettingValue"]
    """<p>Retrieves the value of the specified account setting.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAccountSettingResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAccountSettingResponse:
    out: PutAccountSettingResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "value" in data:
        out["value"] = data["value"]
    return out
