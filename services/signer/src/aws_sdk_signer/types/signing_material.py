"""Generated from Smithy shape ``com.amazonaws.signer#SigningMaterial``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_signer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_signer.types.certificate_arn


class SigningMaterial(TypedDict):
    certificate_arn: "aws_sdk_signer.types.certificate_arn.CertificateArn"
    """<p>The Amazon Resource Name (ARN) of the certificates that is used to sign your code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SigningMaterial) -> dict:
    out: dict = {}
    out["certificateArn"] = value["certificate_arn"]
    return out


def deserialize_json(data: dict) -> SigningMaterial:
    out: SigningMaterial = {}  # type: ignore[typeddict-item]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    else:
        raise DeserializationError("SigningMaterial.certificate_arn required")
    return out
