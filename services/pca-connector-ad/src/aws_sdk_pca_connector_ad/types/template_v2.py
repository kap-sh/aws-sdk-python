"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#TemplateV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pca_connector_ad.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pca_connector_ad.types.certificate_validity
    import aws_sdk_pca_connector_ad.types.enrollment_flags_v2
    import aws_sdk_pca_connector_ad.types.extensions_v2
    import aws_sdk_pca_connector_ad.types.general_flags_v2
    import aws_sdk_pca_connector_ad.types.private_key_attributes_v2
    import aws_sdk_pca_connector_ad.types.private_key_flags_v2
    import aws_sdk_pca_connector_ad.types.subject_name_flags_v2
    import aws_sdk_pca_connector_ad.types.template_name_list


class TemplateV2(TypedDict, closed=True):
    certificate_validity: (
        "aws_sdk_pca_connector_ad.types.certificate_validity.CertificateValidity"
    )
    """<p>Certificate validity describes the validity and renewal periods of a certificate.</p>"""
    superseded_templates: NotRequired[
        "aws_sdk_pca_connector_ad.types.template_name_list.TemplateNameList"
    ]
    """<p>List of templates in Active Directory that are superseded by this template.</p>"""
    private_key_attributes: "aws_sdk_pca_connector_ad.types.private_key_attributes_v2.PrivateKeyAttributesV2"
    """<p>Private key attributes allow you to specify the minimal key length, key spec, and cryptographic providers for the private key of a certificate for v2 templates. V2 templates allow you to use Legacy Cryptographic Service Providers.</p>"""
    private_key_flags: (
        "aws_sdk_pca_connector_ad.types.private_key_flags_v2.PrivateKeyFlagsV2"
    )
    """<p>Private key flags for v2 templates specify the client compatibility, if the private key can be exported, and if user input is required when using a private key. </p>"""
    enrollment_flags: (
        "aws_sdk_pca_connector_ad.types.enrollment_flags_v2.EnrollmentFlagsV2"
    )
    """<p>Enrollment flags describe the enrollment settings for certificates such as using the existing private key and deleting expired or revoked certificates.</p>"""
    subject_name_flags: (
        "aws_sdk_pca_connector_ad.types.subject_name_flags_v2.SubjectNameFlagsV2"
    )
    """<p>Subject name flags describe the subject name and subject alternate name that is included in a certificate.</p>"""
    general_flags: "aws_sdk_pca_connector_ad.types.general_flags_v2.GeneralFlagsV2"
    """<p>General flags describe whether the template is used for computers or users and if the template can be used with autoenrollment.</p>"""
    extensions: "aws_sdk_pca_connector_ad.types.extensions_v2.ExtensionsV2"
    """<p>Extensions describe the key usage extensions and application policies for a template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateV2) -> dict:
    out: dict = {}
    import aws_sdk_pca_connector_ad.types.certificate_validity

    out["CertificateValidity"] = (
        aws_sdk_pca_connector_ad.types.certificate_validity.serialize_json(
            value["certificate_validity"]
        )
    )
    if "superseded_templates" in value:
        import aws_sdk_pca_connector_ad.types.template_name_list

        out["SupersededTemplates"] = (
            aws_sdk_pca_connector_ad.types.template_name_list.serialize_json(
                value["superseded_templates"]
            )
        )
    import aws_sdk_pca_connector_ad.types.private_key_attributes_v2

    out["PrivateKeyAttributes"] = (
        aws_sdk_pca_connector_ad.types.private_key_attributes_v2.serialize_json(
            value["private_key_attributes"]
        )
    )
    import aws_sdk_pca_connector_ad.types.private_key_flags_v2

    out["PrivateKeyFlags"] = (
        aws_sdk_pca_connector_ad.types.private_key_flags_v2.serialize_json(
            value["private_key_flags"]
        )
    )
    import aws_sdk_pca_connector_ad.types.enrollment_flags_v2

    out["EnrollmentFlags"] = (
        aws_sdk_pca_connector_ad.types.enrollment_flags_v2.serialize_json(
            value["enrollment_flags"]
        )
    )
    import aws_sdk_pca_connector_ad.types.subject_name_flags_v2

    out["SubjectNameFlags"] = (
        aws_sdk_pca_connector_ad.types.subject_name_flags_v2.serialize_json(
            value["subject_name_flags"]
        )
    )
    import aws_sdk_pca_connector_ad.types.general_flags_v2

    out["GeneralFlags"] = (
        aws_sdk_pca_connector_ad.types.general_flags_v2.serialize_json(
            value["general_flags"]
        )
    )
    import aws_sdk_pca_connector_ad.types.extensions_v2

    out["Extensions"] = aws_sdk_pca_connector_ad.types.extensions_v2.serialize_json(
        value["extensions"]
    )
    return out


def deserialize_json(data: dict) -> TemplateV2:
    out: TemplateV2 = {}  # type: ignore[typeddict-item]
    if "CertificateValidity" in data:
        import aws_sdk_pca_connector_ad.types.certificate_validity

        out["certificate_validity"] = (
            aws_sdk_pca_connector_ad.types.certificate_validity.deserialize_json(
                data["CertificateValidity"]
            )
        )
    else:
        raise DeserializationError("TemplateV2.certificate_validity required")
    if "SupersededTemplates" in data:
        import aws_sdk_pca_connector_ad.types.template_name_list

        out["superseded_templates"] = (
            aws_sdk_pca_connector_ad.types.template_name_list.deserialize_json(
                data["SupersededTemplates"]
            )
        )
    if "PrivateKeyAttributes" in data:
        import aws_sdk_pca_connector_ad.types.private_key_attributes_v2

        out["private_key_attributes"] = (
            aws_sdk_pca_connector_ad.types.private_key_attributes_v2.deserialize_json(
                data["PrivateKeyAttributes"]
            )
        )
    else:
        raise DeserializationError("TemplateV2.private_key_attributes required")
    if "PrivateKeyFlags" in data:
        import aws_sdk_pca_connector_ad.types.private_key_flags_v2

        out["private_key_flags"] = (
            aws_sdk_pca_connector_ad.types.private_key_flags_v2.deserialize_json(
                data["PrivateKeyFlags"]
            )
        )
    else:
        raise DeserializationError("TemplateV2.private_key_flags required")
    if "EnrollmentFlags" in data:
        import aws_sdk_pca_connector_ad.types.enrollment_flags_v2

        out["enrollment_flags"] = (
            aws_sdk_pca_connector_ad.types.enrollment_flags_v2.deserialize_json(
                data["EnrollmentFlags"]
            )
        )
    else:
        raise DeserializationError("TemplateV2.enrollment_flags required")
    if "SubjectNameFlags" in data:
        import aws_sdk_pca_connector_ad.types.subject_name_flags_v2

        out["subject_name_flags"] = (
            aws_sdk_pca_connector_ad.types.subject_name_flags_v2.deserialize_json(
                data["SubjectNameFlags"]
            )
        )
    else:
        raise DeserializationError("TemplateV2.subject_name_flags required")
    if "GeneralFlags" in data:
        import aws_sdk_pca_connector_ad.types.general_flags_v2

        out["general_flags"] = (
            aws_sdk_pca_connector_ad.types.general_flags_v2.deserialize_json(
                data["GeneralFlags"]
            )
        )
    else:
        raise DeserializationError("TemplateV2.general_flags required")
    if "Extensions" in data:
        import aws_sdk_pca_connector_ad.types.extensions_v2

        out["extensions"] = (
            aws_sdk_pca_connector_ad.types.extensions_v2.deserialize_json(
                data["Extensions"]
            )
        )
    else:
        raise DeserializationError("TemplateV2.extensions required")
    return out
