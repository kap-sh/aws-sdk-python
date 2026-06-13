"""Generated from Smithy shape ``com.amazonaws.proton#Repository``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.arn
    import aws_sdk_proton.types.repository_arn
    import aws_sdk_proton.types.repository_name
    import aws_sdk_proton.types.repository_provider


class Repository(TypedDict):
    arn: "aws_sdk_proton.types.repository_arn.RepositoryArn"
    """<p>The Amazon Resource Name (ARN) of the linked repository.</p>"""
    provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider"
    """<p>The repository provider.</p>"""
    name: "aws_sdk_proton.types.repository_name.RepositoryName"
    """<p>The repository name.</p>"""
    connection_arn: "aws_sdk_proton.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of your AWS CodeStar connection that connects Proton to your repository provider account.</p>"""
    encryption_key: NotRequired["aws_sdk_proton.types.arn.Arn"]
    """<p>Your customer Amazon Web Services KMS encryption key.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Repository) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["provider"] = value["provider"]
    out["name"] = value["name"]
    out["connectionArn"] = value["connection_arn"]
    if "encryption_key" in value:
        out["encryptionKey"] = value["encryption_key"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Repository:
    out: Repository = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Repository.arn required")
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("Repository.provider required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Repository.name required")
    if "connectionArn" in data:
        out["connection_arn"] = data["connectionArn"]
    else:
        raise DeserializationError("Repository.connection_arn required")
    if "encryptionKey" in data:
        out["encryption_key"] = data["encryptionKey"]
    return out
