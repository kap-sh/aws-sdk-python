"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#LogPublishingOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.log_publishing_options
    import capo_elasticsearch_service.types.option_status


class LogPublishingOptionsStatus(TypedDict, closed=True):
    options: NotRequired[
        "capo_elasticsearch_service.types.log_publishing_options.LogPublishingOptions"
    ]
    """<p>The log publishing options configured for the Elasticsearch domain.</p>"""
    status: NotRequired["capo_elasticsearch_service.types.option_status.OptionStatus"]
    """<p>The status of the log publishing options for the Elasticsearch domain. See <code>OptionStatus</code> for the status information that's included. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogPublishingOptionsStatus) -> dict:
    out: dict = {}
    if "options" in value:
        import capo_elasticsearch_service.types.log_publishing_options

        out["Options"] = (
            capo_elasticsearch_service.types.log_publishing_options.serialize_json(
                value["options"]
            )
        )
    if "status" in value:
        import capo_elasticsearch_service.types.option_status

        out["Status"] = capo_elasticsearch_service.types.option_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> LogPublishingOptionsStatus:
    out: LogPublishingOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import capo_elasticsearch_service.types.log_publishing_options

        out["options"] = (
            capo_elasticsearch_service.types.log_publishing_options.deserialize_json(
                data["Options"]
            )
        )
    if "Status" in data:
        import capo_elasticsearch_service.types.option_status

        out["status"] = capo_elasticsearch_service.types.option_status.deserialize_json(
            data["Status"]
        )
    return out
