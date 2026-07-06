"""Generated from Smithy shape ``com.amazonaws.shield#UpdateApplicationLayerAutomaticResponseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_shield.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_shield.types.resource_arn
    import aws_sdk_shield.types.response_action


class UpdateApplicationLayerAutomaticResponseRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_shield.types.resource_arn.ResourceArn"
    """<p>The ARN (Amazon Resource Name) of the resource.</p>"""
    action: "aws_sdk_shield.types.response_action.ResponseAction"
    """<p>Specifies the action setting that Shield Advanced should use in the WAF rules that it creates on behalf of the protected resource in response to DDoS attacks. You specify this as part of the configuration for the automatic application layer DDoS mitigation feature, when you enable or update automatic mitigation. Shield Advanced creates the WAF rules in a Shield Advanced-managed rule group, inside the web ACL that you have associated with the resource. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: UpdateApplicationLayerAutomaticResponseRequest,
) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import aws_sdk_shield.types.response_action

    out["Action"] = aws_sdk_shield.types.response_action.serialize_aws_json_1_1(
        value["action"]
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> UpdateApplicationLayerAutomaticResponseRequest:
    out: UpdateApplicationLayerAutomaticResponseRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "UpdateApplicationLayerAutomaticResponseRequest.resource_arn required"
        )
    if "Action" in data:
        import aws_sdk_shield.types.response_action

        out["action"] = aws_sdk_shield.types.response_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        raise DeserializationError(
            "UpdateApplicationLayerAutomaticResponseRequest.action required"
        )
    return out
