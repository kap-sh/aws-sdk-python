"""Generated from Smithy shape ``com.amazonaws.workspaces#ActiveDirectoryConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.domain_name
    import aws_sdk_workspaces.types.secrets_manager_arn


class ActiveDirectoryConfig(TypedDict):
    domain_name: "aws_sdk_workspaces.types.domain_name.DomainName"
    """<p>The name of the domain.</p>"""
    service_account_secret_arn: (
        "aws_sdk_workspaces.types.secrets_manager_arn.SecretsManagerArn"
    )
    """<p>Indicates the secret ARN on the service account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActiveDirectoryConfig) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    out["ServiceAccountSecretArn"] = value["service_account_secret_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActiveDirectoryConfig:
    out: ActiveDirectoryConfig = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("ActiveDirectoryConfig.domain_name required")
    if "ServiceAccountSecretArn" in data:
        out["service_account_secret_arn"] = data["ServiceAccountSecretArn"]
    else:
        raise DeserializationError(
            "ActiveDirectoryConfig.service_account_secret_arn required"
        )
    return out
