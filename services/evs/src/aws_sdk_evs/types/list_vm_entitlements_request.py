"""Generated from Smithy shape ``com.amazonaws.evs#ListVmEntitlementsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_evs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_evs.types.connector_id
    import aws_sdk_evs.types.entitlement_type
    import aws_sdk_evs.types.environment_id
    import aws_sdk_evs.types.max_results
    import aws_sdk_evs.types.pagination_token


class ListVmEntitlementsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_evs.types.pagination_token.PaginationToken"]
    """<p>A unique pagination token for each page. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>"""
    max_results: NotRequired["aws_sdk_evs.types.max_results.MaxResults"]
    """<p>The maximum number of results to return. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified.</p>"""
    environment_id: "aws_sdk_evs.types.environment_id.EnvironmentId"
    """<p>A unique ID for the environment.</p>"""
    connector_id: "aws_sdk_evs.types.connector_id.ConnectorId"
    """<p>A unique ID for the connector.</p>"""
    entitlement_type: "aws_sdk_evs.types.entitlement_type.EntitlementType"
    """<p>The type of entitlement to list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListVmEntitlementsRequest) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    out["connectorId"] = value["connector_id"]
    import aws_sdk_evs.types.entitlement_type

    out["entitlementType"] = aws_sdk_evs.types.entitlement_type.serialize_aws_json_1_0(
        value["entitlement_type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListVmEntitlementsRequest:
    out: ListVmEntitlementsRequest = {}  # type: ignore[typeddict-item]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError("ListVmEntitlementsRequest.environment_id required")
    if "connectorId" in data:
        out["connector_id"] = data["connectorId"]
    else:
        raise DeserializationError("ListVmEntitlementsRequest.connector_id required")
    if "entitlementType" in data:
        import aws_sdk_evs.types.entitlement_type

        out["entitlement_type"] = (
            aws_sdk_evs.types.entitlement_type.deserialize_aws_json_1_0(
                data["entitlementType"]
            )
        )
    else:
        raise DeserializationError(
            "ListVmEntitlementsRequest.entitlement_type required"
        )
    return out
