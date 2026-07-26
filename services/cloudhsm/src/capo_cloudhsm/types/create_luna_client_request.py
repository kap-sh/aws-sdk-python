"""Generated from Smithy shape ``com.amazonaws.cloudhsm#CreateLunaClientRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudhsm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudhsm.types.certificate
    import capo_cloudhsm.types.client_label


class CreateLunaClientRequest(TypedDict, closed=True):
    label: NotRequired["capo_cloudhsm.types.client_label.ClientLabel"]
    """<p>The label for the client.</p>"""
    certificate: "capo_cloudhsm.types.certificate.Certificate"
    """<p>The contents of a Base64-Encoded X.509 v3 certificate to be installed on the HSMs used by this client.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLunaClientRequest) -> dict:
    out: dict = {}
    if "label" in value:
        out["Label"] = value["label"]
    out["Certificate"] = value["certificate"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLunaClientRequest:
    out: CreateLunaClientRequest = {}  # type: ignore[typeddict-item]
    if "Label" in data:
        out["label"] = data["Label"]
    if "Certificate" in data:
        out["certificate"] = data["Certificate"]
    else:
        raise DeserializationError("CreateLunaClientRequest.certificate required")
    return out
