"""Generated from Smithy shape ``com.amazonaws.ssm#ResetServiceSettingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.service_setting


class ResetServiceSettingResult(TypedDict, closed=True):
    service_setting: NotRequired["capo_ssm.types.service_setting.ServiceSetting"]
    """<p>The current, effective service setting after calling the ResetServiceSetting API operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResetServiceSettingResult) -> dict:
    out: dict = {}
    if "service_setting" in value:
        import capo_ssm.types.service_setting

        out["ServiceSetting"] = capo_ssm.types.service_setting.serialize_aws_json_1_1(
            value["service_setting"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResetServiceSettingResult:
    out: ResetServiceSettingResult = {}  # type: ignore[typeddict-item]
    if "ServiceSetting" in data:
        import capo_ssm.types.service_setting

        out["service_setting"] = (
            capo_ssm.types.service_setting.deserialize_aws_json_1_1(
                data["ServiceSetting"]
            )
        )
    return out
