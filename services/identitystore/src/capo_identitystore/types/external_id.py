"""Generated from Smithy shape ``com.amazonaws.identitystore#ExternalId``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.external_id_identifier
    import capo_identitystore.types.external_id_issuer


class ExternalId(TypedDict, closed=True):
    issuer: "capo_identitystore.types.external_id_issuer.ExternalIdIssuer"
    """<p>The issuer for an external identifier.</p>"""
    id: "capo_identitystore.types.external_id_identifier.ExternalIdIdentifier"
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
