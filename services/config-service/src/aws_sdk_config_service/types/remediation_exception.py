"""Generated from Smithy shape ``com.amazonaws.configservice#RemediationException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.config_rule_name
    import aws_sdk_config_service.types.date
    import aws_sdk_config_service.types.string_with_char_limit256
    import aws_sdk_config_service.types.string_with_char_limit1024


class RemediationException(TypedDict):
    config_rule_name: "aws_sdk_config_service.types.config_rule_name.ConfigRuleName"
    """<p>The name of the Config rule.</p>"""
    resource_type: (
        "aws_sdk_config_service.types.string_with_char_limit256.StringWithCharLimit256"
    )
    """<p>The type of a resource.</p>"""
    resource_id: "aws_sdk_config_service.types.string_with_char_limit1024.StringWithCharLimit1024"
    """<p>The ID of the resource (for example., sg-xxxxxx).</p>"""
    message: NotRequired[
        "aws_sdk_config_service.types.string_with_char_limit1024.StringWithCharLimit1024"
    ]
    """<p>An explanation of an remediation exception.</p>"""
    expiration_time: NotRequired["aws_sdk_config_service.types.date.Date"]
    """<p>The time when the remediation exception will be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemediationException) -> dict:
    out: dict = {}
    out["ConfigRuleName"] = value["config_rule_name"]
    out["ResourceType"] = value["resource_type"]
    out["ResourceId"] = value["resource_id"]
    if "message" in value:
        out["Message"] = value["message"]
    if "expiration_time" in value:
        import aws_sdk_config_service.types.date

        out["ExpirationTime"] = (
            aws_sdk_config_service.types.date.serialize_aws_json_1_1(
                value["expiration_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemediationException:
    out: RemediationException = {}  # type: ignore[typeddict-item]
    if "ConfigRuleName" in data:
        out["config_rule_name"] = data["ConfigRuleName"]
    else:
        raise DeserializationError("RemediationException.config_rule_name required")
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    else:
        raise DeserializationError("RemediationException.resource_type required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("RemediationException.resource_id required")
    if "Message" in data:
        out["message"] = data["Message"]
    if "ExpirationTime" in data:
        import aws_sdk_config_service.types.date

        out["expiration_time"] = (
            aws_sdk_config_service.types.date.deserialize_aws_json_1_1(
                data["ExpirationTime"]
            )
        )
    return out
