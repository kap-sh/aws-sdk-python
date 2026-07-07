"""Generated from Smithy shape ``com.amazonaws.apprunner#DeleteObservabilityConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.observability_configuration


class DeleteObservabilityConfigurationResponse(TypedDict, closed=True):
    observability_configuration: (
        "aws_sdk_apprunner.types.observability_configuration.ObservabilityConfiguration"
    )
    """<p>A description of the App Runner observability configuration that this request just deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteObservabilityConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_apprunner.types.observability_configuration

    out["ObservabilityConfiguration"] = (
        aws_sdk_apprunner.types.observability_configuration.serialize_aws_json_1_0(
            value["observability_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteObservabilityConfigurationResponse:
    out: DeleteObservabilityConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "ObservabilityConfiguration" in data:
        import aws_sdk_apprunner.types.observability_configuration

        out["observability_configuration"] = (
            aws_sdk_apprunner.types.observability_configuration.deserialize_aws_json_1_0(
                data["ObservabilityConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteObservabilityConfigurationResponse.observability_configuration required"
        )
    return out
