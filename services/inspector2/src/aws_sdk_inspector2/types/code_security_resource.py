"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeSecurityResource``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_inspector2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.project_id


class _CodeSecurityResource_projectId(TypedDict):
    projectId: "aws_sdk_inspector2.types.project_id.ProjectId"


CodeSecurityResource: TypeAlias = _CodeSecurityResource_projectId


# --- restJson1 ser/de ---
def serialize_json(value: CodeSecurityResource) -> dict:
    if "projectId" in value:
        return {"projectId": value["projectId"]}
    else:
        raise SerializationError("CodeSecurityResource: no variant present")


def deserialize_json(data: dict) -> CodeSecurityResource:
    if "projectId" in data:
        return {"projectId": data["projectId"]}
    else:
        raise DeserializationError("CodeSecurityResource: no recognized variant key")
