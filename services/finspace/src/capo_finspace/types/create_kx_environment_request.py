"""Generated from Smithy shape ``com.amazonaws.finspace#CreateKxEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import capo_finspace.types.client_token
    import capo_finspace.types.description
    import capo_finspace.types.kms_key_arn
    import capo_finspace.types.kx_environment_name
    import capo_finspace.types.tag_map


class CreateKxEnvironmentRequest(TypedDict, closed=True):
    name: "capo_finspace.types.kx_environment_name.KxEnvironmentName"
    """<p>The name of the kdb environment that you want to create.</p>"""
    description: NotRequired["capo_finspace.types.description.Description"]
    """<p>A description for the kdb environment.</p>"""
    kms_key_id: "capo_finspace.types.kms_key_arn.KmsKeyARN"
    """<p>The KMS key ID to encrypt your data in the FinSpace environment.</p>"""
    tags: NotRequired["capo_finspace.types.tag_map.TagMap"]
    """<p>A list of key-value pairs to label the kdb environment. You can add up to 50 tags to your kdb environment.</p>"""
    client_token: NotRequired["capo_finspace.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKxEnvironmentRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import capo_finspace.types.tag_map

        out["tags"] = capo_finspace.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateKxEnvironmentRequest:
    out: CreateKxEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateKxEnvironmentRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    else:
        raise DeserializationError("CreateKxEnvironmentRequest.kms_key_id required")
    if "tags" in data:
        import capo_finspace.types.tag_map

        out["tags"] = capo_finspace.types.tag_map.deserialize_json(data["tags"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
