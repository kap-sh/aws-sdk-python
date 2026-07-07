"""Generated from Smithy shape ``com.amazonaws.cloudsearch#ListDomainNamesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.domain_name_map


class ListDomainNamesResponse(TypedDict, closed=True):
    domain_names: NotRequired["aws_sdk_cloudsearch.types.domain_name_map.DomainNameMap"]
    """<p>The names of the search domains owned by an account.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListDomainNamesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "domain_names" in value:
        import aws_sdk_cloudsearch.types.domain_name_map

        aws_sdk_cloudsearch.types.domain_name_map.serialize_query(
            value["domain_names"], pairs, f"{prefix}.DomainNames"
        )


def deserialize_query(el: Element) -> ListDomainNamesResponse:
    out: ListDomainNamesResponse = {}  # type: ignore[typeddict-item]
    child_domain_names = el.find("DomainNames")
    if child_domain_names is not None:
        import aws_sdk_cloudsearch.types.domain_name_map

        out["domain_names"] = (
            aws_sdk_cloudsearch.types.domain_name_map.deserialize_query(
                child_domain_names
            )
        )
    return out
