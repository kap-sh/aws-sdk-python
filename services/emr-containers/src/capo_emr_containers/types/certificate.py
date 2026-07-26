"""Generated from Smithy shape ``com.amazonaws.emrcontainers#Certificate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.acm_cert_arn
    import capo_emr_containers.types.base64_encoded


class Certificate(TypedDict, closed=True):
    certificate_arn: NotRequired["capo_emr_containers.types.acm_cert_arn.ACMCertArn"]
    """<p>The ARN of the certificate generated for managed endpoint.</p>"""
    certificate_data: NotRequired[
        "capo_emr_containers.types.base64_encoded.Base64Encoded"
    ]
    """<p>The base64 encoded PEM certificate data generated for managed endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Certificate) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "certificate_data" in value:
        out["certificateData"] = value["certificate_data"]
    return out


def deserialize_json(data: dict) -> Certificate:
    out: Certificate = {}  # type: ignore[typeddict-item]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "certificateData" in data:
        out["certificate_data"] = data["certificateData"]
    return out
