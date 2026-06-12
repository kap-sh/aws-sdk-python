"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#LogsBackupConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.region
    import aws_sdk_observabilityadmin.types.resource_arn


class LogsBackupConfiguration(TypedDict):
    region: "aws_sdk_observabilityadmin.types.region.Region"
    """<p>Logs specific backup destination region within the primary destination account to which log data should be centralized.</p>"""
    kms_key_arn: NotRequired[
        "aws_sdk_observabilityadmin.types.resource_arn.ResourceArn"
    ]
    """<p>KMS Key ARN belonging to the primary destination account and backup region, to encrypt newly created central log groups in the backup destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogsBackupConfiguration) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> LogsBackupConfiguration:
    out: LogsBackupConfiguration = {}  # type: ignore[typeddict-item]
    if "Region" in data:
        out["region"] = data["Region"]
    else:
        raise DeserializationError("LogsBackupConfiguration.region required")
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
