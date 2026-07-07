"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ListAppInstanceUserEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_summary_list
    import aws_sdk_chime_sdk_identity.types.next_token


class ListAppInstanceUserEndpointsResponse(TypedDict, closed=True):
    app_instance_user_endpoints: NotRequired[
        "aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_summary_list.AppInstanceUserEndpointSummaryList"
    ]
    """<p>The information for each requested <code>AppInstanceUserEndpoint</code>.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_identity.types.next_token.NextToken"]
    """<p>The token passed by previous API calls until all requested endpoints are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppInstanceUserEndpointsResponse) -> dict:
    out: dict = {}
    if "app_instance_user_endpoints" in value:
        import aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_summary_list

        out["AppInstanceUserEndpoints"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_summary_list.serialize_json(
                value["app_instance_user_endpoints"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppInstanceUserEndpointsResponse:
    out: ListAppInstanceUserEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "AppInstanceUserEndpoints" in data:
        import aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_summary_list

        out["app_instance_user_endpoints"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint_summary_list.deserialize_json(
                data["AppInstanceUserEndpoints"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
