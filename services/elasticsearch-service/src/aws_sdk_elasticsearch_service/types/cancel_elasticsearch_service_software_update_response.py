"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#CancelElasticsearchServiceSoftwareUpdateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.service_software_options


class CancelElasticsearchServiceSoftwareUpdateResponse(TypedDict):
    service_software_options: NotRequired[
        "aws_sdk_elasticsearch_service.types.service_software_options.ServiceSoftwareOptions"
    ]
    """<p>The current status of the Elasticsearch service software update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelElasticsearchServiceSoftwareUpdateResponse) -> dict:
    out: dict = {}
    if "service_software_options" in value:
        import aws_sdk_elasticsearch_service.types.service_software_options

        out["ServiceSoftwareOptions"] = (
            aws_sdk_elasticsearch_service.types.service_software_options.serialize_json(
                value["service_software_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> CancelElasticsearchServiceSoftwareUpdateResponse:
    out: CancelElasticsearchServiceSoftwareUpdateResponse = {}  # type: ignore[typeddict-item]
    if "ServiceSoftwareOptions" in data:
        import aws_sdk_elasticsearch_service.types.service_software_options

        out["service_software_options"] = (
            aws_sdk_elasticsearch_service.types.service_software_options.deserialize_json(
                data["ServiceSoftwareOptions"]
            )
        )
    return out
