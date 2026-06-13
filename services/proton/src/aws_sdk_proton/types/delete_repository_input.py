"""Generated from Smithy shape ``com.amazonaws.proton#DeleteRepositoryInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.repository_name
    import aws_sdk_proton.types.repository_provider


class DeleteRepositoryInput(TypedDict):
    provider: "aws_sdk_proton.types.repository_provider.RepositoryProvider"
    """<p>The repository provider.</p>"""
    name: "aws_sdk_proton.types.repository_name.RepositoryName"
    """<p>The repository name.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRepositoryInput) -> dict:
    out: dict = {}
    out["provider"] = value["provider"]
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRepositoryInput:
    out: DeleteRepositoryInput = {}  # type: ignore[typeddict-item]
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("DeleteRepositoryInput.provider required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeleteRepositoryInput.name required")
    return out
