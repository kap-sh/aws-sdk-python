"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRedshiftClusterHsmStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsRedshiftClusterHsmStatus(TypedDict, closed=True):
    hsm_client_certificate_identifier: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the HSM client certificate that the Amazon Redshift cluster uses to retrieve the data encryption keys that are stored in an HSM.</p>"""
    hsm_configuration_identifier: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the HSM configuration that contains the information that the Amazon Redshift cluster can use to retrieve and store keys in an HSM.</p>"""
    status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.</p> <p>Type: String</p> <p>Valid values: <code>active</code> | <code>applying</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRedshiftClusterHsmStatus) -> dict:
    out: dict = {}
    if "hsm_client_certificate_identifier" in value:
        out["HsmClientCertificateIdentifier"] = value[
            "hsm_client_certificate_identifier"
        ]
    if "hsm_configuration_identifier" in value:
        out["HsmConfigurationIdentifier"] = value["hsm_configuration_identifier"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsRedshiftClusterHsmStatus:
    out: AwsRedshiftClusterHsmStatus = {}  # type: ignore[typeddict-item]
    if "HsmClientCertificateIdentifier" in data:
        out["hsm_client_certificate_identifier"] = data[
            "HsmClientCertificateIdentifier"
        ]
    if "HsmConfigurationIdentifier" in data:
        out["hsm_configuration_identifier"] = data["HsmConfigurationIdentifier"]
    if "Status" in data:
        out["status"] = data["Status"]
    return out
