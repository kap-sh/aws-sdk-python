"""Generated from Smithy shape ``com.amazonaws.glue#ListDevEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.dev_endpoint_name_list
    import aws_sdk_glue.types.generic_string


class ListDevEndpointsResponse(TypedDict, closed=True):
    dev_endpoint_names: NotRequired[
        "aws_sdk_glue.types.dev_endpoint_name_list.DevEndpointNameList"
    ]
    """<p>The names of all the <code>DevEndpoint</code>s in the account, or the <code>DevEndpoint</code>s with the specified tags.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if the returned list does not contain the last metric available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDevEndpointsResponse) -> dict:
    out: dict = {}
    if "dev_endpoint_names" in value:
        import aws_sdk_glue.types.dev_endpoint_name_list

        out["DevEndpointNames"] = (
            aws_sdk_glue.types.dev_endpoint_name_list.serialize_aws_json_1_1(
                value["dev_endpoint_names"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDevEndpointsResponse:
    out: ListDevEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "DevEndpointNames" in data:
        import aws_sdk_glue.types.dev_endpoint_name_list

        out["dev_endpoint_names"] = (
            aws_sdk_glue.types.dev_endpoint_name_list.deserialize_aws_json_1_1(
                data["DevEndpointNames"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
