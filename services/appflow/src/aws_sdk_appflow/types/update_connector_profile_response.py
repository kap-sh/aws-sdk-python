"""Generated from Smithy shape ``com.amazonaws.appflow#UpdateConnectorProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.connector_profile_arn


class UpdateConnectorProfileResponse(TypedDict):
    connector_profile_arn: NotRequired[
        "aws_sdk_appflow.types.connector_profile_arn.ConnectorProfileArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the connector profile. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectorProfileResponse) -> dict:
    out: dict = {}
    if "connector_profile_arn" in value:
        out["connectorProfileArn"] = value["connector_profile_arn"]
    return out


def deserialize_json(data: dict) -> UpdateConnectorProfileResponse:
    out: UpdateConnectorProfileResponse = {}  # type: ignore[typeddict-item]
    if "connectorProfileArn" in data:
        out["connector_profile_arn"] = data["connectorProfileArn"]
    return out
