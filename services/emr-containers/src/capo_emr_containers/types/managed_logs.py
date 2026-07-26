"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ManagedLogs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.allow_aws_to_retain_logs
    import capo_emr_containers.types.kms_key_arn


class ManagedLogs(TypedDict, closed=True):
    allow_aws_to_retain_logs: NotRequired[
        "capo_emr_containers.types.allow_aws_to_retain_logs.AllowAWSToRetainLogs"
    ]
    """<p>Determines whether Amazon Web Services can retain logs.</p>"""
    encryption_key_arn: NotRequired["capo_emr_containers.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon resource name (ARN) of the encryption key for logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedLogs) -> dict:
    out: dict = {}
    if "allow_aws_to_retain_logs" in value:
        import capo_emr_containers.types.allow_aws_to_retain_logs

        out["allowAWSToRetainLogs"] = (
            capo_emr_containers.types.allow_aws_to_retain_logs.serialize_json(
                value["allow_aws_to_retain_logs"]
            )
        )
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_json(data: dict) -> ManagedLogs:
    out: ManagedLogs = {}  # type: ignore[typeddict-item]
    if "allowAWSToRetainLogs" in data:
        import capo_emr_containers.types.allow_aws_to_retain_logs

        out["allow_aws_to_retain_logs"] = (
            capo_emr_containers.types.allow_aws_to_retain_logs.deserialize_json(
                data["allowAWSToRetainLogs"]
            )
        )
    if "encryptionKeyArn" in data:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    return out
