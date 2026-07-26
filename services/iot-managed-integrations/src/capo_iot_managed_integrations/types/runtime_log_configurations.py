"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#RuntimeLogConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.delete_local_store_after_upload
    import capo_iot_managed_integrations.types.local_store_file_rotation_max_bytes
    import capo_iot_managed_integrations.types.local_store_file_rotation_max_files
    import capo_iot_managed_integrations.types.local_store_location
    import capo_iot_managed_integrations.types.log_level
    import capo_iot_managed_integrations.types.upload_log
    import capo_iot_managed_integrations.types.upload_period_minutes


class RuntimeLogConfigurations(TypedDict, closed=True):
    log_level: NotRequired["capo_iot_managed_integrations.types.log_level.LogLevel"]
    """<p>The different log levels available for configuration.</p>"""
    log_flush_level: NotRequired[
        "capo_iot_managed_integrations.types.log_level.LogLevel"
    ]
    """<p>The different log levels available for configuration.</p>"""
    local_store_location: NotRequired[
        "capo_iot_managed_integrations.types.local_store_location.LocalStoreLocation"
    ]
    """<p>Configuration of where to store runtime logs in the device.</p>"""
    local_store_file_rotation_max_files: NotRequired[
        "capo_iot_managed_integrations.types.local_store_file_rotation_max_files.LocalStoreFileRotationMaxFiles"
    ]
    """<p>Configuration to set the maximum number of runtime log files that can be stored on the device before the oldest files are deleted or overwritten.</p>"""
    local_store_file_rotation_max_bytes: NotRequired[
        "capo_iot_managed_integrations.types.local_store_file_rotation_max_bytes.LocalStoreFileRotationMaxBytes"
    ]
    """<p>Configuration to set the maximum bytes of runtime logs that can be stored on the device before the oldest logs are deleted or overwritten.</p>"""
    upload_log: NotRequired["capo_iot_managed_integrations.types.upload_log.UploadLog"]
    """<p>Configuration to enable or disable uploading of runtime logs to the cloud.</p>"""
    upload_period_minutes: NotRequired[
        "capo_iot_managed_integrations.types.upload_period_minutes.UploadPeriodMinutes"
    ]
    """<p>Configuration to set the time interval in minutes between each batch of runtime logs that the device uploads to the cloud.</p>"""
    delete_local_store_after_upload: NotRequired[
        "capo_iot_managed_integrations.types.delete_local_store_after_upload.DeleteLocalStoreAfterUpload"
    ]
    """<p>Configuration to enable or disable deleting of runtime logs in the device once uploaded to the cloud.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeLogConfigurations) -> dict:
    out: dict = {}
    if "log_level" in value:
        import capo_iot_managed_integrations.types.log_level

        out["LogLevel"] = capo_iot_managed_integrations.types.log_level.serialize_json(
            value["log_level"]
        )
    if "log_flush_level" in value:
        import capo_iot_managed_integrations.types.log_level

        out["LogFlushLevel"] = (
            capo_iot_managed_integrations.types.log_level.serialize_json(
                value["log_flush_level"]
            )
        )
    if "local_store_location" in value:
        out["LocalStoreLocation"] = value["local_store_location"]
    if "local_store_file_rotation_max_files" in value:
        out["LocalStoreFileRotationMaxFiles"] = value[
            "local_store_file_rotation_max_files"
        ]
    if "local_store_file_rotation_max_bytes" in value:
        out["LocalStoreFileRotationMaxBytes"] = value[
            "local_store_file_rotation_max_bytes"
        ]
    if "upload_log" in value:
        out["UploadLog"] = value["upload_log"]
    if "upload_period_minutes" in value:
        out["UploadPeriodMinutes"] = value["upload_period_minutes"]
    if "delete_local_store_after_upload" in value:
        out["DeleteLocalStoreAfterUpload"] = value["delete_local_store_after_upload"]
    return out


def deserialize_json(data: dict) -> RuntimeLogConfigurations:
    out: RuntimeLogConfigurations = {}  # type: ignore[typeddict-item]
    if "LogLevel" in data:
        import capo_iot_managed_integrations.types.log_level

        out["log_level"] = (
            capo_iot_managed_integrations.types.log_level.deserialize_json(
                data["LogLevel"]
            )
        )
    if "LogFlushLevel" in data:
        import capo_iot_managed_integrations.types.log_level

        out["log_flush_level"] = (
            capo_iot_managed_integrations.types.log_level.deserialize_json(
                data["LogFlushLevel"]
            )
        )
    if "LocalStoreLocation" in data:
        out["local_store_location"] = data["LocalStoreLocation"]
    if "LocalStoreFileRotationMaxFiles" in data:
        out["local_store_file_rotation_max_files"] = data[
            "LocalStoreFileRotationMaxFiles"
        ]
    if "LocalStoreFileRotationMaxBytes" in data:
        out["local_store_file_rotation_max_bytes"] = data[
            "LocalStoreFileRotationMaxBytes"
        ]
    if "UploadLog" in data:
        out["upload_log"] = data["UploadLog"]
    if "UploadPeriodMinutes" in data:
        out["upload_period_minutes"] = data["UploadPeriodMinutes"]
    if "DeleteLocalStoreAfterUpload" in data:
        out["delete_local_store_after_upload"] = data["DeleteLocalStoreAfterUpload"]
    return out
