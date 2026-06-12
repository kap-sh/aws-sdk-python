"""Generated from Smithy shape ``com.amazonaws.taxsettings#DeleteSupplementalTaxRegistrationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_taxsettings.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.generic_string

class DeleteSupplementalTaxRegistrationRequest(TypedDict):
    authority_id: "aws_sdk_taxsettings.types.generic_string.GenericString"
    """<p> The unique authority Id for the supplemental TRN information that needs to be deleted. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteSupplementalTaxRegistrationRequest) -> dict:
    out: dict = {}
    out["authorityId"] = value["authority_id"]
    return out


def deserialize_json(data: dict) -> DeleteSupplementalTaxRegistrationRequest:
    out: DeleteSupplementalTaxRegistrationRequest = {}  # type: ignore[typeddict-item]
    if "authorityId" in data:
        out["authority_id"] = data["authorityId"]
    else:
        raise DeserializationError("DeleteSupplementalTaxRegistrationRequest.authority_id required")
    return out