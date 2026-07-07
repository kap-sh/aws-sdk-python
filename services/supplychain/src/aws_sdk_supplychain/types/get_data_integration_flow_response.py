"""Generated from Smithy shape ``com.amazonaws.supplychain#GetDataIntegrationFlowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_integration_flow


class GetDataIntegrationFlowResponse(TypedDict, closed=True):
    flow: "aws_sdk_supplychain.types.data_integration_flow.DataIntegrationFlow"
    """<p>The details of the DataIntegrationFlow returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataIntegrationFlowResponse) -> dict:
    out: dict = {}
    import aws_sdk_supplychain.types.data_integration_flow

    out["flow"] = aws_sdk_supplychain.types.data_integration_flow.serialize_json(
        value["flow"]
    )
    return out


def deserialize_json(data: dict) -> GetDataIntegrationFlowResponse:
    out: GetDataIntegrationFlowResponse = {}  # type: ignore[typeddict-item]
    if "flow" in data:
        import aws_sdk_supplychain.types.data_integration_flow

        out["flow"] = aws_sdk_supplychain.types.data_integration_flow.deserialize_json(
            data["flow"]
        )
    else:
        raise DeserializationError("GetDataIntegrationFlowResponse.flow required")
    return out
