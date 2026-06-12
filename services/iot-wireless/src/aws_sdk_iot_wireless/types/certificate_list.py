"""Generated from Smithy shape ``com.amazonaws.iotwireless#CertificateList``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.certificate_value
    import aws_sdk_iot_wireless.types.signing_alg


class CertificateList(TypedDict):
    signing_alg: "aws_sdk_iot_wireless.types.signing_alg.SigningAlg"
    """<p>The certificate chain algorithm provided by sidewalk.</p>"""
    value: "aws_sdk_iot_wireless.types.certificate_value.CertificateValue"
    """<p>The value of the chosen sidewalk certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CertificateList) -> dict:
    out: dict = {}
    import aws_sdk_iot_wireless.types.signing_alg

    out["SigningAlg"] = aws_sdk_iot_wireless.types.signing_alg.serialize_json(
        value["signing_alg"]
    )
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> CertificateList:
    out: CertificateList = {}  # type: ignore[typeddict-item]
    if "SigningAlg" in data:
        import aws_sdk_iot_wireless.types.signing_alg

        out["signing_alg"] = aws_sdk_iot_wireless.types.signing_alg.deserialize_json(
            data["SigningAlg"]
        )
    else:
        raise DeserializationError("CertificateList.signing_alg required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("CertificateList.value required")
    return out
