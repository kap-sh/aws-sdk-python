"""Generated from Smithy shape ``com.amazonaws.apprunner#CreateObservabilityConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.observability_configuration_name
    import aws_sdk_apprunner.types.tag_list
    import aws_sdk_apprunner.types.trace_configuration


class CreateObservabilityConfigurationRequest(TypedDict, closed=True):
    observability_configuration_name: "aws_sdk_apprunner.types.observability_configuration_name.ObservabilityConfigurationName"
    """<p>A name for the observability configuration. When you use it for the first time in an Amazon Web Services Region, App Runner creates revision number <code>1</code> of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration.</p> <note> <p>The name <code>DefaultConfiguration</code> is reserved. You can't use it to create a new observability configuration, and you can't create a revision of it.</p> <p>When you want to use your own observability configuration for your App Runner service, <i>create a configuration with a different name</i>, and then provide it when you create or update your service.</p> </note>"""
    trace_configuration: NotRequired[
        "aws_sdk_apprunner.types.trace_configuration.TraceConfiguration"
    ]
    """<p>The configuration of the tracing feature within this observability configuration. If you don't specify it, App Runner doesn't enable tracing.</p>"""
    tags: NotRequired["aws_sdk_apprunner.types.tag_list.TagList"]
    """<p>A list of metadata items that you can associate with your observability configuration resource. A tag is a key-value pair.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateObservabilityConfigurationRequest) -> dict:
    out: dict = {}
    out["ObservabilityConfigurationName"] = value["observability_configuration_name"]
    if "trace_configuration" in value:
        import aws_sdk_apprunner.types.trace_configuration

        out["TraceConfiguration"] = (
            aws_sdk_apprunner.types.trace_configuration.serialize_aws_json_1_0(
                value["trace_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_apprunner.types.tag_list

        out["Tags"] = aws_sdk_apprunner.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateObservabilityConfigurationRequest:
    out: CreateObservabilityConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "ObservabilityConfigurationName" in data:
        out["observability_configuration_name"] = data["ObservabilityConfigurationName"]
    else:
        raise DeserializationError(
            "CreateObservabilityConfigurationRequest.observability_configuration_name required"
        )
    if "TraceConfiguration" in data:
        import aws_sdk_apprunner.types.trace_configuration

        out["trace_configuration"] = (
            aws_sdk_apprunner.types.trace_configuration.deserialize_aws_json_1_0(
                data["TraceConfiguration"]
            )
        )
    if "Tags" in data:
        import aws_sdk_apprunner.types.tag_list

        out["tags"] = aws_sdk_apprunner.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
