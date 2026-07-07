"""Generated from Smithy shape ``com.amazonaws.devicefarm#Run``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name
    import aws_sdk_device_farm.types.amazon_role_resource_name
    import aws_sdk_device_farm.types.billing_method
    import aws_sdk_device_farm.types.counters
    import aws_sdk_device_farm.types.customer_artifact_paths
    import aws_sdk_device_farm.types.date_time
    import aws_sdk_device_farm.types.device_minutes
    import aws_sdk_device_farm.types.device_platform
    import aws_sdk_device_farm.types.device_proxy
    import aws_sdk_device_farm.types.device_selection_result
    import aws_sdk_device_farm.types.environment_variables
    import aws_sdk_device_farm.types.execution_result
    import aws_sdk_device_farm.types.execution_result_code
    import aws_sdk_device_farm.types.execution_status
    import aws_sdk_device_farm.types.integer
    import aws_sdk_device_farm.types.job_timeout_minutes
    import aws_sdk_device_farm.types.location
    import aws_sdk_device_farm.types.message
    import aws_sdk_device_farm.types.name
    import aws_sdk_device_farm.types.network_profile
    import aws_sdk_device_farm.types.radios
    import aws_sdk_device_farm.types.skip_app_resign
    import aws_sdk_device_farm.types.string
    import aws_sdk_device_farm.types.test_type
    import aws_sdk_device_farm.types.vpc_config


class Run(TypedDict, closed=True):
    arn: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The run's ARN.</p>"""
    name: NotRequired["aws_sdk_device_farm.types.name.Name"]
    """<p>The run's name.</p>"""
    type: NotRequired["aws_sdk_device_farm.types.test_type.TestType"]
    """<p>The run's type.</p> <p>Must be one of the following values:</p> <ul> <li> <p>BUILTIN_FUZZ</p> </li> <li> <p>APPIUM_JAVA_JUNIT</p> </li> <li> <p>APPIUM_JAVA_TESTNG</p> </li> <li> <p>APPIUM_PYTHON</p> </li> <li> <p>APPIUM_NODE</p> </li> <li> <p>APPIUM_RUBY</p> </li> <li> <p>APPIUM_WEB_JAVA_JUNIT</p> </li> <li> <p>APPIUM_WEB_JAVA_TESTNG</p> </li> <li> <p>APPIUM_WEB_PYTHON</p> </li> <li> <p>APPIUM_WEB_NODE</p> </li> <li> <p>APPIUM_WEB_RUBY</p> </li> <li> <p>INSTRUMENTATION</p> </li> <li> <p>XCTEST</p> </li> <li> <p>XCTEST_UI</p> </li> </ul>"""
    platform: NotRequired["aws_sdk_device_farm.types.device_platform.DevicePlatform"]
    """<p>The run's platform.</p> <p>Allowed values include:</p> <ul> <li> <p>ANDROID</p> </li> <li> <p>IOS</p> </li> </ul>"""
    created: NotRequired["aws_sdk_device_farm.types.date_time.DateTime"]
    """<p>When the run was created.</p>"""
    status: NotRequired["aws_sdk_device_farm.types.execution_status.ExecutionStatus"]
    """<p>The run's status.</p> <p>Allowed values include:</p> <ul> <li> <p>PENDING</p> </li> <li> <p>PENDING_CONCURRENCY</p> </li> <li> <p>PENDING_DEVICE</p> </li> <li> <p>PROCESSING</p> </li> <li> <p>SCHEDULING</p> </li> <li> <p>PREPARING</p> </li> <li> <p>RUNNING</p> </li> <li> <p>COMPLETED</p> </li> <li> <p>STOPPING</p> </li> </ul>"""
    result: NotRequired["aws_sdk_device_farm.types.execution_result.ExecutionResult"]
    """<p>The run's result.</p> <p>Allowed values include:</p> <ul> <li> <p>PENDING</p> </li> <li> <p>PASSED</p> </li> <li> <p>WARNED</p> </li> <li> <p>FAILED</p> </li> <li> <p>SKIPPED</p> </li> <li> <p>ERRORED</p> </li> <li> <p>STOPPED</p> </li> </ul>"""
    started: NotRequired["aws_sdk_device_farm.types.date_time.DateTime"]
    """<p>The run's start time.</p>"""
    stopped: NotRequired["aws_sdk_device_farm.types.date_time.DateTime"]
    """<p>The run's stop time.</p>"""
    counters: NotRequired["aws_sdk_device_farm.types.counters.Counters"]
    """<p>The run's result counters.</p>"""
    message: NotRequired["aws_sdk_device_farm.types.message.Message"]
    """<p>A message about the run's result.</p>"""
    total_jobs: NotRequired["aws_sdk_device_farm.types.integer.Integer"]
    """<p>The total number of jobs for the run.</p>"""
    completed_jobs: NotRequired["aws_sdk_device_farm.types.integer.Integer"]
    """<p>The total number of completed jobs.</p>"""
    billing_method: NotRequired[
        "aws_sdk_device_farm.types.billing_method.BillingMethod"
    ]
    """<p>Specifies the billing method for a test run: <code>metered</code> or <code>unmetered</code>. If the parameter is not specified, the default value is <code>metered</code>.</p> <note> <p>If you have unmetered device slots, you must set this to <code>unmetered</code> to use them. Otherwise, the run is counted toward metered device minutes.</p> </note>"""
    device_minutes: NotRequired[
        "aws_sdk_device_farm.types.device_minutes.DeviceMinutes"
    ]
    """<p>Represents the total (metered or unmetered) minutes used by the test run.</p>"""
    network_profile: NotRequired[
        "aws_sdk_device_farm.types.network_profile.NetworkProfile"
    ]
    """<p>The network profile being used for a test run.</p>"""
    device_proxy: NotRequired["aws_sdk_device_farm.types.device_proxy.DeviceProxy"]
    """<p>The device proxy configured for the devices in the run.</p>"""
    parsing_result_url: NotRequired["aws_sdk_device_farm.types.string.String"]
    """<p>Read-only URL for an object in an S3 bucket where you can get the parsing results of the test package. If the test package doesn't parse, the reason why it doesn't parse appears in the file that this URL points to.</p>"""
    result_code: NotRequired[
        "aws_sdk_device_farm.types.execution_result_code.ExecutionResultCode"
    ]
    """<p>Supporting field for the result field. Set only if <code>result</code> is <code>SKIPPED</code>. <code>PARSING_FAILED</code> if the result is skipped because of test package parsing failure.</p>"""
    seed: NotRequired["aws_sdk_device_farm.types.integer.Integer"]
    """<p>For fuzz tests, this is a seed to use for randomizing the UI fuzz test. Using the same seed value between tests ensures identical event sequences.</p>"""
    app_upload: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>An app to upload or that has been uploaded.</p>"""
    event_count: NotRequired["aws_sdk_device_farm.types.integer.Integer"]
    """<p>For fuzz tests, this is the number of events, between 1 and 10000, that the UI fuzz test should perform.</p>"""
    job_timeout_minutes: NotRequired[
        "aws_sdk_device_farm.types.job_timeout_minutes.JobTimeoutMinutes"
    ]
    """<p>The number of minutes the job executes before it times out.</p>"""
    device_pool_arn: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the device pool for the run.</p>"""
    locale: NotRequired["aws_sdk_device_farm.types.string.String"]
    """<p>Information about the locale that is used for the run.</p>"""
    radios: NotRequired["aws_sdk_device_farm.types.radios.Radios"]
    """<p>Information about the radio states for the run.</p>"""
    location: NotRequired["aws_sdk_device_farm.types.location.Location"]
    """<p>Information about the location that is used for the run.</p>"""
    customer_artifact_paths: NotRequired[
        "aws_sdk_device_farm.types.customer_artifact_paths.CustomerArtifactPaths"
    ]
    """<p>Output <code>CustomerArtifactPaths</code> object for the test run.</p>"""
    web_url: NotRequired["aws_sdk_device_farm.types.string.String"]
    """<p>The Device Farm console URL for the recording of the run.</p>"""
    skip_app_resign: NotRequired[
        "aws_sdk_device_farm.types.skip_app_resign.SkipAppResign"
    ]
    r"""<p>When set to <code>true</code>, for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.</p> <p>For more information about how Device Farm re-signs your apps, see <a href=\"http://aws.amazon.com/device-farm/faqs/\">Do you modify my app?</a> in the <i>AWS Device Farm FAQs</i>.</p>"""
    test_spec_arn: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the YAML-formatted test specification for the run.</p>"""
    device_selection_result: NotRequired[
        "aws_sdk_device_farm.types.device_selection_result.DeviceSelectionResult"
    ]
    """<p>The results of a device filter used to select the devices for a test run.</p>"""
    vpc_config: NotRequired["aws_sdk_device_farm.types.vpc_config.VpcConfig"]
    """<p>The VPC security groups and subnets that are attached to a project.</p>"""
    execution_role_arn: NotRequired[
        "aws_sdk_device_farm.types.amazon_role_resource_name.AmazonRoleResourceName"
    ]
    """<p>The IAM role associated with the run.</p>"""
    environment_variables: NotRequired[
        "aws_sdk_device_farm.types.environment_variables.EnvironmentVariables"
    ]
    """<p>Environment variables associated with the run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Run) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import aws_sdk_device_farm.types.test_type

        out["type"] = aws_sdk_device_farm.types.test_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "platform" in value:
        import aws_sdk_device_farm.types.device_platform

        out["platform"] = (
            aws_sdk_device_farm.types.device_platform.serialize_aws_json_1_1(
                value["platform"]
            )
        )
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
    if "counters" in value:
        import aws_sdk_device_farm.types.counters

        out["counters"] = aws_sdk_device_farm.types.counters.serialize_aws_json_1_1(
            value["counters"]
        )
    if "message" in value:
        out["message"] = value["message"]
    if "total_jobs" in value:
        out["totalJobs"] = value["total_jobs"]
    if "completed_jobs" in value:
        out["completedJobs"] = value["completed_jobs"]
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
    if "network_profile" in value:
        import aws_sdk_device_farm.types.network_profile

        out["networkProfile"] = (
            aws_sdk_device_farm.types.network_profile.serialize_aws_json_1_1(
                value["network_profile"]
            )
        )
    if "device_proxy" in value:
        import aws_sdk_device_farm.types.device_proxy

        out["deviceProxy"] = (
            aws_sdk_device_farm.types.device_proxy.serialize_aws_json_1_1(
                value["device_proxy"]
            )
        )
    if "parsing_result_url" in value:
        out["parsingResultUrl"] = value["parsing_result_url"]
    if "result_code" in value:
        import aws_sdk_device_farm.types.execution_result_code

        out["resultCode"] = (
            aws_sdk_device_farm.types.execution_result_code.serialize_aws_json_1_1(
                value["result_code"]
            )
        )
    if "seed" in value:
        out["seed"] = value["seed"]
    if "app_upload" in value:
        out["appUpload"] = value["app_upload"]
    if "event_count" in value:
        out["eventCount"] = value["event_count"]
    if "job_timeout_minutes" in value:
        out["jobTimeoutMinutes"] = value["job_timeout_minutes"]
    if "device_pool_arn" in value:
        out["devicePoolArn"] = value["device_pool_arn"]
    if "locale" in value:
        out["locale"] = value["locale"]
    if "radios" in value:
        import aws_sdk_device_farm.types.radios

        out["radios"] = aws_sdk_device_farm.types.radios.serialize_aws_json_1_1(
            value["radios"]
        )
    if "location" in value:
        import aws_sdk_device_farm.types.location

        out["location"] = aws_sdk_device_farm.types.location.serialize_aws_json_1_1(
            value["location"]
        )
    if "customer_artifact_paths" in value:
        import aws_sdk_device_farm.types.customer_artifact_paths

        out["customerArtifactPaths"] = (
            aws_sdk_device_farm.types.customer_artifact_paths.serialize_aws_json_1_1(
                value["customer_artifact_paths"]
            )
        )
    if "web_url" in value:
        out["webUrl"] = value["web_url"]
    if "skip_app_resign" in value:
        out["skipAppResign"] = value["skip_app_resign"]
    if "test_spec_arn" in value:
        out["testSpecArn"] = value["test_spec_arn"]
    if "device_selection_result" in value:
        import aws_sdk_device_farm.types.device_selection_result

        out["deviceSelectionResult"] = (
            aws_sdk_device_farm.types.device_selection_result.serialize_aws_json_1_1(
                value["device_selection_result"]
            )
        )
    if "vpc_config" in value:
        import aws_sdk_device_farm.types.vpc_config

        out["vpcConfig"] = aws_sdk_device_farm.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    if "environment_variables" in value:
        import aws_sdk_device_farm.types.environment_variables

        out["environmentVariables"] = (
            aws_sdk_device_farm.types.environment_variables.serialize_aws_json_1_1(
                value["environment_variables"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Run:
    out: Run = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        import aws_sdk_device_farm.types.test_type

        out["type"] = aws_sdk_device_farm.types.test_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if "platform" in data:
        import aws_sdk_device_farm.types.device_platform

        out["platform"] = (
            aws_sdk_device_farm.types.device_platform.deserialize_aws_json_1_1(
                data["platform"]
            )
        )
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
    if "counters" in data:
        import aws_sdk_device_farm.types.counters

        out["counters"] = aws_sdk_device_farm.types.counters.deserialize_aws_json_1_1(
            data["counters"]
        )
    if "message" in data:
        out["message"] = data["message"]
    if "totalJobs" in data:
        out["total_jobs"] = data["totalJobs"]
    if "completedJobs" in data:
        out["completed_jobs"] = data["completedJobs"]
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
    if "networkProfile" in data:
        import aws_sdk_device_farm.types.network_profile

        out["network_profile"] = (
            aws_sdk_device_farm.types.network_profile.deserialize_aws_json_1_1(
                data["networkProfile"]
            )
        )
    if "deviceProxy" in data:
        import aws_sdk_device_farm.types.device_proxy

        out["device_proxy"] = (
            aws_sdk_device_farm.types.device_proxy.deserialize_aws_json_1_1(
                data["deviceProxy"]
            )
        )
    if "parsingResultUrl" in data:
        out["parsing_result_url"] = data["parsingResultUrl"]
    if "resultCode" in data:
        import aws_sdk_device_farm.types.execution_result_code

        out["result_code"] = (
            aws_sdk_device_farm.types.execution_result_code.deserialize_aws_json_1_1(
                data["resultCode"]
            )
        )
    if "seed" in data:
        out["seed"] = data["seed"]
    if "appUpload" in data:
        out["app_upload"] = data["appUpload"]
    if "eventCount" in data:
        out["event_count"] = data["eventCount"]
    if "jobTimeoutMinutes" in data:
        out["job_timeout_minutes"] = data["jobTimeoutMinutes"]
    if "devicePoolArn" in data:
        out["device_pool_arn"] = data["devicePoolArn"]
    if "locale" in data:
        out["locale"] = data["locale"]
    if "radios" in data:
        import aws_sdk_device_farm.types.radios

        out["radios"] = aws_sdk_device_farm.types.radios.deserialize_aws_json_1_1(
            data["radios"]
        )
    if "location" in data:
        import aws_sdk_device_farm.types.location

        out["location"] = aws_sdk_device_farm.types.location.deserialize_aws_json_1_1(
            data["location"]
        )
    if "customerArtifactPaths" in data:
        import aws_sdk_device_farm.types.customer_artifact_paths

        out["customer_artifact_paths"] = (
            aws_sdk_device_farm.types.customer_artifact_paths.deserialize_aws_json_1_1(
                data["customerArtifactPaths"]
            )
        )
    if "webUrl" in data:
        out["web_url"] = data["webUrl"]
    if "skipAppResign" in data:
        out["skip_app_resign"] = data["skipAppResign"]
    if "testSpecArn" in data:
        out["test_spec_arn"] = data["testSpecArn"]
    if "deviceSelectionResult" in data:
        import aws_sdk_device_farm.types.device_selection_result

        out["device_selection_result"] = (
            aws_sdk_device_farm.types.device_selection_result.deserialize_aws_json_1_1(
                data["deviceSelectionResult"]
            )
        )
    if "vpcConfig" in data:
        import aws_sdk_device_farm.types.vpc_config

        out["vpc_config"] = (
            aws_sdk_device_farm.types.vpc_config.deserialize_aws_json_1_1(
                data["vpcConfig"]
            )
        )
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    if "environmentVariables" in data:
        import aws_sdk_device_farm.types.environment_variables

        out["environment_variables"] = (
            aws_sdk_device_farm.types.environment_variables.deserialize_aws_json_1_1(
                data["environmentVariables"]
            )
        )
    return out
