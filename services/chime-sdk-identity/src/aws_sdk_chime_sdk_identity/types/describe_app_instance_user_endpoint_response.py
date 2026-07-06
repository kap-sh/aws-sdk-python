"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#DescribeAppInstanceUserEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint


class DescribeAppInstanceUserEndpointResponse(TypedDict, closed=True):
    app_instance_user_endpoint: NotRequired[
        "aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint.AppInstanceUserEndpoint"
    ]
    """<p>The full details of an <code>AppInstanceUserEndpoint</code>: the <code>AppInstanceUserArn</code>, ID, name, type, resource ARN, attributes, allow messages, state, and created and last updated timestamps. All timestamps use epoch milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppInstanceUserEndpointResponse) -> dict:
    out: dict = {}
    if "app_instance_user_endpoint" in value:
        import aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint

        out["AppInstanceUserEndpoint"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint.serialize_json(
                value["app_instance_user_endpoint"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAppInstanceUserEndpointResponse:
    out: DescribeAppInstanceUserEndpointResponse = {}  # type: ignore[typeddict-item]
    if "AppInstanceUserEndpoint" in data:
        import aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint

        out["app_instance_user_endpoint"] = (
            aws_sdk_chime_sdk_identity.types.app_instance_user_endpoint.deserialize_json(
                data["AppInstanceUserEndpoint"]
            )
        )
    return out
