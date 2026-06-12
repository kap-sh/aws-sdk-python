"""Generated from Smithy shape ``com.amazonaws.cloudsearch#UpdateDomainEndpointOptionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.domain_endpoint_options_status


class UpdateDomainEndpointOptionsResponse(TypedDict):
    domain_endpoint_options: NotRequired[
        "aws_sdk_cloudsearch.types.domain_endpoint_options_status.DomainEndpointOptionsStatus"
    ]
    """<p>The newly-configured domain endpoint options.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateDomainEndpointOptionsResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "domain_endpoint_options" in value:
        import aws_sdk_cloudsearch.types.domain_endpoint_options_status

        aws_sdk_cloudsearch.types.domain_endpoint_options_status.serialize_query(
            value["domain_endpoint_options"], pairs, f"{prefix}.DomainEndpointOptions"
        )


def deserialize_query(el: Element) -> UpdateDomainEndpointOptionsResponse:
    out: UpdateDomainEndpointOptionsResponse = {}  # type: ignore[typeddict-item]
    child_domain_endpoint_options = el.find("DomainEndpointOptions")
    if child_domain_endpoint_options is not None:
        import aws_sdk_cloudsearch.types.domain_endpoint_options_status

        out["domain_endpoint_options"] = (
            aws_sdk_cloudsearch.types.domain_endpoint_options_status.deserialize_query(
                child_domain_endpoint_options
            )
        )
    return out
