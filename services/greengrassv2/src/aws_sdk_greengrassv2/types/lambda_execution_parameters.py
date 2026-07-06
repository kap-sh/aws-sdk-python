"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaExecutionParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.lambda_environment_variables
    import aws_sdk_greengrassv2.types.lambda_event_source_list
    import aws_sdk_greengrassv2.types.lambda_exec_args_list
    import aws_sdk_greengrassv2.types.lambda_input_payload_encoding_type
    import aws_sdk_greengrassv2.types.lambda_linux_process_params
    import aws_sdk_greengrassv2.types.optional_boolean
    import aws_sdk_greengrassv2.types.optional_integer


class LambdaExecutionParameters(TypedDict, closed=True):
    event_sources: NotRequired[
        "aws_sdk_greengrassv2.types.lambda_event_source_list.LambdaEventSourceList"
    ]
    """<p>The list of event sources to which to subscribe to receive work messages. The Lambda function runs when it receives a message from an event source. You can subscribe this function to local publish/subscribe messages and Amazon Web Services IoT Core MQTT messages.</p>"""
    max_queue_size: NotRequired[
        "aws_sdk_greengrassv2.types.optional_integer.OptionalInteger"
    ]
    """<p>The maximum size of the message queue for the Lambda function component. The IoT Greengrass core stores messages in a FIFO (first-in-first-out) queue until it can run the Lambda function to consume each message.</p>"""
    max_instances_count: NotRequired[
        "aws_sdk_greengrassv2.types.optional_integer.OptionalInteger"
    ]
    """<p>The maximum number of instances that a non-pinned Lambda function can run at the same time.</p>"""
    max_idle_time_in_seconds: NotRequired[
        "aws_sdk_greengrassv2.types.optional_integer.OptionalInteger"
    ]
    """<p>The maximum amount of time in seconds that a non-pinned Lambda function can idle before the IoT Greengrass Core software stops its process.</p>"""
    timeout_in_seconds: NotRequired[
        "aws_sdk_greengrassv2.types.optional_integer.OptionalInteger"
    ]
    """<p>The maximum amount of time in seconds that the Lambda function can process a work item.</p>"""
    status_timeout_in_seconds: NotRequired[
        "aws_sdk_greengrassv2.types.optional_integer.OptionalInteger"
    ]
    """<p>The interval in seconds at which a pinned (also known as long-lived) Lambda function component sends status updates to the Lambda manager component.</p>"""
    pinned: NotRequired["aws_sdk_greengrassv2.types.optional_boolean.OptionalBoolean"]
    """<p>Whether or not the Lambda function is pinned, or long-lived.</p> <ul> <li> <p>A pinned Lambda function starts when IoT Greengrass starts and keeps running in its own container.</p> </li> <li> <p>A non-pinned Lambda function starts only when it receives a work item and exists after it idles for <code>maxIdleTimeInSeconds</code>. If the function has multiple work items, the IoT Greengrass Core software creates multiple instances of the function.</p> </li> </ul> <p>Default: <code>true</code> </p>"""
    input_payload_encoding_type: NotRequired[
        "aws_sdk_greengrassv2.types.lambda_input_payload_encoding_type.LambdaInputPayloadEncodingType"
    ]
    """<p>The encoding type that the Lambda function supports.</p> <p>Default: <code>json</code> </p>"""
    exec_args: NotRequired[
        "aws_sdk_greengrassv2.types.lambda_exec_args_list.LambdaExecArgsList"
    ]
    """<p>The list of arguments to pass to the Lambda function when it runs.</p>"""
    environment_variables: NotRequired[
        "aws_sdk_greengrassv2.types.lambda_environment_variables.LambdaEnvironmentVariables"
    ]
    """<p>The map of environment variables that are available to the Lambda function when it runs.</p>"""
    linux_process_params: NotRequired[
        "aws_sdk_greengrassv2.types.lambda_linux_process_params.LambdaLinuxProcessParams"
    ]
    """<p>The parameters for the Linux process that contains the Lambda function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaExecutionParameters) -> dict:
    out: dict = {}
    if "event_sources" in value:
        import aws_sdk_greengrassv2.types.lambda_event_source_list

        out["eventSources"] = (
            aws_sdk_greengrassv2.types.lambda_event_source_list.serialize_json(
                value["event_sources"]
            )
        )
    if "max_queue_size" in value:
        out["maxQueueSize"] = value["max_queue_size"]
    if "max_instances_count" in value:
        out["maxInstancesCount"] = value["max_instances_count"]
    if "max_idle_time_in_seconds" in value:
        out["maxIdleTimeInSeconds"] = value["max_idle_time_in_seconds"]
    if "timeout_in_seconds" in value:
        out["timeoutInSeconds"] = value["timeout_in_seconds"]
    if "status_timeout_in_seconds" in value:
        out["statusTimeoutInSeconds"] = value["status_timeout_in_seconds"]
    if "pinned" in value:
        out["pinned"] = value["pinned"]
    if "input_payload_encoding_type" in value:
        import aws_sdk_greengrassv2.types.lambda_input_payload_encoding_type

        out["inputPayloadEncodingType"] = (
            aws_sdk_greengrassv2.types.lambda_input_payload_encoding_type.serialize_json(
                value["input_payload_encoding_type"]
            )
        )
    if "exec_args" in value:
        import aws_sdk_greengrassv2.types.lambda_exec_args_list

        out["execArgs"] = (
            aws_sdk_greengrassv2.types.lambda_exec_args_list.serialize_json(
                value["exec_args"]
            )
        )
    if "environment_variables" in value:
        import aws_sdk_greengrassv2.types.lambda_environment_variables

        out["environmentVariables"] = (
            aws_sdk_greengrassv2.types.lambda_environment_variables.serialize_json(
                value["environment_variables"]
            )
        )
    if "linux_process_params" in value:
        import aws_sdk_greengrassv2.types.lambda_linux_process_params

        out["linuxProcessParams"] = (
            aws_sdk_greengrassv2.types.lambda_linux_process_params.serialize_json(
                value["linux_process_params"]
            )
        )
    return out


def deserialize_json(data: dict) -> LambdaExecutionParameters:
    out: LambdaExecutionParameters = {}  # type: ignore[typeddict-item]
    if "eventSources" in data:
        import aws_sdk_greengrassv2.types.lambda_event_source_list

        out["event_sources"] = (
            aws_sdk_greengrassv2.types.lambda_event_source_list.deserialize_json(
                data["eventSources"]
            )
        )
    if "maxQueueSize" in data:
        out["max_queue_size"] = data["maxQueueSize"]
    if "maxInstancesCount" in data:
        out["max_instances_count"] = data["maxInstancesCount"]
    if "maxIdleTimeInSeconds" in data:
        out["max_idle_time_in_seconds"] = data["maxIdleTimeInSeconds"]
    if "timeoutInSeconds" in data:
        out["timeout_in_seconds"] = data["timeoutInSeconds"]
    if "statusTimeoutInSeconds" in data:
        out["status_timeout_in_seconds"] = data["statusTimeoutInSeconds"]
    if "pinned" in data:
        out["pinned"] = data["pinned"]
    if "inputPayloadEncodingType" in data:
        import aws_sdk_greengrassv2.types.lambda_input_payload_encoding_type

        out["input_payload_encoding_type"] = (
            aws_sdk_greengrassv2.types.lambda_input_payload_encoding_type.deserialize_json(
                data["inputPayloadEncodingType"]
            )
        )
    if "execArgs" in data:
        import aws_sdk_greengrassv2.types.lambda_exec_args_list

        out["exec_args"] = (
            aws_sdk_greengrassv2.types.lambda_exec_args_list.deserialize_json(
                data["execArgs"]
            )
        )
    if "environmentVariables" in data:
        import aws_sdk_greengrassv2.types.lambda_environment_variables

        out["environment_variables"] = (
            aws_sdk_greengrassv2.types.lambda_environment_variables.deserialize_json(
                data["environmentVariables"]
            )
        )
    if "linuxProcessParams" in data:
        import aws_sdk_greengrassv2.types.lambda_linux_process_params

        out["linux_process_params"] = (
            aws_sdk_greengrassv2.types.lambda_linux_process_params.deserialize_json(
                data["linuxProcessParams"]
            )
        )
    return out
