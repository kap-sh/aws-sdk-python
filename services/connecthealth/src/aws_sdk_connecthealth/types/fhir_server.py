"""Generated from Smithy shape ``com.amazonaws.connecthealth#FHIRServer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.non_empty_string
    import aws_sdk_connecthealth.types.sensitive_non_empty_string


class FHIRServer(TypedDict, closed=True):
    fhir_endpoint: "aws_sdk_connecthealth.types.non_empty_string.NonEmptyString"
    """<p>FHIR server endpoint URL for accessing patient data.</p>"""
    oauth_token: NotRequired[
        "aws_sdk_connecthealth.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>OAuth token for authenticating with the FHIR server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FHIRServer) -> dict:
    out: dict = {}
    out["fhirEndpoint"] = value["fhir_endpoint"]
    if "oauth_token" in value:
        out["oauthToken"] = value["oauth_token"]
    return out


def deserialize_json(data: dict) -> FHIRServer:
    out: FHIRServer = {}  # type: ignore[typeddict-item]
    if "fhirEndpoint" in data:
        out["fhir_endpoint"] = data["fhirEndpoint"]
    else:
        raise DeserializationError("FHIRServer.fhir_endpoint required")
    if "oauthToken" in data:
        out["oauth_token"] = data["oauthToken"]
    return out
