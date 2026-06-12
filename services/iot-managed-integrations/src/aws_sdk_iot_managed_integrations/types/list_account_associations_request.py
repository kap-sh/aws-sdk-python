"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListAccountAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.connector_destination_id
    import aws_sdk_iot_managed_integrations.types.max_results
    import aws_sdk_iot_managed_integrations.types.next_token


class ListAccountAssociationsRequest(TypedDict):
    connector_destination_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.connector_destination_id.ConnectorDestinationId"
    ]
    """<p>The identifier of the connector destination to filter account associations by.</p>"""
    max_results: NotRequired[
        "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
    ]
    """<p>The maximum number of account associations to return in a single response.</p>"""
    next_token: NotRequired[
        "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
    ]
    """<p>A token used for pagination of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccountAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAccountAssociationsRequest:
    out: ListAccountAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
