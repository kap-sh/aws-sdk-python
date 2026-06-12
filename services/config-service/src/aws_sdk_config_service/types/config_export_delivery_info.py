"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigExportDeliveryInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.date
    import aws_sdk_config_service.types.delivery_status
    import aws_sdk_config_service.types.string


class ConfigExportDeliveryInfo(TypedDict):
    last_status: NotRequired[
        "aws_sdk_config_service.types.delivery_status.DeliveryStatus"
    ]
    """<p>Status of the last attempted delivery.</p>"""
    last_error_code: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The error code from the last attempted delivery.</p>"""
    last_error_message: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The error message from the last attempted delivery.</p>"""
    last_attempt_time: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>The time of the last attempted delivery.</p>"""
    last_successful_time: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>The time of the last successful delivery.</p>"""
    next_delivery_time: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>The time that the next delivery occurs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigExportDeliveryInfo) -> dict:
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
    if "last_attempt_time" in value:
        import aws_sdk_config_service.types.date

        out["lastAttemptTime"] = (
            aws_sdk_config_service.types.date.serialize_aws_json_1_1(
                value["last_attempt_time"]
            )
        )
    if "last_successful_time" in value:
        import aws_sdk_config_service.types.date

        out["lastSuccessfulTime"] = (
            aws_sdk_config_service.types.date.serialize_aws_json_1_1(
                value["last_successful_time"]
            )
        )
    if "next_delivery_time" in value:
        import aws_sdk_config_service.types.date

        out["nextDeliveryTime"] = (
            aws_sdk_config_service.types.date.serialize_aws_json_1_1(
                value["next_delivery_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigExportDeliveryInfo:
    out: ConfigExportDeliveryInfo = {}  # type: ignore[typeddict-item]
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
    if "lastAttemptTime" in data:
        import aws_sdk_config_service.types.date

        out["last_attempt_time"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["lastAttemptTime"]
            )
        )
    if "lastSuccessfulTime" in data:
        import aws_sdk_config_service.types.date

        out["last_successful_time"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["lastSuccessfulTime"]
            )
        )
    if "nextDeliveryTime" in data:
        import aws_sdk_config_service.types.date

        out["next_delivery_time"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["nextDeliveryTime"]
            )
        )
    return out
