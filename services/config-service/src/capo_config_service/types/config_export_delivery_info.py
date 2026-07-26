"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigExportDeliveryInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.date
    import capo_config_service.types.delivery_status
    import capo_config_service.types.string


class ConfigExportDeliveryInfo(TypedDict, closed=True):
    last_status: NotRequired["capo_config_service.types.delivery_status.DeliveryStatus"]
    """<p>Status of the last attempted delivery.</p>"""
    last_error_code: NotRequired["capo_config_service.types.string.String"]
    """<p>The error code from the last attempted delivery.</p>"""
    last_error_message: NotRequired["capo_config_service.types.string.String"]
    """<p>The error message from the last attempted delivery.</p>"""
    last_attempt_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time of the last attempted delivery.</p>"""
    last_successful_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time of the last successful delivery.</p>"""
    next_delivery_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The time that the next delivery occurs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigExportDeliveryInfo) -> dict:
    out: dict = {}
    if "last_status" in value:
        import capo_config_service.types.delivery_status

        out["lastStatus"] = (
            capo_config_service.types.delivery_status.serialize_aws_json_1_1(
                value["last_status"]
            )
        )
    if "last_error_code" in value:
        out["lastErrorCode"] = value["last_error_code"]
    if "last_error_message" in value:
        out["lastErrorMessage"] = value["last_error_message"]
    if "last_attempt_time" in value:
        import capo_config_service.types.date

        out["lastAttemptTime"] = capo_config_service.types.date.serialize_aws_json_1_1(
            value["last_attempt_time"]
        )
    if "last_successful_time" in value:
        import capo_config_service.types.date

        out["lastSuccessfulTime"] = (
            capo_config_service.types.date.serialize_aws_json_1_1(
                value["last_successful_time"]
            )
        )
    if "next_delivery_time" in value:
        import capo_config_service.types.date

        out["nextDeliveryTime"] = capo_config_service.types.date.serialize_aws_json_1_1(
            value["next_delivery_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigExportDeliveryInfo:
    out: ConfigExportDeliveryInfo = {}  # type: ignore[typeddict-item]
    if "lastStatus" in data:
        import capo_config_service.types.delivery_status

        out["last_status"] = (
            capo_config_service.types.delivery_status.deserialize_aws_json_1_1(
                data["lastStatus"]
            )
        )
    if "lastErrorCode" in data:
        out["last_error_code"] = data["lastErrorCode"]
    if "lastErrorMessage" in data:
        out["last_error_message"] = data["lastErrorMessage"]
    if "lastAttemptTime" in data:
        import capo_config_service.types.date

        out["last_attempt_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["lastAttemptTime"]
            )
        )
    if "lastSuccessfulTime" in data:
        import capo_config_service.types.date

        out["last_successful_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["lastSuccessfulTime"]
            )
        )
    if "nextDeliveryTime" in data:
        import capo_config_service.types.date

        out["next_delivery_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["nextDeliveryTime"]
            )
        )
    return out
