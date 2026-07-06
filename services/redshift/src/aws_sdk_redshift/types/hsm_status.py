"""Generated from Smithy shape ``com.amazonaws.redshift#HsmStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class HsmStatus(TypedDict, closed=True):
    hsm_client_certificate_identifier: NotRequired[
        "aws_sdk_redshift.types.string.String"
    ]
    """<p>Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.</p>"""
    hsm_configuration_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.</p>"""
    status: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.</p> <p>Values: active, applying</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: HsmStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "hsm_client_certificate_identifier" in value:
        pairs.append(
            (
                f"{prefix}.HsmClientCertificateIdentifier",
                str(value["hsm_client_certificate_identifier"]),
            )
        )
    if "hsm_configuration_identifier" in value:
        pairs.append(
            (
                f"{prefix}.HsmConfigurationIdentifier",
                str(value["hsm_configuration_identifier"]),
            )
        )
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))


def deserialize_query(el: Element) -> HsmStatus:
    out: HsmStatus = {}  # type: ignore[typeddict-item]
    child_hsm_client_certificate_identifier = el.find("HsmClientCertificateIdentifier")
    if child_hsm_client_certificate_identifier is not None:
        out["hsm_client_certificate_identifier"] = str(
            child_hsm_client_certificate_identifier.text or ""
        )
    child_hsm_configuration_identifier = el.find("HsmConfigurationIdentifier")
    if child_hsm_configuration_identifier is not None:
        out["hsm_configuration_identifier"] = str(
            child_hsm_configuration_identifier.text or ""
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
