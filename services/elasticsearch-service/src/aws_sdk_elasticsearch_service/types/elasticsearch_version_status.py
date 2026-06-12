"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ElasticsearchVersionStatus``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.elasticsearch_version_string
    import aws_sdk_elasticsearch_service.types.option_status


class ElasticsearchVersionStatus(TypedDict):
    options: "aws_sdk_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString"
    """<p> Specifies the Elasticsearch version for the specified Elasticsearch domain.</p>"""
    status: "aws_sdk_elasticsearch_service.types.option_status.OptionStatus"
    """<p> Specifies the status of the Elasticsearch version options for the specified Elasticsearch domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ElasticsearchVersionStatus) -> dict:
    out: dict = {}
    out["Options"] = value["options"]
    import aws_sdk_elasticsearch_service.types.option_status

    out["Status"] = aws_sdk_elasticsearch_service.types.option_status.serialize_json(
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
        import aws_sdk_elasticsearch_service.types.option_status

        out["status"] = (
            aws_sdk_elasticsearch_service.types.option_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("ElasticsearchVersionStatus.status required")
    return out
