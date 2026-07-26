"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ListDomainNamesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.domain_info_list


class ListDomainNamesResponse(TypedDict, closed=True):
    domain_names: NotRequired[
        "capo_elasticsearch_service.types.domain_info_list.DomainInfoList"
    ]
    """<p>List of domain names and respective engine types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainNamesResponse) -> dict:
    out: dict = {}
    if "domain_names" in value:
        import capo_elasticsearch_service.types.domain_info_list

        out["DomainNames"] = (
            capo_elasticsearch_service.types.domain_info_list.serialize_json(
                value["domain_names"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListDomainNamesResponse:
    out: ListDomainNamesResponse = {}  # type: ignore[typeddict-item]
    if "DomainNames" in data:
        import capo_elasticsearch_service.types.domain_info_list

        out["domain_names"] = (
            capo_elasticsearch_service.types.domain_info_list.deserialize_json(
                data["DomainNames"]
            )
        )
    return out
