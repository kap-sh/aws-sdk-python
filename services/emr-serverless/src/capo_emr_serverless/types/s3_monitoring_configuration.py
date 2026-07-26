"""Generated from Smithy shape ``com.amazonaws.emrserverless#S3MonitoringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.encryption_key_arn
    import capo_emr_serverless.types.uri_string


class S3MonitoringConfiguration(TypedDict, closed=True):
    log_uri: NotRequired["capo_emr_serverless.types.uri_string.UriString"]
    """<p>The Amazon S3 destination URI for log publishing.</p>"""
    encryption_key_arn: NotRequired[
        "capo_emr_serverless.types.encryption_key_arn.EncryptionKeyArn"
    ]
    """<p>The KMS key ARN to encrypt the logs published to the given Amazon S3 destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3MonitoringConfiguration) -> dict:
    out: dict = {}
    if "log_uri" in value:
        out["logUri"] = value["log_uri"]
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_json(data: dict) -> S3MonitoringConfiguration:
    out: S3MonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if "logUri" in data:
        out["log_uri"] = data["logUri"]
    if "encryptionKeyArn" in data:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    return out
