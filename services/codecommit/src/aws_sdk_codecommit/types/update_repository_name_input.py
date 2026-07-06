"""Generated from Smithy shape ``com.amazonaws.codecommit#UpdateRepositoryNameInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.repository_name


class UpdateRepositoryNameInput(TypedDict, closed=True):
    old_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The current name of the repository.</p>"""
    new_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The new name for the repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRepositoryNameInput) -> dict:
    out: dict = {}
    out["oldName"] = value["old_name"]
    out["newName"] = value["new_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRepositoryNameInput:
    out: UpdateRepositoryNameInput = {}  # type: ignore[typeddict-item]
    if "oldName" in data:
        out["old_name"] = data["oldName"]
    else:
        raise DeserializationError("UpdateRepositoryNameInput.old_name required")
    if "newName" in data:
        out["new_name"] = data["newName"]
    else:
        raise DeserializationError("UpdateRepositoryNameInput.new_name required")
    return out
