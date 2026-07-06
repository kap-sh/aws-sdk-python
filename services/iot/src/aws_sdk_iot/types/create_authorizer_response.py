"""Generated from Smithy shape ``com.amazonaws.iot#CreateAuthorizerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.authorizer_arn
    import aws_sdk_iot.types.authorizer_name


class CreateAuthorizerResponse(TypedDict, closed=True):
    authorizer_name: NotRequired["aws_sdk_iot.types.authorizer_name.AuthorizerName"]
    """<p>The authorizer's name.</p>"""
    authorizer_arn: NotRequired["aws_sdk_iot.types.authorizer_arn.AuthorizerArn"]
    """<p>The authorizer ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAuthorizerResponse) -> dict:
    out: dict = {}
    if "authorizer_name" in value:
        out["authorizerName"] = value["authorizer_name"]
    if "authorizer_arn" in value:
        out["authorizerArn"] = value["authorizer_arn"]
    return out


def deserialize_json(data: dict) -> CreateAuthorizerResponse:
    out: CreateAuthorizerResponse = {}  # type: ignore[typeddict-item]
    if "authorizerName" in data:
        out["authorizer_name"] = data["authorizerName"]
    if "authorizerArn" in data:
        out["authorizer_arn"] = data["authorizerArn"]
    return out
