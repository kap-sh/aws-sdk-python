"""Generated from Smithy shape ``com.amazonaws.ssmsap#GetConfigurationCheckOperationInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.operation_id


class GetConfigurationCheckOperationInput(TypedDict):
    operation_id: "aws_sdk_ssm_sap.types.operation_id.OperationId"
    """<p>The ID of the configuration check operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationCheckOperationInput) -> dict:
    out: dict = {}
    out["OperationId"] = value["operation_id"]
    return out


def deserialize_json(data: dict) -> GetConfigurationCheckOperationInput:
    out: GetConfigurationCheckOperationInput = {}  # type: ignore[typeddict-item]
    if "OperationId" in data:
        out["operation_id"] = data["OperationId"]
    else:
        raise DeserializationError(
            "GetConfigurationCheckOperationInput.operation_id required"
        )
    return out
