"""Generated from Smithy shape ``com.amazonaws.iot#RegisterThingResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_pem
    import aws_sdk_iot.types.resource_arns


class RegisterThingResponse(TypedDict):
    certificate_pem: NotRequired["aws_sdk_iot.types.certificate_pem.CertificatePem"]
    """<p>The certificate data, in PEM format.</p>"""
    resource_arns: NotRequired["aws_sdk_iot.types.resource_arns.ResourceArns"]
    """<p>ARNs for the generated resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterThingResponse) -> dict:
    out: dict = {}
    if "certificate_pem" in value:
        out["certificatePem"] = value["certificate_pem"]
    if "resource_arns" in value:
        import aws_sdk_iot.types.resource_arns

        out["resourceArns"] = aws_sdk_iot.types.resource_arns.serialize_json(
            value["resource_arns"]
        )
    return out


def deserialize_json(data: dict) -> RegisterThingResponse:
    out: RegisterThingResponse = {}  # type: ignore[typeddict-item]
    if "certificatePem" in data:
        out["certificate_pem"] = data["certificatePem"]
    if "resourceArns" in data:
        import aws_sdk_iot.types.resource_arns

        out["resource_arns"] = aws_sdk_iot.types.resource_arns.deserialize_json(
            data["resourceArns"]
        )
    return out
