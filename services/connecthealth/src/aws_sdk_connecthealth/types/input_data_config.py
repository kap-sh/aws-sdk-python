"""Generated from Smithy shape ``com.amazonaws.connecthealth#InputDataConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.fhir_server
    import aws_sdk_connecthealth.types.s3_sources


class InputDataConfig(TypedDict, closed=True):
    fhir_server: NotRequired["aws_sdk_connecthealth.types.fhir_server.FHIRServer"]
    """<p>FHIR server configuration to retrieve patient data.</p>"""
    s3_sources: NotRequired["aws_sdk_connecthealth.types.s3_sources.S3Sources"]
    """<p>List of S3 sources containing patient data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputDataConfig) -> dict:
    out: dict = {}
    if "fhir_server" in value:
        import aws_sdk_connecthealth.types.fhir_server

        out["fhirServer"] = aws_sdk_connecthealth.types.fhir_server.serialize_json(
            value["fhir_server"]
        )
    if "s3_sources" in value:
        import aws_sdk_connecthealth.types.s3_sources

        out["s3Sources"] = aws_sdk_connecthealth.types.s3_sources.serialize_json(
            value["s3_sources"]
        )
    return out


def deserialize_json(data: dict) -> InputDataConfig:
    out: InputDataConfig = {}  # type: ignore[typeddict-item]
    if "fhirServer" in data:
        import aws_sdk_connecthealth.types.fhir_server

        out["fhir_server"] = aws_sdk_connecthealth.types.fhir_server.deserialize_json(
            data["fhirServer"]
        )
    if "s3Sources" in data:
        import aws_sdk_connecthealth.types.s3_sources

        out["s3_sources"] = aws_sdk_connecthealth.types.s3_sources.deserialize_json(
            data["s3Sources"]
        )
    return out
