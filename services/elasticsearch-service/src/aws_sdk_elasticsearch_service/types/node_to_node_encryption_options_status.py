"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#NodeToNodeEncryptionOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.node_to_node_encryption_options
    import aws_sdk_elasticsearch_service.types.option_status


class NodeToNodeEncryptionOptionsStatus(TypedDict, closed=True):
    options: "aws_sdk_elasticsearch_service.types.node_to_node_encryption_options.NodeToNodeEncryptionOptions"
    """<p>Specifies the node-to-node encryption options for the specified Elasticsearch domain.</p>"""
    status: "aws_sdk_elasticsearch_service.types.option_status.OptionStatus"
    """<p>Specifies the status of the node-to-node encryption options for the specified Elasticsearch domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeToNodeEncryptionOptionsStatus) -> dict:
    out: dict = {}
    import aws_sdk_elasticsearch_service.types.node_to_node_encryption_options

    out["Options"] = (
        aws_sdk_elasticsearch_service.types.node_to_node_encryption_options.serialize_json(
            value["options"]
        )
    )
    import aws_sdk_elasticsearch_service.types.option_status

    out["Status"] = aws_sdk_elasticsearch_service.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> NodeToNodeEncryptionOptionsStatus:
    out: NodeToNodeEncryptionOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_elasticsearch_service.types.node_to_node_encryption_options

        out["options"] = (
            aws_sdk_elasticsearch_service.types.node_to_node_encryption_options.deserialize_json(
                data["Options"]
            )
        )
    else:
        raise DeserializationError("NodeToNodeEncryptionOptionsStatus.options required")
    if "Status" in data:
        import aws_sdk_elasticsearch_service.types.option_status

        out["status"] = (
            aws_sdk_elasticsearch_service.types.option_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("NodeToNodeEncryptionOptionsStatus.status required")
    return out
