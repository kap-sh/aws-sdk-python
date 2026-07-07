"""Generated from Smithy shape ``com.amazonaws.fsx#LustreLogConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.general_arn
    import aws_sdk_fsx.types.lustre_access_audit_log_level


class LustreLogConfiguration(TypedDict, closed=True):
    level: NotRequired[
        "aws_sdk_fsx.types.lustre_access_audit_log_level.LustreAccessAuditLogLevel"
    ]
    """<p>The data repository events that are logged by Amazon FSx.</p> <ul> <li> <p> <code>WARN_ONLY</code> - only warning events are logged.</p> </li> <li> <p> <code>ERROR_ONLY</code> - only error events are logged.</p> </li> <li> <p> <code>WARN_ERROR</code> - both warning events and error events are logged.</p> </li> <li> <p> <code>DISABLED</code> - logging of data repository events is turned off.</p> </li> </ul> <p>Note that Amazon File Cache uses a default setting of <code>WARN_ERROR</code>, which can't be changed.</p>"""
    destination: NotRequired["aws_sdk_fsx.types.general_arn.GeneralARN"]
    """<p>The Amazon Resource Name (ARN) that specifies the destination of the logs. The destination can be any Amazon CloudWatch Logs log group ARN. The destination ARN must be in the same Amazon Web Services partition, Amazon Web Services Region, and Amazon Web Services account as your Amazon FSx file system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LustreLogConfiguration) -> dict:
    out: dict = {}
    if "level" in value:
        import aws_sdk_fsx.types.lustre_access_audit_log_level

        out["Level"] = (
            aws_sdk_fsx.types.lustre_access_audit_log_level.serialize_aws_json_1_1(
                value["level"]
            )
        )
    if "destination" in value:
        out["Destination"] = value["destination"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LustreLogConfiguration:
    out: LustreLogConfiguration = {}  # type: ignore[typeddict-item]
    if "Level" in data:
        import aws_sdk_fsx.types.lustre_access_audit_log_level

        out["level"] = (
            aws_sdk_fsx.types.lustre_access_audit_log_level.deserialize_aws_json_1_1(
                data["Level"]
            )
        )
    if "Destination" in data:
        out["destination"] = data["Destination"]
    return out
