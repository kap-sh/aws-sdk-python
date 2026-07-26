"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AclGrantee``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.acl_canonical_id
    import capo_accessanalyzer.types.acl_uri


class _AclGrantee_id(TypedDict, closed=True):
    id: "capo_accessanalyzer.types.acl_canonical_id.AclCanonicalId"


class _AclGrantee_uri(TypedDict, closed=True):
    uri: "capo_accessanalyzer.types.acl_uri.AclUri"


AclGrantee: TypeAlias = _AclGrantee_id | _AclGrantee_uri


# --- restJson1 ser/de ---
def serialize_json(value: AclGrantee) -> dict:
    if "id" in value:
        return {"id": value["id"]}
    elif "uri" in value:
        return {"uri": value["uri"]}
    else:
        raise SerializationError("AclGrantee: no variant present")


def deserialize_json(data: dict) -> AclGrantee:
    if "id" in data:
        return {"id": data["id"]}
    elif "uri" in data:
        return {"uri": data["uri"]}
    else:
        raise DeserializationError("AclGrantee: no recognized variant key")
