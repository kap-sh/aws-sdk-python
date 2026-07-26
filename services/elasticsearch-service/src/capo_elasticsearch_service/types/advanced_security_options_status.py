"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AdvancedSecurityOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.advanced_security_options
    import capo_elasticsearch_service.types.option_status


class AdvancedSecurityOptionsStatus(TypedDict, closed=True):
    options: "capo_elasticsearch_service.types.advanced_security_options.AdvancedSecurityOptions"
    """<p> Specifies advanced security options for the specified Elasticsearch domain.</p>"""
    status: "capo_elasticsearch_service.types.option_status.OptionStatus"
    """<p> Status of the advanced security options for the specified Elasticsearch domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedSecurityOptionsStatus) -> dict:
    out: dict = {}
    import capo_elasticsearch_service.types.advanced_security_options

    out["Options"] = (
        capo_elasticsearch_service.types.advanced_security_options.serialize_json(
            value["options"]
        )
    )
    import capo_elasticsearch_service.types.option_status

    out["Status"] = capo_elasticsearch_service.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> AdvancedSecurityOptionsStatus:
    out: AdvancedSecurityOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import capo_elasticsearch_service.types.advanced_security_options

        out["options"] = (
            capo_elasticsearch_service.types.advanced_security_options.deserialize_json(
                data["Options"]
            )
        )
    else:
        raise DeserializationError("AdvancedSecurityOptionsStatus.options required")
    if "Status" in data:
        import capo_elasticsearch_service.types.option_status

        out["status"] = capo_elasticsearch_service.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("AdvancedSecurityOptionsStatus.status required")
    return out
