"""Generated from Smithy shape ``com.amazonaws.shield#ApplicationLayerAutomaticResponseConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_shield.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_shield.types.application_layer_automatic_response_status
    import aws_sdk_shield.types.response_action


class ApplicationLayerAutomaticResponseConfiguration(TypedDict):
    status: "aws_sdk_shield.types.application_layer_automatic_response_status.ApplicationLayerAutomaticResponseStatus"
    """<p>Indicates whether automatic application layer DDoS mitigation is enabled for the protection. </p>"""
    action: "aws_sdk_shield.types.response_action.ResponseAction"
    """<p>Specifies the action setting that Shield Advanced should use in the WAF rules that it creates on behalf of the protected resource in response to DDoS attacks. You specify this as part of the configuration for the automatic application layer DDoS mitigation feature, when you enable or update automatic mitigation. Shield Advanced creates the WAF rules in a Shield Advanced-managed rule group, inside the web ACL that you have associated with the resource. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ApplicationLayerAutomaticResponseConfiguration,
) -> dict:
    out: dict = {}
    import aws_sdk_shield.types.application_layer_automatic_response_status

    out["Status"] = (
        aws_sdk_shield.types.application_layer_automatic_response_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    import aws_sdk_shield.types.response_action

    out["Action"] = aws_sdk_shield.types.response_action.serialize_aws_json_1_1(
        value["action"]
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ApplicationLayerAutomaticResponseConfiguration:
    out: ApplicationLayerAutomaticResponseConfiguration = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_shield.types.application_layer_automatic_response_status

        out["status"] = (
            aws_sdk_shield.types.application_layer_automatic_response_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        raise DeserializationError(
            "ApplicationLayerAutomaticResponseConfiguration.status required"
        )
    if "Action" in data:
        import aws_sdk_shield.types.response_action

        out["action"] = aws_sdk_shield.types.response_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        raise DeserializationError(
            "ApplicationLayerAutomaticResponseConfiguration.action required"
        )
    return out
