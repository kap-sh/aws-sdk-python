"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#SourceData``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from aws_sdk_rolesanywhere.errors import DeserializationError, SerializationError


class _SourceData_x509CertificateData(TypedDict, closed=True):
    x509CertificateData: "str"


class _SourceData_acmPcaArn(TypedDict, closed=True):
    acmPcaArn: "str"


SourceData: TypeAlias = _SourceData_x509CertificateData | _SourceData_acmPcaArn


# --- restJson1 ser/de ---
def serialize_json(value: SourceData) -> dict:
    if "x509CertificateData" in value:
        return {"x509CertificateData": value["x509CertificateData"]}
    elif "acmPcaArn" in value:
        return {"acmPcaArn": value["acmPcaArn"]}
    else:
        raise SerializationError("SourceData: no variant present")


def deserialize_json(data: dict) -> SourceData:
    if "x509CertificateData" in data:
        return {"x509CertificateData": data["x509CertificateData"]}
    elif "acmPcaArn" in data:
        return {"acmPcaArn": data["acmPcaArn"]}
    else:
        raise DeserializationError("SourceData: no recognized variant key")
