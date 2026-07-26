"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ElasticsearchVersionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.elasticsearch_version_string
    import capo_elasticsearch_service.types.option_status


class ElasticsearchVersionStatus(TypedDict, closed=True):
    options: "capo_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString"
    """<p> Specifies the Elasticsearch version for the specified Elasticsearch domain.</p>"""
    status: "capo_elasticsearch_service.types.option_status.OptionStatus"
    """<p> Specifies the status of the Elasticsearch version options for the specified Elasticsearch domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ElasticsearchVersionStatus) -> dict:
    out: dict = {}
    out["Options"] = value["options"]
    import capo_elasticsearch_service.types.option_status

    out["Status"] = capo_elasticsearch_service.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> ElasticsearchVersionStatus:
    out: ElasticsearchVersionStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        out["options"] = data["Options"]
    else:
        raise DeserializationError("ElasticsearchVersionStatus.options required")
    if "Status" in data:
        import capo_elasticsearch_service.types.option_status

        out["status"] = capo_elasticsearch_service.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("ElasticsearchVersionStatus.status required")
    return out
