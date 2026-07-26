"""Generated from Smithy shape ``com.amazonaws.configservice#PutRemediationExceptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.config_rule_name
    import capo_config_service.types.date
    import capo_config_service.types.remediation_exception_resource_keys
    import capo_config_service.types.string_with_char_limit1024


class PutRemediationExceptionsRequest(TypedDict, closed=True):
    config_rule_name: "capo_config_service.types.config_rule_name.ConfigRuleName"
    """<p>The name of the Config rule for which you want to create remediation exception.</p>"""
    resource_keys: "capo_config_service.types.remediation_exception_resource_keys.RemediationExceptionResourceKeys"
    """<p>An exception list of resource exception keys to be processed with the current request. Config adds exception for each resource key. For example, Config adds 3 exceptions for 3 resource keys. </p>"""
    message: NotRequired[
        "capo_config_service.types.string_with_char_limit1024.StringWithCharLimit1024"
    ]
    """<p>The message contains an explanation of the exception.</p>"""
    expiration_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>The exception is automatically deleted after the expiration date.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRemediationExceptionsRequest) -> dict:
    out: dict = {}
    out["ConfigRuleName"] = value["config_rule_name"]
    import capo_config_service.types.remediation_exception_resource_keys

    out["ResourceKeys"] = (
        capo_config_service.types.remediation_exception_resource_keys.serialize_aws_json_1_1(
            value["resource_keys"]
        )
    )
    if "message" in value:
        out["Message"] = value["message"]
    if "expiration_time" in value:
        import capo_config_service.types.date

        out["ExpirationTime"] = capo_config_service.types.date.serialize_aws_json_1_1(
            value["expiration_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRemediationExceptionsRequest:
    out: PutRemediationExceptionsRequest = {}  # type: ignore[typeddict-item]
    if "ConfigRuleName" in data:
        out["config_rule_name"] = data["ConfigRuleName"]
    else:
        raise DeserializationError(
            "PutRemediationExceptionsRequest.config_rule_name required"
        )
    if "ResourceKeys" in data:
        import capo_config_service.types.remediation_exception_resource_keys

        out["resource_keys"] = (
            capo_config_service.types.remediation_exception_resource_keys.deserialize_aws_json_1_1(
                data["ResourceKeys"]
            )
        )
    else:
        raise DeserializationError(
            "PutRemediationExceptionsRequest.resource_keys required"
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "ExpirationTime" in data:
        import capo_config_service.types.date

        out["expiration_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["ExpirationTime"]
            )
        )
    return out
