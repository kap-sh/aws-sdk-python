"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AutoTuneOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.auto_tune_options
    import capo_elasticsearch_service.types.auto_tune_status


class AutoTuneOptionsStatus(TypedDict, closed=True):
    options: NotRequired[
        "capo_elasticsearch_service.types.auto_tune_options.AutoTuneOptions"
    ]
    """<p> Specifies Auto-Tune options for the specified Elasticsearch domain.</p>"""
    status: NotRequired[
        "capo_elasticsearch_service.types.auto_tune_status.AutoTuneStatus"
    ]
    """<p> Specifies Status of the Auto-Tune options for the specified Elasticsearch domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneOptionsStatus) -> dict:
    out: dict = {}
    if "options" in value:
        import capo_elasticsearch_service.types.auto_tune_options

        out["Options"] = (
            capo_elasticsearch_service.types.auto_tune_options.serialize_json(
                value["options"]
            )
        )
    if "status" in value:
        import capo_elasticsearch_service.types.auto_tune_status

        out["Status"] = (
            capo_elasticsearch_service.types.auto_tune_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutoTuneOptionsStatus:
    out: AutoTuneOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import capo_elasticsearch_service.types.auto_tune_options

        out["options"] = (
            capo_elasticsearch_service.types.auto_tune_options.deserialize_json(
                data["Options"]
            )
        )
    if "Status" in data:
        import capo_elasticsearch_service.types.auto_tune_status

        out["status"] = (
            capo_elasticsearch_service.types.auto_tune_status.deserialize_json(
                data["Status"]
            )
        )
    return out
