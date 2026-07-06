"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#GetTrustStoreRevocationContentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.location


class GetTrustStoreRevocationContentOutput(TypedDict, closed=True):
    location: NotRequired["aws_sdk_elastic_load_balancing_v2.types.location.Location"]
    """<p>The revocation files Amazon S3 URI.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetTrustStoreRevocationContentOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "location" in value:
        pairs.append((f"{prefix}.Location", str(value["location"])))


def deserialize_query(el: Element) -> GetTrustStoreRevocationContentOutput:
    out: GetTrustStoreRevocationContentOutput = {}  # type: ignore[typeddict-item]
    child_location = el.find("Location")
    if child_location is not None:
        out["location"] = str(child_location.text or "")
    return out
