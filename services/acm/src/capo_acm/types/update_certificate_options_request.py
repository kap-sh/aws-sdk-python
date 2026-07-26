"""Generated from Smithy shape ``com.amazonaws.acm#UpdateCertificateOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_acm.types.arn
    import capo_acm.types.certificate_options


class UpdateCertificateOptionsRequest(TypedDict, closed=True):
    certificate_arn: "capo_acm.types.arn.Arn"
    """<p>ARN of the requested certificate to update. This must be of the form:</p> <p> <code>arn:aws:acm:us-east-1:<i>account</i>:certificate/<i>12345678-1234-1234-1234-123456789012</i> </code> </p>"""
    options: "capo_acm.types.certificate_options.CertificateOptions"
    """<p>Use to update the options for your certificate. Currently, you can specify whether to add your certificate to a transparency log or export your certificate. Certificate transparency makes it possible to detect SSL/TLS certificates that have been mistakenly or maliciously issued. Certificates that have not been logged typically produce an error message in a browser. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCertificateOptionsRequest) -> dict:
    out: dict = {}
    out["CertificateArn"] = value["certificate_arn"]
    import capo_acm.types.certificate_options

    out["Options"] = capo_acm.types.certificate_options.serialize_aws_json_1_1(
        value["options"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCertificateOptionsRequest:
    out: UpdateCertificateOptionsRequest = {}  # type: ignore[typeddict-item]
    if "CertificateArn" in data:
        out["certificate_arn"] = data["CertificateArn"]
    else:
        raise DeserializationError(
            "UpdateCertificateOptionsRequest.certificate_arn required"
        )
    if "Options" in data:
        import capo_acm.types.certificate_options

        out["options"] = capo_acm.types.certificate_options.deserialize_aws_json_1_1(
            data["Options"]
        )
    else:
        raise DeserializationError("UpdateCertificateOptionsRequest.options required")
    return out
