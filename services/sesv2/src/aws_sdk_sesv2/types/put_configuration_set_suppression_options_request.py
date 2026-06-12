"""Generated from Smithy shape ``com.amazonaws.sesv2#PutConfigurationSetSuppressionOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.configuration_set_name
    import aws_sdk_sesv2.types.suppression_list_reasons
    import aws_sdk_sesv2.types.suppression_list_scope
    import aws_sdk_sesv2.types.suppression_validation_options


class PutConfigurationSetSuppressionOptionsRequest(TypedDict):
    configuration_set_name: (
        "aws_sdk_sesv2.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set to change the suppression list preferences for.</p>"""
    suppression_scope: NotRequired[
        "aws_sdk_sesv2.types.suppression_list_scope.SuppressionListScope"
    ]
    """<p>The suppression scope for the configuration set. This overrides the tenant or account suppression scope for emails sent using this configuration set. Can be one of the following:</p> <ul> <li> <p> <code>TENANT</code> – Use the tenant's suppression list.</p> </li> <li> <p> <code>ACCOUNT</code> – Use the account-level suppression list.</p> </li> </ul>"""
    suppressed_reasons: NotRequired[
        "aws_sdk_sesv2.types.suppression_list_reasons.SuppressionListReasons"
    ]
    """<p>A list that contains the reasons that email addresses are automatically added to the suppression list for your account or for a specific tenant. This list can contain any or all of the following:</p> <ul> <li> <p> <code>COMPLAINT</code> – Amazon SES adds an email address to the suppression list for your account or for a specific tenant when a message sent to that address results in a complaint.</p> </li> <li> <p> <code>BOUNCE</code> – Amazon SES adds an email address to the suppression list for your account or for a specific tenant when a message sent to that address results in a hard bounce.</p> </li> </ul>"""
    validation_options: NotRequired[
        "aws_sdk_sesv2.types.suppression_validation_options.SuppressionValidationOptions"
    ]
    """<p>An object that contains information about the email address suppression preferences for the configuration set in the current Amazon Web Services Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutConfigurationSetSuppressionOptionsRequest) -> dict:
    out: dict = {}
    if "suppression_scope" in value:
        import aws_sdk_sesv2.types.suppression_list_scope

        out["SuppressionScope"] = (
            aws_sdk_sesv2.types.suppression_list_scope.serialize_json(
                value["suppression_scope"]
            )
        )
    if "suppressed_reasons" in value:
        import aws_sdk_sesv2.types.suppression_list_reasons

        out["SuppressedReasons"] = (
            aws_sdk_sesv2.types.suppression_list_reasons.serialize_json(
                value["suppressed_reasons"]
            )
        )
    if "validation_options" in value:
        import aws_sdk_sesv2.types.suppression_validation_options

        out["ValidationOptions"] = (
            aws_sdk_sesv2.types.suppression_validation_options.serialize_json(
                value["validation_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutConfigurationSetSuppressionOptionsRequest:
    out: PutConfigurationSetSuppressionOptionsRequest = {}  # type: ignore[typeddict-item]
    if "SuppressionScope" in data:
        import aws_sdk_sesv2.types.suppression_list_scope

        out["suppression_scope"] = (
            aws_sdk_sesv2.types.suppression_list_scope.deserialize_json(
                data["SuppressionScope"]
            )
        )
    if "SuppressedReasons" in data:
        import aws_sdk_sesv2.types.suppression_list_reasons

        out["suppressed_reasons"] = (
            aws_sdk_sesv2.types.suppression_list_reasons.deserialize_json(
                data["SuppressedReasons"]
            )
        )
    if "ValidationOptions" in data:
        import aws_sdk_sesv2.types.suppression_validation_options

        out["validation_options"] = (
            aws_sdk_sesv2.types.suppression_validation_options.deserialize_json(
                data["ValidationOptions"]
            )
        )
    return out
