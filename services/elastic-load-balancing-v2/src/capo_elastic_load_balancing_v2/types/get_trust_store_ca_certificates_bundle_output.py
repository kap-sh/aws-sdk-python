"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#GetTrustStoreCaCertificatesBundleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.location


class GetTrustStoreCaCertificatesBundleOutput(TypedDict, closed=True):
    location: NotRequired["capo_elastic_load_balancing_v2.types.location.Location"]
    """<p>The ca certificate bundles Amazon S3 URI.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetTrustStoreCaCertificatesBundleOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "location" in value:
        pairs.append((f"{prefix}.Location", str(value["location"])))


def deserialize_query(el: Element) -> GetTrustStoreCaCertificatesBundleOutput:
    out: GetTrustStoreCaCertificatesBundleOutput = {}  # type: ignore[typeddict-item]
    child_location = el.find("Location")
    if child_location is not None:
        out["location"] = str(child_location.text or "")
    return out
