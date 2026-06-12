"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityHubPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.enabled_standard_identifier_list
    import aws_sdk_securityhub.types.security_controls_configuration


class SecurityHubPolicy(TypedDict):
    service_enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether Security Hub CSPM is enabled in the policy. </p>"""
    enabled_standard_identifiers: NotRequired[
        "aws_sdk_securityhub.types.enabled_standard_identifier_list.EnabledStandardIdentifierList"
    ]
    """<p> A list that defines which security standards are enabled in the configuration policy. </p>"""
    security_controls_configuration: NotRequired[
        "aws_sdk_securityhub.types.security_controls_configuration.SecurityControlsConfiguration"
    ]
    """<p> An object that defines which security controls are enabled in the configuration policy. The enablement status of a control is aligned across all of the enabled standards in an account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityHubPolicy) -> dict:
    out: dict = {}
    if "service_enabled" in value:
        out["ServiceEnabled"] = value["service_enabled"]
    if "enabled_standard_identifiers" in value:
        import aws_sdk_securityhub.types.enabled_standard_identifier_list

        out["EnabledStandardIdentifiers"] = (
            aws_sdk_securityhub.types.enabled_standard_identifier_list.serialize_json(
                value["enabled_standard_identifiers"]
            )
        )
    if "security_controls_configuration" in value:
        import aws_sdk_securityhub.types.security_controls_configuration

        out["SecurityControlsConfiguration"] = (
            aws_sdk_securityhub.types.security_controls_configuration.serialize_json(
                value["security_controls_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SecurityHubPolicy:
    out: SecurityHubPolicy = {}  # type: ignore[typeddict-item]
    if "ServiceEnabled" in data:
        out["service_enabled"] = data["ServiceEnabled"]
    if "EnabledStandardIdentifiers" in data:
        import aws_sdk_securityhub.types.enabled_standard_identifier_list

        out["enabled_standard_identifiers"] = (
            aws_sdk_securityhub.types.enabled_standard_identifier_list.deserialize_json(
                data["EnabledStandardIdentifiers"]
            )
        )
    if "SecurityControlsConfiguration" in data:
        import aws_sdk_securityhub.types.security_controls_configuration

        out["security_controls_configuration"] = (
            aws_sdk_securityhub.types.security_controls_configuration.deserialize_json(
                data["SecurityControlsConfiguration"]
            )
        )
    return out
