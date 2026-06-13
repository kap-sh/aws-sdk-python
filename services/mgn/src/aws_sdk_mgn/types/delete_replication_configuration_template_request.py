"""Generated from Smithy shape ``com.amazonaws.mgn#DeleteReplicationConfigurationTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.replication_configuration_template_id


class DeleteReplicationConfigurationTemplateRequest(TypedDict):
    replication_configuration_template_id: "aws_sdk_mgn.types.replication_configuration_template_id.ReplicationConfigurationTemplateID"
    """<p>Request to delete Replication Configuration Template from service by Replication Configuration Template ID.</p>"""


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
