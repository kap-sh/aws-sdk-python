"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#EBSOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.ebs_options
    import aws_sdk_elasticsearch_service.types.option_status


class EBSOptionsStatus(TypedDict, closed=True):
    options: "aws_sdk_elasticsearch_service.types.ebs_options.EBSOptions"
    """<p> Specifies the EBS options for the specified Elasticsearch domain.</p>"""
    status: "aws_sdk_elasticsearch_service.types.option_status.OptionStatus"
    """<p> Specifies the status of the EBS options for the specified Elasticsearch domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EBSOptionsStatus) -> dict:
    out: dict = {}
    import aws_sdk_elasticsearch_service.types.ebs_options

    out["Options"] = aws_sdk_elasticsearch_service.types.ebs_options.serialize_json(
        value["options"]
    )
    import aws_sdk_elasticsearch_service.types.option_status

    out["Status"] = aws_sdk_elasticsearch_service.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> EBSOptionsStatus:
    out: EBSOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_elasticsearch_service.types.ebs_options

        out["options"] = (
            aws_sdk_elasticsearch_service.types.ebs_options.deserialize_json(
                data["Options"]
            )
        )
    else:
        raise DeserializationError("EBSOptionsStatus.options required")
    if "Status" in data:
        import aws_sdk_elasticsearch_service.types.option_status

        out["status"] = (
            aws_sdk_elasticsearch_service.types.option_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("EBSOptionsStatus.status required")
    return out
