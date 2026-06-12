"""Generated from Smithy shape ``com.amazonaws.apprunner#CreateObservabilityConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.observability_configuration


class CreateObservabilityConfigurationResponse(TypedDict):
    observability_configuration: (
        "aws_sdk_apprunner.types.observability_configuration.ObservabilityConfiguration"
    )
    """<p>A description of the App Runner observability configuration that's created by this request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateObservabilityConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.observability_configuration

    out["ObservabilityConfiguration"] = (
        aws_sdk_apprunner.types.observability_configuration.serialize_aws_json_1_0(
            value["observability_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateObservabilityConfigurationResponse:
    out: CreateObservabilityConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "ObservabilityConfiguration" in data:
        import aws_sdk_apprunner.types.observability_configuration

        out["observability_configuration"] = (
            aws_sdk_apprunner.types.observability_configuration.deserialize_aws_json_1_0(
                data["ObservabilityConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateObservabilityConfigurationResponse.observability_configuration required"
        )
    return out
