"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationRecorderStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.amazon_resource_name
    import aws_sdk_config_service.types.boolean
    import aws_sdk_config_service.types.date
    import aws_sdk_config_service.types.recorder_status
    import aws_sdk_config_service.types.service_principal
    import aws_sdk_config_service.types.string


class ConfigurationRecorderStatus(TypedDict):
    arn: NotRequired[
        "aws_sdk_config_service.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the configuration recorder.</p>"""
    name: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The name of the configuration recorder.</p>"""
    last_start_time: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>The time the recorder was last started.</p>"""
    last_stop_time: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>The time the recorder was last stopped.</p>"""
    recording: "aws_sdk_config_service.types.boolean.Boolean"
    """<p>Specifies whether or not the recorder is currently recording.</p>"""
    last_status: NotRequired[
        "aws_sdk_config_service.types.recorder_status.RecorderStatus"
    ]
    """<p>The status of the latest recording event processed by the recorder.</p>"""
    last_error_code: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The latest error code from when the recorder last failed.</p>"""
    last_error_message: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The latest error message from when the recorder last failed.</p>"""
    last_status_change_time: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>The time of the latest change in status of an recording event processed by the recorder.</p>"""
    service_principal: NotRequired[
        "aws_sdk_config_service.types.service_principal.ServicePrincipal"
    ]
    """<p>For service-linked configuration recorders, the service principal of the linked Amazon Web Services service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationRecorderStatus) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "last_start_time" in value:
        import aws_sdk_config_service.types.date

        out["lastStartTime"] = aws_sdk_config_service.types.date.serialize_aws_json_1_1(
            value["last_start_time"]
        )
    if "last_stop_time" in value:
        import aws_sdk_config_service.types.date

        out["lastStopTime"] = aws_sdk_config_service.types.date.serialize_aws_json_1_1(
            value["last_stop_time"]
        )
    out["recording"] = value.get("recording", False)
    if "last_status" in value:
        import aws_sdk_config_service.types.recorder_status

        out["lastStatus"] = (
            aws_sdk_config_service.types.recorder_status.serialize_aws_json_1_1(
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
    if "service_principal" in value:
        out["servicePrincipal"] = value["service_principal"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigurationRecorderStatus:
    out: ConfigurationRecorderStatus = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "lastStartTime" in data:
        import aws_sdk_config_service.types.date

        out["last_start_time"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["lastStartTime"]
            )
        )
    if "lastStopTime" in data:
        import aws_sdk_config_service.types.date

        out["last_stop_time"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["lastStopTime"]
            )
        )
    if "recording" in data:
        out["recording"] = data["recording"]
    else:
        out["recording"] = False
    if "lastStatus" in data:
        import aws_sdk_config_service.types.recorder_status

        out["last_status"] = (
            aws_sdk_config_service.types.recorder_status.deserialize_aws_json_1_1(
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
    if "servicePrincipal" in data:
        out["service_principal"] = data["servicePrincipal"]
    return out
