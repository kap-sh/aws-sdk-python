"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigStreamDeliveryInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.date
    import aws_sdk_config_service.types.delivery_status
    import aws_sdk_config_service.types.string


class ConfigStreamDeliveryInfo(TypedDict):
    last_status: NotRequired[
        "aws_sdk_config_service.types.delivery_status.DeliveryStatus"
    ]
    """<p>Status of the last attempted delivery.</p> <p> <b>Note</b> Providing an SNS topic on a <a href=\"https://docs.aws.amazon.com/config/latest/APIReference/API_DeliveryChannel.html\">DeliveryChannel</a> for Config is optional. If the SNS delivery is turned off, the last status will be <b>Not_Applicable</b>.</p>"""
    last_error_code: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The error code from the last attempted delivery.</p>"""
    last_error_message: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The error message from the last attempted delivery.</p>"""
    last_status_change_time: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>The time from the last status change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigStreamDeliveryInfo) -> dict:
    out: dict = {}
    if "last_status" in value:
        import aws_sdk_config_service.types.delivery_status

        out["lastStatus"] = (
            aws_sdk_config_service.types.delivery_status.serialize_aws_json_1_1(
                value["last_status"]
            )
        )
    if "last_error_code" in value:
        out["lastErrorCode"] = value["last_error_code"]
    if "last_error_message" in value:
        out["lastErrorMessage"] = value["last_error_message"]
    if "last_status_change_time" in value:
        import aws_sdk_config_service.types.date

        out["lastStatusChangeTime"] = (
            aws_sdk_config_service.types.date.serialize_aws_json_1_1(
                value["last_status_change_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigStreamDeliveryInfo:
    out: ConfigStreamDeliveryInfo = {}  # type: ignore[typeddict-item]
    if "lastStatus" in data:
        import aws_sdk_config_service.types.delivery_status

        out["last_status"] = (
            aws_sdk_config_service.types.delivery_status.deserialize_aws_json_1_1(
                data["lastStatus"]
            )
        )
    if "lastErrorCode" in data:
        out["last_error_code"] = data["lastErrorCode"]
    if "lastErrorMessage" in data:
        out["last_error_message"] = data["lastErrorMessage"]
    if "lastStatusChangeTime" in data:
        import aws_sdk_config_service.types.date

        out["last_status_change_time"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["lastStatusChangeTime"]
            )
        )
    return out
