"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DomainEndpointOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudsearch.types.domain_endpoint_options
    import capo_cloudsearch.types.option_status


class DomainEndpointOptionsStatus(TypedDict, closed=True):
    options: "capo_cloudsearch.types.domain_endpoint_options.DomainEndpointOptions"
    """<p>The domain endpoint options configured for the domain.</p>"""
    status: "capo_cloudsearch.types.option_status.OptionStatus"
    """<p>The status of the configured domain endpoint options.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DomainEndpointOptionsStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_cloudsearch.types.domain_endpoint_options

    capo_cloudsearch.types.domain_endpoint_options.serialize_query(
        value["options"], pairs, f"{key_prefix}Options"
    )
    import capo_cloudsearch.types.option_status

    capo_cloudsearch.types.option_status.serialize_query(
        value["status"], pairs, f"{key_prefix}Status"
    )


def deserialize_query(el: Element) -> DomainEndpointOptionsStatus:
    out: DomainEndpointOptionsStatus = {}  # type: ignore[typeddict-item]
    child_options = el.find("Options")
    if child_options is not None:
        import capo_cloudsearch.types.domain_endpoint_options

        out["options"] = (
            capo_cloudsearch.types.domain_endpoint_options.deserialize_query(
                child_options
            )
        )
    else:
        raise DeserializationError("DomainEndpointOptionsStatus.options required")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudsearch.types.option_status

        out["status"] = capo_cloudsearch.types.option_status.deserialize_query(
            child_status
        )
    else:
        raise DeserializationError("DomainEndpointOptionsStatus.status required")
    return out
