"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.account_identifier
    import aws_sdk_observabilityadmin.types.resource_identifier
    import aws_sdk_observabilityadmin.types.resource_type
    import aws_sdk_observabilityadmin.types.tag_map_output
    import aws_sdk_observabilityadmin.types.telemetry_configuration_state
    import aws_sdk_observabilityadmin.types.telemetry_source_type


class TelemetryConfiguration(TypedDict):
    account_identifier: NotRequired[
        "aws_sdk_observabilityadmin.types.account_identifier.AccountIdentifier"
    ]
    """<p> The account ID which contains the resource managed in telemetry configuration. An example of a valid account ID is <code>012345678901</code>. </p>"""
    telemetry_configuration_state: NotRequired[
        "aws_sdk_observabilityadmin.types.telemetry_configuration_state.TelemetryConfigurationState"
    ]
    """<p> The configuration state for the resource, for example <code>{ Logs: NotApplicable; Metrics: Enabled; Traces: NotApplicable; }</code>. </p>"""
    resource_type: NotRequired[
        "aws_sdk_observabilityadmin.types.resource_type.ResourceType"
    ]
    """<p> The type of resource, for example <code>Amazon Web Services::EC2::Instance</code>, or <code>Amazon Web Services::EKS::Cluster</code>, etc. </p>"""
    resource_identifier: NotRequired[
        "aws_sdk_observabilityadmin.types.resource_identifier.ResourceIdentifier"
    ]
    """<p> The identifier of the resource, for example for Amazon VPC, it would be <code>vpc-1a2b3c4d5e6f1a2b3</code>. </p>"""
    resource_tags: NotRequired[
        "aws_sdk_observabilityadmin.types.tag_map_output.TagMapOutput"
    ]
    r"""<p> Tags associated with the resource, for example <code>{ Name: \"ExampleInstance\", Environment: \"Development\" }</code>. </p>"""
    last_update_time_stamp: NotRequired["int"]
    """<p> The timestamp of the last change to the telemetry configuration for the resource. For example, <code>1728679196318</code>. </p>"""
    telemetry_source_type: NotRequired[
        "aws_sdk_observabilityadmin.types.telemetry_source_type.TelemetrySourceType"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryConfiguration) -> dict:
    out: dict = {}
    if "account_identifier" in value:
        out["AccountIdentifier"] = value["account_identifier"]
    if "telemetry_configuration_state" in value:
        import aws_sdk_observabilityadmin.types.telemetry_configuration_state

        out["TelemetryConfigurationState"] = (
            aws_sdk_observabilityadmin.types.telemetry_configuration_state.serialize_json(
                value["telemetry_configuration_state"]
            )
        )
    if "resource_type" in value:
        import aws_sdk_observabilityadmin.types.resource_type

        out["ResourceType"] = (
            aws_sdk_observabilityadmin.types.resource_type.serialize_json(
                value["resource_type"]
            )
        )
    if "resource_identifier" in value:
        out["ResourceIdentifier"] = value["resource_identifier"]
    if "resource_tags" in value:
        import aws_sdk_observabilityadmin.types.tag_map_output

        out["ResourceTags"] = (
            aws_sdk_observabilityadmin.types.tag_map_output.serialize_json(
                value["resource_tags"]
            )
        )
    if "last_update_time_stamp" in value:
        out["LastUpdateTimeStamp"] = value["last_update_time_stamp"]
    if "telemetry_source_type" in value:
        import aws_sdk_observabilityadmin.types.telemetry_source_type

        out["TelemetrySourceType"] = (
            aws_sdk_observabilityadmin.types.telemetry_source_type.serialize_json(
                value["telemetry_source_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> TelemetryConfiguration:
    out: TelemetryConfiguration = {}  # type: ignore[typeddict-item]
    if "AccountIdentifier" in data:
        out["account_identifier"] = data["AccountIdentifier"]
    if "TelemetryConfigurationState" in data:
        import aws_sdk_observabilityadmin.types.telemetry_configuration_state

        out["telemetry_configuration_state"] = (
            aws_sdk_observabilityadmin.types.telemetry_configuration_state.deserialize_json(
                data["TelemetryConfigurationState"]
            )
        )
    if "ResourceType" in data:
        import aws_sdk_observabilityadmin.types.resource_type

        out["resource_type"] = (
            aws_sdk_observabilityadmin.types.resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    if "ResourceIdentifier" in data:
        out["resource_identifier"] = data["ResourceIdentifier"]
    if "ResourceTags" in data:
        import aws_sdk_observabilityadmin.types.tag_map_output

        out["resource_tags"] = (
            aws_sdk_observabilityadmin.types.tag_map_output.deserialize_json(
                data["ResourceTags"]
            )
        )
    if "LastUpdateTimeStamp" in data:
        out["last_update_time_stamp"] = data["LastUpdateTimeStamp"]
    if "TelemetrySourceType" in data:
        import aws_sdk_observabilityadmin.types.telemetry_source_type

        out["telemetry_source_type"] = (
            aws_sdk_observabilityadmin.types.telemetry_source_type.deserialize_json(
                data["TelemetrySourceType"]
            )
        )
    return out
