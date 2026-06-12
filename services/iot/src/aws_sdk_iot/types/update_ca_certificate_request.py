"""Generated from Smithy shape ``com.amazonaws.iot#UpdateCACertificateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.auto_registration_status
    import aws_sdk_iot.types.ca_certificate_status
    import aws_sdk_iot.types.certificate_id
    import aws_sdk_iot.types.registration_config
    import aws_sdk_iot.types.remove_auto_registration


class UpdateCACertificateRequest(TypedDict):
    certificate_id: "aws_sdk_iot.types.certificate_id.CertificateId"
    """<p>The CA certificate identifier.</p>"""
    new_status: NotRequired[
        "aws_sdk_iot.types.ca_certificate_status.CACertificateStatus"
    ]
    """<p>The updated status of the CA certificate.</p> <p> <b>Note:</b> The status value REGISTER_INACTIVE is deprecated and should not be used.</p>"""
    new_auto_registration_status: NotRequired[
        "aws_sdk_iot.types.auto_registration_status.AutoRegistrationStatus"
    ]
    """<p>The new value for the auto registration status. Valid values are: \"ENABLE\" or \"DISABLE\".</p>"""
    registration_config: NotRequired[
        "aws_sdk_iot.types.registration_config.RegistrationConfig"
    ]
    """<p>Information about the registration configuration.</p>"""
    remove_auto_registration: (
        "aws_sdk_iot.types.remove_auto_registration.RemoveAutoRegistration"
    )
    """<p>If true, removes auto registration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCACertificateRequest) -> dict:
    out: dict = {}
    if "registration_config" in value:
        import aws_sdk_iot.types.registration_config

        out["registrationConfig"] = (
            aws_sdk_iot.types.registration_config.serialize_json(
                value["registration_config"]
            )
        )
    out["removeAutoRegistration"] = value.get("remove_auto_registration", False)
    return out


def deserialize_json(data: dict) -> UpdateCACertificateRequest:
    out: UpdateCACertificateRequest = {}  # type: ignore[typeddict-item]
    if "registrationConfig" in data:
        import aws_sdk_iot.types.registration_config

        out["registration_config"] = (
            aws_sdk_iot.types.registration_config.deserialize_json(
                data["registrationConfig"]
            )
        )
    if "removeAutoRegistration" in data:
        out["remove_auto_registration"] = data["removeAutoRegistration"]
    else:
        out["remove_auto_registration"] = False
    return out
