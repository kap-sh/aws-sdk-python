"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#DescribeAppInstanceUserEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.string64
    import capo_chime_sdk_identity.types.string1600


class DescribeAppInstanceUserEndpointRequest(TypedDict, closed=True):
    app_instance_user_arn: "capo_chime_sdk_identity.types.string1600.String1600"
    """<p>The ARN of the <code>AppInstanceUser</code>.</p>"""
    endpoint_id: "capo_chime_sdk_identity.types.string64.String64"
    """<p>The unique identifier of the <code>AppInstanceUserEndpoint</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAppInstanceUserEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAppInstanceUserEndpointRequest:
    out: DescribeAppInstanceUserEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
