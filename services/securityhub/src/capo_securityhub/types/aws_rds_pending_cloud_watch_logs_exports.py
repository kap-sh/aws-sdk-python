"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsPendingCloudWatchLogsExports``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.string_list


class AwsRdsPendingCloudWatchLogsExports(TypedDict, closed=True):
    log_types_to_enable: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p>A list of log types that are being enabled.</p>"""
    log_types_to_disable: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p>A list of log types that are being disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsPendingCloudWatchLogsExports) -> dict:
    out: dict = {}
    if "log_types_to_enable" in value:
        import capo_securityhub.types.string_list

        out["LogTypesToEnable"] = capo_securityhub.types.string_list.serialize_json(
            value["log_types_to_enable"]
        )
    if "log_types_to_disable" in value:
        import capo_securityhub.types.string_list

        out["LogTypesToDisable"] = capo_securityhub.types.string_list.serialize_json(
            value["log_types_to_disable"]
        )
    return out


def deserialize_json(data: dict) -> AwsRdsPendingCloudWatchLogsExports:
    out: AwsRdsPendingCloudWatchLogsExports = {}  # type: ignore[typeddict-item]
    if "LogTypesToEnable" in data:
        import capo_securityhub.types.string_list

        out["log_types_to_enable"] = (
            capo_securityhub.types.string_list.deserialize_json(
                data["LogTypesToEnable"]
            )
        )
    if "LogTypesToDisable" in data:
        import capo_securityhub.types.string_list

        out["log_types_to_disable"] = (
            capo_securityhub.types.string_list.deserialize_json(
                data["LogTypesToDisable"]
            )
        )
    return out
