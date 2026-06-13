"""Generated from Smithy shape ``com.amazonaws.ssmincidents#AutomationExecution``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn


class _AutomationExecution_ssmExecutionArn(TypedDict):
    ssmExecutionArn: "aws_sdk_ssm_incidents.types.arn.Arn"


AutomationExecution: TypeAlias = _AutomationExecution_ssmExecutionArn


# --- restJson1 ser/de ---
def serialize_json(value: AutomationExecution) -> dict:
    if "ssmExecutionArn" in value:
        return {"ssmExecutionArn": value["ssmExecutionArn"]}
    else:
        raise SerializationError("AutomationExecution: no variant present")


def deserialize_json(data: dict) -> AutomationExecution:
    if "ssmExecutionArn" in data:
        return {"ssmExecutionArn": data["ssmExecutionArn"]}
    else:
        raise DeserializationError("AutomationExecution: no recognized variant key")
