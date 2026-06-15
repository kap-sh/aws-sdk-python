"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationRecorderSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.amazon_resource_name
    import aws_sdk_config_service.types.recorder_name
    import aws_sdk_config_service.types.recording_scope
    import aws_sdk_config_service.types.service_principal


class ConfigurationRecorderSummary(TypedDict):
    arn: "aws_sdk_config_service.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the configuration recorder.</p>"""
    name: "aws_sdk_config_service.types.recorder_name.RecorderName"
    """<p>The name of the configuration recorder.</p>"""
    service_principal: NotRequired[
        "aws_sdk_config_service.types.service_principal.ServicePrincipal"
    ]
    """<p>For service-linked configuration recorders, indicates which Amazon Web Services service the configuration recorder is linked to.</p>"""
    recording_scope: "aws_sdk_config_service.types.recording_scope.RecordingScope"
    r"""<p>Indicates whether the <a href=\"https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigurationItem.html\">ConfigurationItems</a> in scope for the configuration recorder are recorded for free (<code>INTERNAL</code>) or if you are charged a service fee for recording (<code>PAID</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationRecorderSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "service_principal" in value:
        out["servicePrincipal"] = value["service_principal"]
    import aws_sdk_config_service.types.recording_scope

    out["recordingScope"] = (
        aws_sdk_config_service.types.recording_scope.serialize_aws_json_1_1(
            value["recording_scope"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigurationRecorderSummary:
    out: ConfigurationRecorderSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ConfigurationRecorderSummary.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ConfigurationRecorderSummary.name required")
    if "servicePrincipal" in data:
        out["service_principal"] = data["servicePrincipal"]
    if "recordingScope" in data:
        import aws_sdk_config_service.types.recording_scope

        out["recording_scope"] = (
            aws_sdk_config_service.types.recording_scope.deserialize_aws_json_1_1(
                data["recordingScope"]
            )
        )
    else:
        raise DeserializationError(
            "ConfigurationRecorderSummary.recording_scope required"
        )
    return out
