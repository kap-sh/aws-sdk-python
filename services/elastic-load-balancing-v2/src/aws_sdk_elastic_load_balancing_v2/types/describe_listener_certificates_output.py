"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#DescribeListenerCertificatesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.certificate_list
    import aws_sdk_elastic_load_balancing_v2.types.marker


class DescribeListenerCertificatesOutput(TypedDict):
    certificates: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.certificate_list.CertificateList"
    ]
    """<p>Information about the certificates.</p>"""
    next_marker: NotRequired["aws_sdk_elastic_load_balancing_v2.types.marker.Marker"]
    """<p>If there are additional results, this is the marker for the next set of results. Otherwise, this is null.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeListenerCertificatesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "certificates" in value:
        import aws_sdk_elastic_load_balancing_v2.types.certificate_list

        aws_sdk_elastic_load_balancing_v2.types.certificate_list.serialize_query(
            value["certificates"], pairs, f"{prefix}.Certificates"
        )
    if "next_marker" in value:
        pairs.append((f"{prefix}.NextMarker", str(value["next_marker"])))


def deserialize_query(el: Element) -> DescribeListenerCertificatesOutput:
    out: DescribeListenerCertificatesOutput = {}  # type: ignore[typeddict-item]
    child_certificates = el.find("Certificates")
    if child_certificates is not None:
        import aws_sdk_elastic_load_balancing_v2.types.certificate_list

        out["certificates"] = (
            aws_sdk_elastic_load_balancing_v2.types.certificate_list.deserialize_query(
                child_certificates
            )
        )
    child_next_marker = el.find("NextMarker")
    if child_next_marker is not None:
        out["next_marker"] = str(child_next_marker.text or "")
    return out
