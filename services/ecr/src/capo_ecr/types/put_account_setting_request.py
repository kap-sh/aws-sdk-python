"""Generated from Smithy shape ``com.amazonaws.ecr#PutAccountSettingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr.types.account_setting_name
    import capo_ecr.types.account_setting_value


class PutAccountSettingRequest(TypedDict, closed=True):
    name: "capo_ecr.types.account_setting_name.AccountSettingName"
    """<p>The name of the account setting, such as <code>BASIC_SCAN_TYPE_VERSION</code>, <code>REGISTRY_POLICY_SCOPE</code>, or <code>BLOB_MOUNTING</code>.</p>"""
    value: "capo_ecr.types.account_setting_value.AccountSettingValue"
    """<p>Setting value that is specified. Valid value for basic scan type: <code>AWS_NATIVE</code>. Valid values for registry policy scope: <code>V2</code>. Valid values for blob mounting: <code>ENABLED</code> or <code>DISABLED</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutAccountSettingRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutAccountSettingRequest:
    out: PutAccountSettingRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PutAccountSettingRequest.name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("PutAccountSettingRequest.value required")
    return out
