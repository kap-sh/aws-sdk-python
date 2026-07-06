"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetManagedThingStateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.state_endpoints


class GetManagedThingStateResponse(TypedDict, closed=True):
    endpoints: "aws_sdk_iot_managed_integrations.types.state_endpoints.StateEndpoints"
    """<p>The device endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedThingStateResponse) -> dict:
    out: dict = {}
    import aws_sdk_iot_managed_integrations.types.state_endpoints

    out["Endpoints"] = (
        aws_sdk_iot_managed_integrations.types.state_endpoints.serialize_json(
            value["endpoints"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetManagedThingStateResponse:
    out: GetManagedThingStateResponse = {}  # type: ignore[typeddict-item]
    if "Endpoints" in data:
        import aws_sdk_iot_managed_integrations.types.state_endpoints

        out["endpoints"] = (
            aws_sdk_iot_managed_integrations.types.state_endpoints.deserialize_json(
                data["Endpoints"]
            )
        )
    else:
        raise DeserializationError("GetManagedThingStateResponse.endpoints required")
    return out
