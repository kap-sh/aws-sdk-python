"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DescribeDomainEndpointOptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.domain_endpoint_options_status


class DescribeDomainEndpointOptionsResponse(TypedDict, closed=True):
    domain_endpoint_options: NotRequired[
        "capo_cloudsearch.types.domain_endpoint_options_status.DomainEndpointOptionsStatus"
    ]
    """<p>The status and configuration of a search domain's endpoint options.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDomainEndpointOptionsResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "domain_endpoint_options" in value:
        import capo_cloudsearch.types.domain_endpoint_options_status

        capo_cloudsearch.types.domain_endpoint_options_status.serialize_query(
            value["domain_endpoint_options"], pairs, f"{prefix}.DomainEndpointOptions"
        )


def deserialize_query(el: Element) -> DescribeDomainEndpointOptionsResponse:
    out: DescribeDomainEndpointOptionsResponse = {}  # type: ignore[typeddict-item]
    child_domain_endpoint_options = el.find("DomainEndpointOptions")
    if child_domain_endpoint_options is not None:
        import capo_cloudsearch.types.domain_endpoint_options_status

        out["domain_endpoint_options"] = (
            capo_cloudsearch.types.domain_endpoint_options_status.deserialize_query(
                child_domain_endpoint_options
            )
        )
    return out
