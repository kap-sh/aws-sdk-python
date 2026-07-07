"""Generated from Smithy shape ``com.amazonaws.securityhub#SecurityControlsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.disabled_security_control_identifier_list
    import aws_sdk_securityhub.types.enabled_security_control_identifier_list
    import aws_sdk_securityhub.types.security_control_custom_parameters_list


class SecurityControlsConfiguration(TypedDict, closed=True):
    enabled_security_control_identifiers: NotRequired[
        "aws_sdk_securityhub.types.enabled_security_control_identifier_list.EnabledSecurityControlIdentifierList"
    ]
    """<p> A list of security controls that are enabled in the configuration policy. Security Hub CSPM disables all other controls (including newly released controls) other than the listed controls. </p>"""
    disabled_security_control_identifiers: NotRequired[
        "aws_sdk_securityhub.types.disabled_security_control_identifier_list.DisabledSecurityControlIdentifierList"
    ]
    """<p> A list of security controls that are disabled in the configuration policy. Security Hub CSPM enables all other controls (including newly released controls) other than the listed controls. </p>"""
    security_control_custom_parameters: NotRequired[
        "aws_sdk_securityhub.types.security_control_custom_parameters_list.SecurityControlCustomParametersList"
    ]
    """<p> A list of security controls and control parameter values that are included in a configuration policy. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityControlsConfiguration) -> dict:
    out: dict = {}
    if "enabled_security_control_identifiers" in value:
        import aws_sdk_securityhub.types.enabled_security_control_identifier_list

        out["EnabledSecurityControlIdentifiers"] = (
            aws_sdk_securityhub.types.enabled_security_control_identifier_list.serialize_json(
                value["enabled_security_control_identifiers"]
            )
        )
    if "disabled_security_control_identifiers" in value:
        import aws_sdk_securityhub.types.disabled_security_control_identifier_list

        out["DisabledSecurityControlIdentifiers"] = (
            aws_sdk_securityhub.types.disabled_security_control_identifier_list.serialize_json(
                value["disabled_security_control_identifiers"]
            )
        )
    if "security_control_custom_parameters" in value:
        import aws_sdk_securityhub.types.security_control_custom_parameters_list

        out["SecurityControlCustomParameters"] = (
            aws_sdk_securityhub.types.security_control_custom_parameters_list.serialize_json(
                value["security_control_custom_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> SecurityControlsConfiguration:
    out: SecurityControlsConfiguration = {}  # type: ignore[typeddict-item]
    if "EnabledSecurityControlIdentifiers" in data:
        import aws_sdk_securityhub.types.enabled_security_control_identifier_list

        out["enabled_security_control_identifiers"] = (
            aws_sdk_securityhub.types.enabled_security_control_identifier_list.deserialize_json(
                data["EnabledSecurityControlIdentifiers"]
            )
        )
    if "DisabledSecurityControlIdentifiers" in data:
        import aws_sdk_securityhub.types.disabled_security_control_identifier_list

        out["disabled_security_control_identifiers"] = (
            aws_sdk_securityhub.types.disabled_security_control_identifier_list.deserialize_json(
                data["DisabledSecurityControlIdentifiers"]
            )
        )
    if "SecurityControlCustomParameters" in data:
        import aws_sdk_securityhub.types.security_control_custom_parameters_list

        out["security_control_custom_parameters"] = (
            aws_sdk_securityhub.types.security_control_custom_parameters_list.deserialize_json(
                data["SecurityControlCustomParameters"]
            )
        )
    return out
