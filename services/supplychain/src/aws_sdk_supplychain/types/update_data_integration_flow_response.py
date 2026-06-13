"""Generated from Smithy shape ``com.amazonaws.supplychain#UpdateDataIntegrationFlowResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow


class UpdateDataIntegrationFlowResponse(TypedDict):
    flow: "aws_sdk_supplychain.types.data_integration_flow.DataIntegrationFlow"
    """<p>The details of the updated DataIntegrationFlow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataIntegrationFlowResponse) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.data_integration_flow

    out["flow"] = aws_sdk_supplychain.types.data_integration_flow.serialize_json(
        value["flow"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDataIntegrationFlowResponse:
    out: UpdateDataIntegrationFlowResponse = {}  # type: ignore[typeddict-item]
    if "flow" in data:
        import aws_sdk_supplychain.types.data_integration_flow

        out["flow"] = aws_sdk_supplychain.types.data_integration_flow.deserialize_json(
            data["flow"]
        )
    else:
        raise DeserializationError("UpdateDataIntegrationFlowResponse.flow required")
    return out
