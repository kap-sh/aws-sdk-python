"""Generated from Smithy shape ``com.amazonaws.identitystore#ExternalId``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.external_id_identifier
    import aws_sdk_identitystore.types.external_id_issuer


class ExternalId(TypedDict):
    issuer: "aws_sdk_identitystore.types.external_id_issuer.ExternalIdIssuer"
    """<p>The issuer for an external identifier.</p>"""
    id: "aws_sdk_identitystore.types.external_id_identifier.ExternalIdIdentifier"
    """<p>The identifier issued to this resource by an external identity provider.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExternalId) -> dict:
    out: dict = {}
    out["Issuer"] = value["issuer"]
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExternalId:
    out: ExternalId = {}  # type: ignore[typeddict-item]
    if "Issuer" in data:
        out["issuer"] = data["Issuer"]
    else:
        raise DeserializationError("ExternalId.issuer required")
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("ExternalId.id required")
    return out
