"""Generated from Smithy shape ``com.amazonaws.datasync#ManagedSecretConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datasync.types.secret_arn


class ManagedSecretConfig(TypedDict):
    secret_arn: NotRequired["aws_sdk_datasync.types.secret_arn.SecretArn"]
    """<p>Specifies the ARN for an Secrets Manager secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedSecretConfig) -> dict:
    out: dict = {}
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedSecretConfig:
    out: ManagedSecretConfig = {}  # type: ignore[typeddict-item]
    if "SecretArn" in data:
        out["secret_arn"] = data["SecretArn"]
    return out
