"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListResourceTelemetryForOrganizationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.next_token
    import aws_sdk_observabilityadmin.types.telemetry_configurations


class ListResourceTelemetryForOrganizationOutput(TypedDict):
    telemetry_configurations: NotRequired[
        "aws_sdk_observabilityadmin.types.telemetry_configurations.TelemetryConfigurations"
    ]
    """<p> A list of telemetry configurations for Amazon Web Services resources supported by telemetry config in the organization. </p>"""
    next_token: NotRequired["aws_sdk_observabilityadmin.types.next_token.NextToken"]
    """<p> The token for the next set of items to return. A previous call provides this token. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceTelemetryForOrganizationOutput) -> dict:
    out: dict = {}
    if "telemetry_configurations" in value:
        import aws_sdk_observabilityadmin.types.telemetry_configurations

        out["TelemetryConfigurations"] = (
            aws_sdk_observabilityadmin.types.telemetry_configurations.serialize_json(
                value["telemetry_configurations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourceTelemetryForOrganizationOutput:
    out: ListResourceTelemetryForOrganizationOutput = {}  # type: ignore[typeddict-item]
    if "TelemetryConfigurations" in data:
        import aws_sdk_observabilityadmin.types.telemetry_configurations

        out["telemetry_configurations"] = (
            aws_sdk_observabilityadmin.types.telemetry_configurations.deserialize_json(
                data["TelemetryConfigurations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
