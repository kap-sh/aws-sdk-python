"""Generated from Smithy shape ``com.amazonaws.proton#RepositorySummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.arn
    import aws_sdk_proton.types.repository_arn
    import aws_sdk_proton.types.repository_name
    import aws_sdk_proton.types.repository_provider


class RepositorySummary(TypedDict):
    arn: "aws_sdk_proton.types.repository_arn.RepositoryArn"
    """<p>The Amazon Resource Name (ARN) of the linked repository.</p>"""
    provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider"
    """<p>The repository provider.</p>"""
    name: "aws_sdk_proton.types.repository_name.RepositoryName"
    """<p>The repository name.</p>"""
    connection_arn: "aws_sdk_proton.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the of your connection that connects Proton to your repository.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositorySummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["provider"] = value["provider"]
    out["name"] = value["name"]
    out["connectionArn"] = value["connection_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RepositorySummary:
    out: RepositorySummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("RepositorySummary.arn required")
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("RepositorySummary.provider required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RepositorySummary.name required")
    if "connectionArn" in data:
        out["connection_arn"] = data["connectionArn"]
    else:
        raise DeserializationError("RepositorySummary.connection_arn required")
    return out
