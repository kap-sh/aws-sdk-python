"""Generated from Smithy shape ``com.amazonaws.drs#DeleteReplicationConfigurationTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.replication_configuration_template_id


class DeleteReplicationConfigurationTemplateRequest(TypedDict, closed=True):
    replication_configuration_template_id: "aws_sdk_drs.types.replication_configuration_template_id.ReplicationConfigurationTemplateID"
    """<p>The ID of the Replication Configuration Template to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteReplicationConfigurationTemplateRequest) -> dict:
    out: dict = {}
    out["replicationConfigurationTemplateID"] = value[
        "replication_configuration_template_id"
    ]
    return out


def deserialize_json(data: dict) -> DeleteReplicationConfigurationTemplateRequest:
    out: DeleteReplicationConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
    if "replicationConfigurationTemplateID" in data:
        out["replication_configuration_template_id"] = data[
            "replicationConfigurationTemplateID"
        ]
    else:
        raise DeserializationError(
            "DeleteReplicationConfigurationTemplateRequest.replication_configuration_template_id required"
        )
    return out
