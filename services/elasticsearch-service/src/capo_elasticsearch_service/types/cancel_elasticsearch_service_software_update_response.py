"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#CancelElasticsearchServiceSoftwareUpdateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.service_software_options


class CancelElasticsearchServiceSoftwareUpdateResponse(TypedDict, closed=True):
    service_software_options: NotRequired[
        "capo_elasticsearch_service.types.service_software_options.ServiceSoftwareOptions"
    ]
    """<p>The current status of the Elasticsearch service software update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelElasticsearchServiceSoftwareUpdateResponse) -> dict:
    out: dict = {}
    if "service_software_options" in value:
        import capo_elasticsearch_service.types.service_software_options

        out["ServiceSoftwareOptions"] = (
            capo_elasticsearch_service.types.service_software_options.serialize_json(
                value["service_software_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> CancelElasticsearchServiceSoftwareUpdateResponse:
    out: CancelElasticsearchServiceSoftwareUpdateResponse = {}  # type: ignore[typeddict-item]
    if "ServiceSoftwareOptions" in data:
        import capo_elasticsearch_service.types.service_software_options

        out["service_software_options"] = (
            capo_elasticsearch_service.types.service_software_options.deserialize_json(
                data["ServiceSoftwareOptions"]
            )
        )
    return out
