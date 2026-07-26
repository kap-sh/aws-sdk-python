"""Generated from Smithy shape ``com.amazonaws.ssm#GetServiceSettingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.service_setting


class GetServiceSettingResult(TypedDict, closed=True):
    service_setting: NotRequired["capo_ssm.types.service_setting.ServiceSetting"]
    """<p>The query result of the current service setting.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetServiceSettingResult) -> dict:
    out: dict = {}
    if "service_setting" in value:
        import capo_ssm.types.service_setting

        out["ServiceSetting"] = capo_ssm.types.service_setting.serialize_aws_json_1_1(
            value["service_setting"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetServiceSettingResult:
    out: GetServiceSettingResult = {}  # type: ignore[typeddict-item]
    if "ServiceSetting" in data:
        import capo_ssm.types.service_setting

        out["service_setting"] = (
            capo_ssm.types.service_setting.deserialize_aws_json_1_1(
                data["ServiceSetting"]
            )
        )
    return out
