"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#RegisterAppInstanceUserEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.chime_arn
    import aws_sdk_chime_sdk_identity.types.string64


class RegisterAppInstanceUserEndpointResponse(TypedDict, closed=True):
    app_instance_user_arn: NotRequired[
        "aws_sdk_chime_sdk_identity.types.chime_arn.ChimeArn"
    ]
    """<p>The ARN of the <code>AppInstanceUser</code>.</p>"""
    endpoint_id: NotRequired["aws_sdk_chime_sdk_identity.types.string64.String64"]
    """<p>The unique identifier of the <code>AppInstanceUserEndpoint</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterAppInstanceUserEndpointResponse) -> dict:
    out: dict = {}
    if "app_instance_user_arn" in value:
        out["AppInstanceUserArn"] = value["app_instance_user_arn"]
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    return out


def deserialize_json(data: dict) -> RegisterAppInstanceUserEndpointResponse:
    out: RegisterAppInstanceUserEndpointResponse = {}  # type: ignore[typeddict-item]
    if "AppInstanceUserArn" in data:
        out["app_instance_user_arn"] = data["AppInstanceUserArn"]
    if "EndpointId" in data:
        out["endpoint_id"] = data["EndpointId"]
    return out
