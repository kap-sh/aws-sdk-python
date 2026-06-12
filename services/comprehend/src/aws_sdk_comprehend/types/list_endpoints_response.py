"""Generated from Smithy shape ``com.amazonaws.comprehend#ListEndpointsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.endpoint_properties_list
    import aws_sdk_comprehend.types.string


class ListEndpointsResponse(TypedDict):
    endpoint_properties_list: NotRequired[
        "aws_sdk_comprehend.types.endpoint_properties_list.EndpointPropertiesList"
    ]
    """<p>Displays a list of endpoint properties being retrieved by the service in response to the request.</p>"""
    next_token: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEndpointsResponse) -> dict:
    out: dict = {}
    if "endpoint_properties_list" in value:
        import aws_sdk_comprehend.types.endpoint_properties_list

        out["EndpointPropertiesList"] = (
            aws_sdk_comprehend.types.endpoint_properties_list.serialize_aws_json_1_1(
                value["endpoint_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEndpointsResponse:
    out: ListEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "EndpointPropertiesList" in data:
        import aws_sdk_comprehend.types.endpoint_properties_list

        out["endpoint_properties_list"] = (
            aws_sdk_comprehend.types.endpoint_properties_list.deserialize_aws_json_1_1(
                data["EndpointPropertiesList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
