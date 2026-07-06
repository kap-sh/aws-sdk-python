"""Generated from Smithy shape ``com.amazonaws.appflow#UpdateConnectorRegistrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appflow.types.arn


class UpdateConnectorRegistrationResponse(TypedDict, closed=True):
    connector_arn: NotRequired["aws_sdk_appflow.types.arn.ARN"]
    """<p>The ARN of the connector being updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectorRegistrationResponse) -> dict:
    out: dict = {}
    if "connector_arn" in value:
        out["connectorArn"] = value["connector_arn"]
    return out


def deserialize_json(data: dict) -> UpdateConnectorRegistrationResponse:
    out: UpdateConnectorRegistrationResponse = {}  # type: ignore[typeddict-item]
    if "connectorArn" in data:
        out["connector_arn"] = data["connectorArn"]
    return out
