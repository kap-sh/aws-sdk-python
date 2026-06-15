"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateRegistryRecordResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.registry_record_arn
    import aws_sdk_bedrock_agentcore_control.types.registry_record_status


class CreateRegistryRecordResponse(TypedDict):
    record_arn: (
        "aws_sdk_bedrock_agentcore_control.types.registry_record_arn.RegistryRecordArn"
    )
    """<p>The Amazon Resource Name (ARN) of the created registry record.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.registry_record_status.RegistryRecordStatus"
    """<p>The status of the registry record. Set to <code>CREATING</code> while the asynchronous workflow is in progress.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRegistryRecordResponse) -> dict:
    out: dict = {}
    out["recordArn"] = value["record_arn"]
    import aws_sdk_bedrock_agentcore_control.types.registry_record_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.registry_record_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateRegistryRecordResponse:
    out: CreateRegistryRecordResponse = {}  # type: ignore[typeddict-item]
    if "recordArn" in data:
        out["record_arn"] = data["recordArn"]
    else:
        raise DeserializationError("CreateRegistryRecordResponse.record_arn required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.registry_record_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.registry_record_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateRegistryRecordResponse.status required")
    return out
