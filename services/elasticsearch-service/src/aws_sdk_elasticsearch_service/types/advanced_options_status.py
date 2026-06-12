"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AdvancedOptionsStatus``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.advanced_options
    import aws_sdk_elasticsearch_service.types.option_status


class AdvancedOptionsStatus(TypedDict):
    options: "aws_sdk_elasticsearch_service.types.advanced_options.AdvancedOptions"
    """<p> Specifies the status of advanced options for the specified Elasticsearch domain.</p>"""
    status: "aws_sdk_elasticsearch_service.types.option_status.OptionStatus"
    """<p> Specifies the status of <code>OptionStatus</code> for advanced options for the specified Elasticsearch domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedOptionsStatus) -> dict:
    out: dict = {}
    import aws_sdk_elasticsearch_service.types.advanced_options

    out["Options"] = (
        aws_sdk_elasticsearch_service.types.advanced_options.serialize_json(
            value["options"]
        )
    )
    import aws_sdk_elasticsearch_service.types.option_status

    out["Status"] = aws_sdk_elasticsearch_service.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> AdvancedOptionsStatus:
    out: AdvancedOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_elasticsearch_service.types.advanced_options

        out["options"] = (
            aws_sdk_elasticsearch_service.types.advanced_options.deserialize_json(
                data["Options"]
            )
        )
    else:
        raise DeserializationError("AdvancedOptionsStatus.options required")
    if "Status" in data:
        import aws_sdk_elasticsearch_service.types.option_status

        out["status"] = (
            aws_sdk_elasticsearch_service.types.option_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("AdvancedOptionsStatus.status required")
    return out
