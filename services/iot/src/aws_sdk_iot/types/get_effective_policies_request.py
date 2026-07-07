"""Generated from Smithy shape ``com.amazonaws.iot#GetEffectivePoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.cognito_identity_pool_id
    import aws_sdk_iot.types.principal
    import aws_sdk_iot.types.thing_name


class GetEffectivePoliciesRequest(TypedDict, closed=True):
    principal: NotRequired["aws_sdk_iot.types.principal.Principal"]
    """<p>The principal. Valid principals are CertificateArn (arn:aws:iot:<i>region</i>:<i>accountId</i>:cert/<i>certificateId</i>), thingGroupArn (arn:aws:iot:<i>region</i>:<i>accountId</i>:thinggroup/<i>groupName</i>) and CognitoId (<i>region</i>:<i>id</i>).</p>"""
    cognito_identity_pool_id: NotRequired[
        "aws_sdk_iot.types.cognito_identity_pool_id.CognitoIdentityPoolId"
    ]
    """<p>The Cognito identity pool ID.</p>"""
    thing_name: NotRequired["aws_sdk_iot.types.thing_name.ThingName"]
    """<p>The thing name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEffectivePoliciesRequest) -> dict:
    out: dict = {}
    if "principal" in value:
        out["principal"] = value["principal"]
    if "cognito_identity_pool_id" in value:
        out["cognitoIdentityPoolId"] = value["cognito_identity_pool_id"]
    return out


def deserialize_json(data: dict) -> GetEffectivePoliciesRequest:
    out: GetEffectivePoliciesRequest = {}  # type: ignore[typeddict-item]
    if "principal" in data:
        out["principal"] = data["principal"]
    if "cognitoIdentityPoolId" in data:
        out["cognito_identity_pool_id"] = data["cognitoIdentityPoolId"]
    return out
