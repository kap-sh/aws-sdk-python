"""Generated from Smithy shape ``com.amazonaws.directoryservice#CreateAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.alias_name
    import capo_directory_service.types.directory_id


class CreateAliasRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>The identifier of the directory for which to create the alias.</p>"""
    alias: "capo_directory_service.types.alias_name.AliasName"
    """<p>The requested alias.</p> <p>The alias must be unique amongst all aliases in Amazon Web Services. This operation throws an <code>EntityAlreadyExistsException</code> error if the alias already exists.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAliasRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["Alias"] = value["alias"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAliasRequest:
    out: CreateAliasRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError("CreateAliasRequest.directory_id required")
    if "Alias" in data:
        out["alias"] = data["Alias"]
    else:
        raise DeserializationError("CreateAliasRequest.alias required")
    return out
