"""Generated from Smithy shape ``com.amazonaws.iot#DescribeCACertificateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.ca_certificate_description
    import capo_iot.types.registration_config


class DescribeCACertificateResponse(TypedDict, closed=True):
    certificate_description: NotRequired[
        "capo_iot.types.ca_certificate_description.CACertificateDescription"
    ]
    """<p>The CA certificate description.</p>"""
    registration_config: NotRequired[
        "capo_iot.types.registration_config.RegistrationConfig"
    ]
    """<p>Information about the registration configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCACertificateResponse) -> dict:
    out: dict = {}
    if "certificate_description" in value:
        import capo_iot.types.ca_certificate_description

        out["certificateDescription"] = (
            capo_iot.types.ca_certificate_description.serialize_json(
                value["certificate_description"]
            )
        )
    if "registration_config" in value:
        import capo_iot.types.registration_config

        out["registrationConfig"] = capo_iot.types.registration_config.serialize_json(
            value["registration_config"]
        )
    return out


def deserialize_json(data: dict) -> DescribeCACertificateResponse:
    out: DescribeCACertificateResponse = {}  # type: ignore[typeddict-item]
    if "certificateDescription" in data:
        import capo_iot.types.ca_certificate_description

        out["certificate_description"] = (
            capo_iot.types.ca_certificate_description.deserialize_json(
                data["certificateDescription"]
            )
        )
    if "registrationConfig" in data:
        import capo_iot.types.registration_config

        out["registration_config"] = (
            capo_iot.types.registration_config.deserialize_json(
                data["registrationConfig"]
            )
        )
    return out
