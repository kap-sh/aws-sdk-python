"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsPendingCloudWatchLogsExports``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.string_list


class AwsRdsPendingCloudWatchLogsExports(TypedDict, closed=True):
    log_types_to_enable: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p>A list of log types that are being enabled.</p>"""
    log_types_to_disable: NotRequired[
        "aws_sdk_securityhub.types.string_list.StringList"
    ]
    """<p>A list of log types that are being disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsPendingCloudWatchLogsExports) -> dict:
    out: dict = {}
    if "log_types_to_enable" in value:
        import aws_sdk_securityhub.types.string_list

        out["LogTypesToEnable"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["log_types_to_enable"]
        )
    if "log_types_to_disable" in value:
        import aws_sdk_securityhub.types.string_list

        out["LogTypesToDisable"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["log_types_to_disable"]
        )
    return out


def deserialize_json(data: dict) -> AwsRdsPendingCloudWatchLogsExports:
    out: AwsRdsPendingCloudWatchLogsExports = {}  # type: ignore[typeddict-item]
    if "LogTypesToEnable" in data:
        import aws_sdk_securityhub.types.string_list

        out["log_types_to_enable"] = (
            aws_sdk_securityhub.types.string_list.deserialize_json(
                data["LogTypesToEnable"]
            )
        )
    if "LogTypesToDisable" in data:
        import aws_sdk_securityhub.types.string_list

        out["log_types_to_disable"] = (
            aws_sdk_securityhub.types.string_list.deserialize_json(
                data["LogTypesToDisable"]
            )
        )
    return out
