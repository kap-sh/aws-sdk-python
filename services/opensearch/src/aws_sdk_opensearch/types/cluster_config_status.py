"""Generated from Smithy shape ``com.amazonaws.opensearch#ClusterConfigStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.cluster_config
    import aws_sdk_opensearch.types.option_status


class ClusterConfigStatus(TypedDict, closed=True):
    options: "aws_sdk_opensearch.types.cluster_config.ClusterConfig"
    """<p>Cluster configuration options for the specified domain.</p>"""
    status: "aws_sdk_opensearch.types.option_status.OptionStatus"
    """<p>The status of cluster configuration options for the specified domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterConfigStatus) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.cluster_config

    out["Options"] = aws_sdk_opensearch.types.cluster_config.serialize_json(
        value["options"]
    )
    import aws_sdk_opensearch.types.option_status

    out["Status"] = aws_sdk_opensearch.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> ClusterConfigStatus:
    out: ClusterConfigStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import aws_sdk_opensearch.types.cluster_config

        out["options"] = aws_sdk_opensearch.types.cluster_config.deserialize_json(
            data["Options"]
        )
    else:
        raise DeserializationError("ClusterConfigStatus.options required")
    if "Status" in data:
        import aws_sdk_opensearch.types.option_status

        out["status"] = aws_sdk_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("ClusterConfigStatus.status required")
    return out
