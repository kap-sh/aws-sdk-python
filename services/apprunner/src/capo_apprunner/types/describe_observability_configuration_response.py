"""Generated from Smithy shape ``com.amazonaws.apprunner#DescribeObservabilityConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import capo_apprunner.types.observability_configuration


class DescribeObservabilityConfigurationResponse(TypedDict, closed=True):
    observability_configuration: (
        "capo_apprunner.types.observability_configuration.ObservabilityConfiguration"
    )
    """<p>A full description of the App Runner observability configuration that you specified in this request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeObservabilityConfigurationResponse) -> dict:
    out: dict = {}
    import capo_apprunner.types.observability_configuration

    out["ObservabilityConfiguration"] = (
        capo_apprunner.types.observability_configuration.serialize_aws_json_1_0(
            value["observability_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeObservabilityConfigurationResponse:
    out: DescribeObservabilityConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "ObservabilityConfiguration" in data:
        import capo_apprunner.types.observability_configuration

        out["observability_configuration"] = (
            capo_apprunner.types.observability_configuration.deserialize_aws_json_1_0(
                data["ObservabilityConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeObservabilityConfigurationResponse.observability_configuration required"
        )
    return out
