"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListManagedThingSchemasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.capability_id
    import aws_sdk_iot_managed_integrations.types.endpoint_id
    import aws_sdk_iot_managed_integrations.types.managed_thing_id
    import aws_sdk_iot_managed_integrations.types.max_results
    import aws_sdk_iot_managed_integrations.types.next_token


class ListManagedThingSchemasRequest(TypedDict, closed=True):
    identifier: "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    """<p>The managed thing id.</p>"""
    endpoint_id_filter: NotRequired[
        "aws_sdk_iot_managed_integrations.types.endpoint_id.EndpointId"
    ]
    """<p>Filter on an endpoint id.</p>"""
    capability_id_filter: NotRequired[
        "aws_sdk_iot_managed_integrations.types.capability_id.CapabilityId"
    ]
    """<p>Filter on a capability id.</p>"""
    next_token: NotRequired[
        "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
    ]
    """<p>A token that can be used to retrieve the next set of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_iot_managed_integrations.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return at one time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedThingSchemasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListManagedThingSchemasRequest:
    out: ListManagedThingSchemasRequest = {}  # type: ignore[typeddict-item]
    return out
