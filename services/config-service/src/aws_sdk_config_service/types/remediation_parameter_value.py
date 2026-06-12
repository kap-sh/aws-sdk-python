"""Generated from Smithy shape ``com.amazonaws.configservice#RemediationParameterValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.resource_value
    import aws_sdk_config_service.types.static_value


class RemediationParameterValue(TypedDict):
    resource_value: NotRequired[
        "aws_sdk_config_service.types.resource_value.ResourceValue"
    ]
    """<p>The value is dynamic and changes at run-time.</p>"""
    static_value: NotRequired["aws_sdk_config_service.types.static_value.StaticValue"]
    """<p>The value is static and does not change at run-time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemediationParameterValue) -> dict:
    out: dict = {}
    if "resource_value" in value:
        import aws_sdk_config_service.types.resource_value

        out["ResourceValue"] = (
            aws_sdk_config_service.types.resource_value.serialize_aws_json_1_1(
                value["resource_value"]
            )
        )
    if "static_value" in value:
        import aws_sdk_config_service.types.static_value

        out["StaticValue"] = (
            aws_sdk_config_service.types.static_value.serialize_aws_json_1_1(
                value["static_value"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemediationParameterValue:
    out: RemediationParameterValue = {}  # type: ignore[typeddict-item]
    if "ResourceValue" in data:
        import aws_sdk_config_service.types.resource_value

        out["resource_value"] = (
            aws_sdk_config_service.types.resource_value.deserialize_aws_json_1_1(
                data["ResourceValue"]
            )
        )
    if "StaticValue" in data:
        import aws_sdk_config_service.types.static_value

        out["static_value"] = (
            aws_sdk_config_service.types.static_value.deserialize_aws_json_1_1(
                data["StaticValue"]
            )
        )
    return out
