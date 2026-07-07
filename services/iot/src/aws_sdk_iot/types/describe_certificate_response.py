"""Generated from Smithy shape ``com.amazonaws.iot#DescribeCertificateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_description


class DescribeCertificateResponse(TypedDict, closed=True):
    certificate_description: NotRequired[
        "aws_sdk_iot.types.certificate_description.CertificateDescription"
    ]
    """<p>The description of the certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCertificateResponse) -> dict:
    out: dict = {}
    if "certificate_description" in value:
        import aws_sdk_iot.types.certificate_description

        out["certificateDescription"] = (
            aws_sdk_iot.types.certificate_description.serialize_json(
                value["certificate_description"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeCertificateResponse:
    out: DescribeCertificateResponse = {}  # type: ignore[typeddict-item]
    if "certificateDescription" in data:
        import aws_sdk_iot.types.certificate_description

        out["certificate_description"] = (
            aws_sdk_iot.types.certificate_description.deserialize_json(
                data["certificateDescription"]
            )
        )
    return out
