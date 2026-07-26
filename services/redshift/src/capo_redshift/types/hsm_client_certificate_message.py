"""Generated from Smithy shape ``com.amazonaws.redshift#HsmClientCertificateMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.hsm_client_certificate_list
    import capo_redshift.types.string


class HsmClientCertificateMessage(TypedDict, closed=True):
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""
    hsm_client_certificates: NotRequired[
        "capo_redshift.types.hsm_client_certificate_list.HsmClientCertificateList"
    ]
    """<p>A list of the identifiers for one or more HSM client certificates used by Amazon Redshift clusters to store and retrieve database encryption keys in an HSM.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: HsmClientCertificateMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "hsm_client_certificates" in value:
        import capo_redshift.types.hsm_client_certificate_list

        capo_redshift.types.hsm_client_certificate_list.serialize_query(
            value["hsm_client_certificates"], pairs, f"{prefix}.HsmClientCertificates"
        )


def deserialize_query(el: Element) -> HsmClientCertificateMessage:
    out: HsmClientCertificateMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_hsm_client_certificates = el.find("HsmClientCertificates")
    if child_hsm_client_certificates is not None:
        import capo_redshift.types.hsm_client_certificate_list

        out["hsm_client_certificates"] = (
            capo_redshift.types.hsm_client_certificate_list.deserialize_query(
                child_hsm_client_certificates
            )
        )
    return out
