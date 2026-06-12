"""Generated from Smithy shape ``com.amazonaws.devicefarm#RemoteAccessSession``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name
    import aws_sdk_device_farm.types.billing_method
    import aws_sdk_device_farm.types.date_time
    import aws_sdk_device_farm.types.device
    import aws_sdk_device_farm.types.device_minutes
    import aws_sdk_device_farm.types.device_proxy
    import aws_sdk_device_farm.types.execution_result
    import aws_sdk_device_farm.types.execution_status
    import aws_sdk_device_farm.types.interaction_mode
    import aws_sdk_device_farm.types.message
    import aws_sdk_device_farm.types.name
    import aws_sdk_device_farm.types.remote_access_endpoints
    import aws_sdk_device_farm.types.skip_app_resign
    import aws_sdk_device_farm.types.string
    import aws_sdk_device_farm.types.vpc_config


class RemoteAccessSession(TypedDict):
    arn: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the remote access session.</p>"""
    name: NotRequired["aws_sdk_device_farm.types.name.Name"]
    """<p>The name of the remote access session.</p>"""
    created: NotRequired["aws_sdk_device_farm.types.date_time.DateTime"]
    """<p>The date and time the remote access session was created.</p>"""
    status: NotRequired["aws_sdk_device_farm.types.execution_status.ExecutionStatus"]
    """<p>The status of the remote access session. Can be any of the following:</p> <ul> <li> <p>PENDING.</p> </li> <li> <p>PENDING_CONCURRENCY.</p> </li> <li> <p>PENDING_DEVICE.</p> </li> <li> <p>PROCESSING.</p> </li> <li> <p>SCHEDULING.</p> </li> <li> <p>PREPARING.</p> </li> <li> <p>RUNNING.</p> </li> <li> <p>COMPLETED.</p> </li> <li> <p>STOPPING.</p> </li> </ul>"""
    result: NotRequired["aws_sdk_device_farm.types.execution_result.ExecutionResult"]
    """<p>The result of the remote access session. Can be any of the following:</p> <ul> <li> <p>PENDING.</p> </li> <li> <p>PASSED.</p> </li> <li> <p>WARNED.</p> </li> <li> <p>FAILED.</p> </li> <li> <p>SKIPPED.</p> </li> <li> <p>ERRORED.</p> </li> <li> <p>STOPPED.</p> </li> </ul>"""
    message: NotRequired["aws_sdk_device_farm.types.message.Message"]
    """<p>A message about the remote access session.</p>"""
    started: NotRequired["aws_sdk_device_farm.types.date_time.DateTime"]
    """<p>The date and time the remote access session was started.</p>"""
    stopped: NotRequired["aws_sdk_device_farm.types.date_time.DateTime"]
    """<p>The date and time the remote access session was stopped.</p>"""
    device: NotRequired["aws_sdk_device_farm.types.device.Device"]
    """<p>The device (phone or tablet) used in the remote access session.</p>"""
    instance_arn: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the instance.</p>"""
    billing_method: NotRequired[
        "aws_sdk_device_farm.types.billing_method.BillingMethod"
    ]
    """<p>The billing method of the remote access session. Possible values include <code>METERED</code> or <code>UNMETERED</code>. For more information about metered devices, see <a href=\"https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html#welcome-terminology\">AWS Device Farm terminology</a>.</p>"""
    device_minutes: NotRequired[
        "aws_sdk_device_farm.types.device_minutes.DeviceMinutes"
    ]
    """<p>The number of minutes a device is used in a remote access session (including setup and teardown minutes).</p>"""
    endpoint: NotRequired["aws_sdk_device_farm.types.string.String"]
    """<p>The endpoint for the remote access session. This field is deprecated, and is replaced by the new <code>endpoints.interactiveEndpoint</code> field.</p>"""
    device_udid: NotRequired["aws_sdk_device_farm.types.string.String"]
    """<p>Unique device identifier for the remote device. Only returned if remote debugging is enabled for the remote access session.</p> <p>Remote debugging is <a href=\"https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html\">no longer supported</a>.</p>"""
    interaction_mode: NotRequired[
        "aws_sdk_device_farm.types.interaction_mode.InteractionMode"
    ]
    """<p>The interaction mode of the remote access session. Changing the interactive mode of remote access sessions is no longer available.</p>"""
    skip_app_resign: NotRequired[
        "aws_sdk_device_farm.types.skip_app_resign.SkipAppResign"
    ]
    """<p>When set to <code>true</code>, for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.</p> <p>For more information about how Device Farm re-signs your apps, see <a href=\"http://aws.amazon.com/device-farm/faqs/\">Do you modify my app?</a> in the <i>AWS Device Farm FAQs</i>.</p>"""
    vpc_config: NotRequired["aws_sdk_device_farm.types.vpc_config.VpcConfig"]
    """<p>The VPC security groups and subnets that are attached to a project.</p>"""
    device_proxy: NotRequired["aws_sdk_device_farm.types.device_proxy.DeviceProxy"]
    """<p>The device proxy configured for the remote access session.</p>"""
    app_upload: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN for the app to be installed onto your device.</p>"""
    endpoints: NotRequired[
        "aws_sdk_device_farm.types.remote_access_endpoints.RemoteAccessEndpoints"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoteAccessSession) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "created" in value:
        import aws_sdk_device_farm.types.date_time

        out["created"] = aws_sdk_device_farm.types.date_time.serialize_aws_json_1_1(
            value["created"]
        )
    if "status" in value:
        import aws_sdk_device_farm.types.execution_status

        out["status"] = (
            aws_sdk_device_farm.types.execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "result" in value:
        import aws_sdk_device_farm.types.execution_result

        out["result"] = (
            aws_sdk_device_farm.types.execution_result.serialize_aws_json_1_1(
                value["result"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    if "started" in value:
        import aws_sdk_device_farm.types.date_time

        out["started"] = aws_sdk_device_farm.types.date_time.serialize_aws_json_1_1(
            value["started"]
        )
    if "stopped" in value:
        import aws_sdk_device_farm.types.date_time

        out["stopped"] = aws_sdk_device_farm.types.date_time.serialize_aws_json_1_1(
            value["stopped"]
        )
    if "device" in value:
        import aws_sdk_device_farm.types.device

        out["device"] = aws_sdk_device_farm.types.device.serialize_aws_json_1_1(
            value["device"]
        )
    if "instance_arn" in value:
        out["instanceArn"] = value["instance_arn"]
    if "billing_method" in value:
        import aws_sdk_device_farm.types.billing_method

        out["billingMethod"] = (
            aws_sdk_device_farm.types.billing_method.serialize_aws_json_1_1(
                value["billing_method"]
            )
        )
    if "device_minutes" in value:
        import aws_sdk_device_farm.types.device_minutes

        out["deviceMinutes"] = (
            aws_sdk_device_farm.types.device_minutes.serialize_aws_json_1_1(
                value["device_minutes"]
            )
        )
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "device_udid" in value:
        out["deviceUdid"] = value["device_udid"]
    if "interaction_mode" in value:
        import aws_sdk_device_farm.types.interaction_mode

        out["interactionMode"] = (
            aws_sdk_device_farm.types.interaction_mode.serialize_aws_json_1_1(
                value["interaction_mode"]
            )
        )
    if "skip_app_resign" in value:
        out["skipAppResign"] = value["skip_app_resign"]
    if "vpc_config" in value:
        import aws_sdk_device_farm.types.vpc_config

        out["vpcConfig"] = aws_sdk_device_farm.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "device_proxy" in value:
        import aws_sdk_device_farm.types.device_proxy

        out["deviceProxy"] = (
            aws_sdk_device_farm.types.device_proxy.serialize_aws_json_1_1(
                value["device_proxy"]
            )
        )
    if "app_upload" in value:
        out["appUpload"] = value["app_upload"]
    if "endpoints" in value:
        import aws_sdk_device_farm.types.remote_access_endpoints

        out["endpoints"] = (
            aws_sdk_device_farm.types.remote_access_endpoints.serialize_aws_json_1_1(
                value["endpoints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoteAccessSession:
    out: RemoteAccessSession = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "created" in data:
        import aws_sdk_device_farm.types.date_time

        out["created"] = aws_sdk_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["created"]
        )
    if "status" in data:
        import aws_sdk_device_farm.types.execution_status

        out["status"] = (
            aws_sdk_device_farm.types.execution_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "result" in data:
        import aws_sdk_device_farm.types.execution_result

        out["result"] = (
            aws_sdk_device_farm.types.execution_result.deserialize_aws_json_1_1(
                data["result"]
            )
        )
    if "message" in data:
        out["message"] = data["message"]
    if "started" in data:
        import aws_sdk_device_farm.types.date_time

        out["started"] = aws_sdk_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["started"]
        )
    if "stopped" in data:
        import aws_sdk_device_farm.types.date_time

        out["stopped"] = aws_sdk_device_farm.types.date_time.deserialize_aws_json_1_1(
            data["stopped"]
        )
    if "device" in data:
        import aws_sdk_device_farm.types.device

        out["device"] = aws_sdk_device_farm.types.device.deserialize_aws_json_1_1(
            data["device"]
        )
    if "instanceArn" in data:
        out["instance_arn"] = data["instanceArn"]
    if "billingMethod" in data:
        import aws_sdk_device_farm.types.billing_method

        out["billing_method"] = (
            aws_sdk_device_farm.types.billing_method.deserialize_aws_json_1_1(
                data["billingMethod"]
            )
        )
    if "deviceMinutes" in data:
        import aws_sdk_device_farm.types.device_minutes

        out["device_minutes"] = (
            aws_sdk_device_farm.types.device_minutes.deserialize_aws_json_1_1(
                data["deviceMinutes"]
            )
        )
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    if "deviceUdid" in data:
        out["device_udid"] = data["deviceUdid"]
    if "interactionMode" in data:
        import aws_sdk_device_farm.types.interaction_mode

        out["interaction_mode"] = (
            aws_sdk_device_farm.types.interaction_mode.deserialize_aws_json_1_1(
                data["interactionMode"]
            )
        )
    if "skipAppResign" in data:
        out["skip_app_resign"] = data["skipAppResign"]
    if "vpcConfig" in data:
        import aws_sdk_device_farm.types.vpc_config

        out["vpc_config"] = (
            aws_sdk_device_farm.types.vpc_config.deserialize_aws_json_1_1(
                data["vpcConfig"]
            )
        )
    if "deviceProxy" in data:
        import aws_sdk_device_farm.types.device_proxy

        out["device_proxy"] = (
            aws_sdk_device_farm.types.device_proxy.deserialize_aws_json_1_1(
                data["deviceProxy"]
            )
        )
    if "appUpload" in data:
        out["app_upload"] = data["appUpload"]
    if "endpoints" in data:
        import aws_sdk_device_farm.types.remote_access_endpoints

        out["endpoints"] = (
            aws_sdk_device_farm.types.remote_access_endpoints.deserialize_aws_json_1_1(
                data["endpoints"]
            )
        )
    return out
