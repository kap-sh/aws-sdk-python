"""Generated from Smithy shape ``com.amazonaws.appflow#RegisterConnectorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.arn


class RegisterConnectorResponse(TypedDict):
    connector_arn: NotRequired["aws_sdk_appflow.types.arn.ARN"]
    """<p>The ARN of the connector being registered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterConnectorResponse) -> dict:
    out: dict = {}
    if "connector_arn" in value:
        out["connectorArn"] = value["connector_arn"]
    return out


def deserialize_json(data: dict) -> RegisterConnectorResponse:
    out: RegisterConnectorResponse = {}  # type: ignore[typeddict-item]
    if "connectorArn" in data:
        out["connector_arn"] = data["connectorArn"]
    return out
