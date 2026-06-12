"""Generated from Smithy shape ``com.amazonaws.devicefarm#ScheduleRunConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name
    import aws_sdk_device_farm.types.amazon_resource_names
    import aws_sdk_device_farm.types.amazon_role_resource_name
    import aws_sdk_device_farm.types.billing_method
    import aws_sdk_device_farm.types.customer_artifact_paths
    import aws_sdk_device_farm.types.device_proxy
    import aws_sdk_device_farm.types.environment_variables
    import aws_sdk_device_farm.types.location
    import aws_sdk_device_farm.types.radios
    import aws_sdk_device_farm.types.string


class ScheduleRunConfiguration(TypedDict):
    extra_data_package_arn: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the extra data for the run. The extra data is a .zip file that AWS Device Farm extracts to external data for Android or the app's sandbox for iOS.</p>"""
    network_profile_arn: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>Reserved for internal use.</p>"""
    locale: NotRequired["aws_sdk_device_farm.types.string.String"]
    """<p>Information about the locale that is used for the run.</p>"""
    location: NotRequired["aws_sdk_device_farm.types.location.Location"]
    """<p>Information about the location that is used for the run.</p>"""
    vpce_configuration_arns: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_names.AmazonResourceNames"
    ]
    """<p>An array of ARNs for your VPC endpoint configurations.</p>"""
    device_proxy: NotRequired["aws_sdk_device_farm.types.device_proxy.DeviceProxy"]
    """<p>The device proxy to be configured on the device for the run.</p>"""
    customer_artifact_paths: NotRequired[
        "aws_sdk_device_farm.types.customer_artifact_paths.CustomerArtifactPaths"
    ]
    """<p>Input <code>CustomerArtifactPaths</code> object for the scheduled run configuration.</p>"""
    radios: NotRequired["aws_sdk_device_farm.types.radios.Radios"]
    """<p>Information about the radio states for the run.</p>"""
    auxiliary_apps: NotRequired[
        "aws_sdk_device_farm.types.amazon_resource_names.AmazonResourceNames"
    ]
    """<p>A list of upload ARNs for app packages to be installed with your app.</p>"""
    billing_method: NotRequired[
        "aws_sdk_device_farm.types.billing_method.BillingMethod"
    ]
    """<p>Specifies the billing method for a test run: <code>metered</code> or <code>unmetered</code>. If the parameter is not specified, the default value is <code>metered</code>.</p> <note> <p>If you have purchased unmetered device slots, you must set this parameter to <code>unmetered</code> to make use of them. Otherwise, your run counts against your metered time.</p> </note>"""
    environment_variables: NotRequired[
        "aws_sdk_device_farm.types.environment_variables.EnvironmentVariables"
    ]
    """<p>Environment variables associated with the run.</p>"""
    execution_role_arn: NotRequired[
        "aws_sdk_device_farm.types.amazon_role_resource_name.AmazonRoleResourceName"
    ]
    """<p>An IAM role to be assumed by the test host for the run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScheduleRunConfiguration) -> dict:
    out: dict = {}
    if "extra_data_package_arn" in value:
        out["extraDataPackageArn"] = value["extra_data_package_arn"]
    if "network_profile_arn" in value:
        out["networkProfileArn"] = value["network_profile_arn"]
    if "locale" in value:
        out["locale"] = value["locale"]
    if "location" in value:
        import aws_sdk_device_farm.types.location

        out["location"] = aws_sdk_device_farm.types.location.serialize_aws_json_1_1(
            value["location"]
        )
    if "vpce_configuration_arns" in value:
        import aws_sdk_device_farm.types.amazon_resource_names

        out["vpceConfigurationArns"] = (
            aws_sdk_device_farm.types.amazon_resource_names.serialize_aws_json_1_1(
                value["vpce_configuration_arns"]
            )
        )
    if "device_proxy" in value:
        import aws_sdk_device_farm.types.device_proxy

        out["deviceProxy"] = (
            aws_sdk_device_farm.types.device_proxy.serialize_aws_json_1_1(
                value["device_proxy"]
            )
        )
    if "customer_artifact_paths" in value:
        import aws_sdk_device_farm.types.customer_artifact_paths

        out["customerArtifactPaths"] = (
            aws_sdk_device_farm.types.customer_artifact_paths.serialize_aws_json_1_1(
                value["customer_artifact_paths"]
            )
        )
    if "radios" in value:
        import aws_sdk_device_farm.types.radios

        out["radios"] = aws_sdk_device_farm.types.radios.serialize_aws_json_1_1(
            value["radios"]
        )
    if "auxiliary_apps" in value:
        import aws_sdk_device_farm.types.amazon_resource_names

        out["auxiliaryApps"] = (
            aws_sdk_device_farm.types.amazon_resource_names.serialize_aws_json_1_1(
                value["auxiliary_apps"]
            )
        )
    if "billing_method" in value:
        import aws_sdk_device_farm.types.billing_method

        out["billingMethod"] = (
            aws_sdk_device_farm.types.billing_method.serialize_aws_json_1_1(
                value["billing_method"]
            )
        )
    if "environment_variables" in value:
        import aws_sdk_device_farm.types.environment_variables

        out["environmentVariables"] = (
            aws_sdk_device_farm.types.environment_variables.serialize_aws_json_1_1(
                value["environment_variables"]
            )
        )
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScheduleRunConfiguration:
    out: ScheduleRunConfiguration = {}  # type: ignore[typeddict-item]
    if "extraDataPackageArn" in data:
        out["extra_data_package_arn"] = data["extraDataPackageArn"]
    if "networkProfileArn" in data:
        out["network_profile_arn"] = data["networkProfileArn"]
    if "locale" in data:
        out["locale"] = data["locale"]
    if "location" in data:
        import aws_sdk_device_farm.types.location

        out["location"] = aws_sdk_device_farm.types.location.deserialize_aws_json_1_1(
            data["location"]
        )
    if "vpceConfigurationArns" in data:
        import aws_sdk_device_farm.types.amazon_resource_names

        out["vpce_configuration_arns"] = (
            aws_sdk_device_farm.types.amazon_resource_names.deserialize_aws_json_1_1(
                data["vpceConfigurationArns"]
            )
        )
    if "deviceProxy" in data:
        import aws_sdk_device_farm.types.device_proxy

        out["device_proxy"] = (
            aws_sdk_device_farm.types.device_proxy.deserialize_aws_json_1_1(
                data["deviceProxy"]
            )
        )
    if "customerArtifactPaths" in data:
        import aws_sdk_device_farm.types.customer_artifact_paths

        out["customer_artifact_paths"] = (
            aws_sdk_device_farm.types.customer_artifact_paths.deserialize_aws_json_1_1(
                data["customerArtifactPaths"]
            )
        )
    if "radios" in data:
        import aws_sdk_device_farm.types.radios

        out["radios"] = aws_sdk_device_farm.types.radios.deserialize_aws_json_1_1(
            data["radios"]
        )
    if "auxiliaryApps" in data:
        import aws_sdk_device_farm.types.amazon_resource_names

        out["auxiliary_apps"] = (
            aws_sdk_device_farm.types.amazon_resource_names.deserialize_aws_json_1_1(
                data["auxiliaryApps"]
            )
        )
    if "billingMethod" in data:
        import aws_sdk_device_farm.types.billing_method

        out["billing_method"] = (
            aws_sdk_device_farm.types.billing_method.deserialize_aws_json_1_1(
                data["billingMethod"]
            )
        )
    if "environmentVariables" in data:
        import aws_sdk_device_farm.types.environment_variables

        out["environment_variables"] = (
            aws_sdk_device_farm.types.environment_variables.deserialize_aws_json_1_1(
                data["environmentVariables"]
            )
        )
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    return out
