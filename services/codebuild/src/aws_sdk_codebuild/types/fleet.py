"""Generated from Smithy shape ``com.amazonaws.codebuild#Fleet``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.compute_configuration
    import aws_sdk_codebuild.types.compute_type
    import aws_sdk_codebuild.types.environment_type
    import aws_sdk_codebuild.types.fleet_capacity
    import aws_sdk_codebuild.types.fleet_name
    import aws_sdk_codebuild.types.fleet_overflow_behavior
    import aws_sdk_codebuild.types.fleet_status
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.proxy_configuration
    import aws_sdk_codebuild.types.scaling_configuration_output
    import aws_sdk_codebuild.types.tag_list
    import aws_sdk_codebuild.types.timestamp
    import aws_sdk_codebuild.types.vpc_config


class Fleet(TypedDict):
    arn: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the compute fleet.</p>"""
    name: NotRequired["aws_sdk_codebuild.types.fleet_name.FleetName"]
    """<p>The name of the compute fleet.</p>"""
    id: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the compute fleet.</p>"""
    created: NotRequired["aws_sdk_codebuild.types.timestamp.Timestamp"]
    """<p>The time at which the compute fleet was created.</p>"""
    last_modified: NotRequired["aws_sdk_codebuild.types.timestamp.Timestamp"]
    """<p>The time at which the compute fleet was last modified.</p>"""
    status: NotRequired["aws_sdk_codebuild.types.fleet_status.FleetStatus"]
    """<p>The status of the compute fleet.</p>"""
    base_capacity: NotRequired["aws_sdk_codebuild.types.fleet_capacity.FleetCapacity"]
    """<p>The initial number of machines allocated to the compute ﬂeet, which deﬁnes the number of builds that can run in parallel.</p>"""
    environment_type: NotRequired[
        "aws_sdk_codebuild.types.environment_type.EnvironmentType"
    ]
    r"""<p>The environment type of the compute fleet.</p> <ul> <li> <p>The environment type <code>ARM_CONTAINER</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), Asia Pacific (Mumbai), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), EU (Frankfurt), and South America (São Paulo).</p> </li> <li> <p>The environment type <code>ARM_EC2</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).</p> </li> <li> <p>The environment type <code>LINUX_CONTAINER</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).</p> </li> <li> <p>The environment type <code>LINUX_EC2</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).</p> </li> <li> <p>The environment type <code>LINUX_GPU_CONTAINER</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), and Asia Pacific (Sydney).</p> </li> <li> <p>The environment type <code>MAC_ARM</code> is available for Medium fleets only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Sydney), and EU (Frankfurt)</p> </li> <li> <p>The environment type <code>MAC_ARM</code> is available for Large fleets only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), and Asia Pacific (Sydney).</p> </li> <li> <p>The environment type <code>WINDOWS_EC2</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Tokyo), Asia Pacific (Singapore), Asia Pacific (Sydney), South America (São Paulo), and Asia Pacific (Mumbai).</p> </li> <li> <p>The environment type <code>WINDOWS_SERVER_2019_CONTAINER</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Sydney), Asia Pacific (Tokyo), Asia Pacific (Mumbai) and EU (Ireland).</p> </li> <li> <p>The environment type <code>WINDOWS_SERVER_2022_CONTAINER</code> is available only in regions US East (N. Virginia), US East (Ohio), US West (Oregon), EU (Ireland), EU (Frankfurt), Asia Pacific (Sydney), Asia Pacific (Singapore), Asia Pacific (Tokyo), South America (São Paulo) and Asia Pacific (Mumbai).</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html\">Build environment compute types</a> in the <i>CodeBuild user guide</i>.</p>"""
    compute_type: NotRequired["aws_sdk_codebuild.types.compute_type.ComputeType"]
    r"""<p>Information about the compute resources the compute fleet uses. Available values include:</p> <ul> <li> <p> <code>ATTRIBUTE_BASED_COMPUTE</code>: Specify the amount of vCPUs, memory, disk space, and the type of machine.</p> <note> <p> If you use <code>ATTRIBUTE_BASED_COMPUTE</code>, you must define your attributes by using <code>computeConfiguration</code>. CodeBuild will select the cheapest instance that satisfies your specified attributes. For more information, see <a href=\"https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment-reserved-capacity.types\">Reserved capacity environment types</a> in the <i>CodeBuild User Guide</i>.</p> </note> </li> <li> <p> <code>CUSTOM_INSTANCE_TYPE</code>: Specify the instance type for your compute fleet. For a list of supported instance types, see <a href=\"https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment-reserved-capacity.instance-types\">Supported instance families </a> in the <i>CodeBuild User Guide</i>.</p> </li> <li> <p> <code>BUILD_GENERAL1_SMALL</code>: Use up to 4 GiB memory and 2 vCPUs for builds.</p> </li> <li> <p> <code>BUILD_GENERAL1_MEDIUM</code>: Use up to 8 GiB memory and 4 vCPUs for builds.</p> </li> <li> <p> <code>BUILD_GENERAL1_LARGE</code>: Use up to 16 GiB memory and 8 vCPUs for builds, depending on your environment type.</p> </li> <li> <p> <code>BUILD_GENERAL1_XLARGE</code>: Use up to 72 GiB memory and 36 vCPUs for builds, depending on your environment type.</p> </li> <li> <p> <code>BUILD_GENERAL1_2XLARGE</code>: Use up to 144 GiB memory, 72 vCPUs, and 824 GB of SSD storage for builds. This compute type supports Docker images up to 100 GB uncompressed.</p> </li> <li> <p> <code>BUILD_LAMBDA_1GB</code>: Use up to 1 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> <li> <p> <code>BUILD_LAMBDA_2GB</code>: Use up to 2 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> <li> <p> <code>BUILD_LAMBDA_4GB</code>: Use up to 4 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> <li> <p> <code>BUILD_LAMBDA_8GB</code>: Use up to 8 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> <li> <p> <code>BUILD_LAMBDA_10GB</code>: Use up to 10 GiB memory for builds. Only available for environment type <code>LINUX_LAMBDA_CONTAINER</code> and <code>ARM_LAMBDA_CONTAINER</code>.</p> </li> </ul> <p> If you use <code>BUILD_GENERAL1_SMALL</code>: </p> <ul> <li> <p> For environment type <code>LINUX_CONTAINER</code>, you can use up to 4 GiB memory and 2 vCPUs for builds. </p> </li> <li> <p> For environment type <code>LINUX_GPU_CONTAINER</code>, you can use up to 16 GiB memory, 4 vCPUs, and 1 NVIDIA A10G Tensor Core GPU for builds.</p> </li> <li> <p> For environment type <code>ARM_CONTAINER</code>, you can use up to 4 GiB memory and 2 vCPUs on ARM-based processors for builds.</p> </li> </ul> <p> If you use <code>BUILD_GENERAL1_LARGE</code>: </p> <ul> <li> <p> For environment type <code>LINUX_CONTAINER</code>, you can use up to 16 GiB memory and 8 vCPUs for builds. </p> </li> <li> <p> For environment type <code>LINUX_GPU_CONTAINER</code>, you can use up to 255 GiB memory, 32 vCPUs, and 4 NVIDIA Tesla V100 GPUs for builds.</p> </li> <li> <p> For environment type <code>ARM_CONTAINER</code>, you can use up to 16 GiB memory and 8 vCPUs on ARM-based processors for builds.</p> </li> </ul> <p>For more information, see <a href=\"https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html#environment.types\">On-demand environment types</a> in the <i>CodeBuild User Guide.</i> </p>"""
    compute_configuration: NotRequired[
        "aws_sdk_codebuild.types.compute_configuration.ComputeConfiguration"
    ]
    """<p>The compute configuration of the compute fleet. This is only required if <code>computeType</code> is set to <code>ATTRIBUTE_BASED_COMPUTE</code> or <code>CUSTOM_INSTANCE_TYPE</code>.</p>"""
    scaling_configuration: NotRequired[
        "aws_sdk_codebuild.types.scaling_configuration_output.ScalingConfigurationOutput"
    ]
    """<p>The scaling configuration of the compute fleet.</p>"""
    overflow_behavior: NotRequired[
        "aws_sdk_codebuild.types.fleet_overflow_behavior.FleetOverflowBehavior"
    ]
    r"""<p>The compute fleet overflow behavior.</p> <ul> <li> <p>For overflow behavior <code>QUEUE</code>, your overflow builds need to wait on the existing fleet instance to become available.</p> </li> <li> <p>For overflow behavior <code>ON_DEMAND</code>, your overflow builds run on CodeBuild on-demand.</p> <note> <p>If you choose to set your overflow behavior to on-demand while creating a VPC-connected fleet, make sure that you add the required VPC permissions to your project service role. For more information, see <a href=\"https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#customer-managed-policies-example-create-vpc-network-interface\">Example policy statement to allow CodeBuild access to Amazon Web Services services required to create a VPC network interface</a>.</p> </note> </li> </ul>"""
    vpc_config: NotRequired["aws_sdk_codebuild.types.vpc_config.VpcConfig"]
    proxy_configuration: NotRequired[
        "aws_sdk_codebuild.types.proxy_configuration.ProxyConfiguration"
    ]
    """<p>The proxy configuration of the compute fleet.</p>"""
    image_id: NotRequired["aws_sdk_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Machine Image (AMI) of the compute fleet.</p>"""
    fleet_service_role: NotRequired[
        "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>The service role associated with the compute fleet. For more information, see <a href=\"https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#customer-managed-policies-example-permission-policy-fleet-service-role.html\"> Allow a user to add a permission policy for a fleet service role</a> in the <i>CodeBuild User Guide</i>.</p>"""
    tags: NotRequired["aws_sdk_codebuild.types.tag_list.TagList"]
    """<p>A list of tag key and value pairs associated with this compute fleet.</p> <p>These tags are available for use by Amazon Web Services services that support CodeBuild build project tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Fleet) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "id" in value:
        out["id"] = value["id"]
    if "created" in value:
        import aws_sdk_codebuild.types.timestamp

        out["created"] = aws_sdk_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["created"]
        )
    if "last_modified" in value:
        import aws_sdk_codebuild.types.timestamp

        out["lastModified"] = aws_sdk_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["last_modified"]
        )
    if "status" in value:
        import aws_sdk_codebuild.types.fleet_status

        out["status"] = aws_sdk_codebuild.types.fleet_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "base_capacity" in value:
        out["baseCapacity"] = value["base_capacity"]
    if "environment_type" in value:
        import aws_sdk_codebuild.types.environment_type

        out["environmentType"] = (
            aws_sdk_codebuild.types.environment_type.serialize_aws_json_1_1(
                value["environment_type"]
            )
        )
    if "compute_type" in value:
        import aws_sdk_codebuild.types.compute_type

        out["computeType"] = (
            aws_sdk_codebuild.types.compute_type.serialize_aws_json_1_1(
                value["compute_type"]
            )
        )
    if "compute_configuration" in value:
        import aws_sdk_codebuild.types.compute_configuration

        out["computeConfiguration"] = (
            aws_sdk_codebuild.types.compute_configuration.serialize_aws_json_1_1(
                value["compute_configuration"]
            )
        )
    if "scaling_configuration" in value:
        import aws_sdk_codebuild.types.scaling_configuration_output

        out["scalingConfiguration"] = (
            aws_sdk_codebuild.types.scaling_configuration_output.serialize_aws_json_1_1(
                value["scaling_configuration"]
            )
        )
    if "overflow_behavior" in value:
        import aws_sdk_codebuild.types.fleet_overflow_behavior

        out["overflowBehavior"] = (
            aws_sdk_codebuild.types.fleet_overflow_behavior.serialize_aws_json_1_1(
                value["overflow_behavior"]
            )
        )
    if "vpc_config" in value:
        import aws_sdk_codebuild.types.vpc_config

        out["vpcConfig"] = aws_sdk_codebuild.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "proxy_configuration" in value:
        import aws_sdk_codebuild.types.proxy_configuration

        out["proxyConfiguration"] = (
            aws_sdk_codebuild.types.proxy_configuration.serialize_aws_json_1_1(
                value["proxy_configuration"]
            )
        )
    if "image_id" in value:
        out["imageId"] = value["image_id"]
    if "fleet_service_role" in value:
        out["fleetServiceRole"] = value["fleet_service_role"]
    if "tags" in value:
        import aws_sdk_codebuild.types.tag_list

        out["tags"] = aws_sdk_codebuild.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Fleet:
    out: Fleet = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "id" in data:
        out["id"] = data["id"]
    if "created" in data:
        import aws_sdk_codebuild.types.timestamp

        out["created"] = aws_sdk_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["created"]
        )
    if "lastModified" in data:
        import aws_sdk_codebuild.types.timestamp

        out["last_modified"] = (
            aws_sdk_codebuild.types.timestamp.deserialize_aws_json_1_1(
                data["lastModified"]
            )
        )
    if "status" in data:
        import aws_sdk_codebuild.types.fleet_status

        out["status"] = aws_sdk_codebuild.types.fleet_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if "baseCapacity" in data:
        out["base_capacity"] = data["baseCapacity"]
    if "environmentType" in data:
        import aws_sdk_codebuild.types.environment_type

        out["environment_type"] = (
            aws_sdk_codebuild.types.environment_type.deserialize_aws_json_1_1(
                data["environmentType"]
            )
        )
    if "computeType" in data:
        import aws_sdk_codebuild.types.compute_type

        out["compute_type"] = (
            aws_sdk_codebuild.types.compute_type.deserialize_aws_json_1_1(
                data["computeType"]
            )
        )
    if "computeConfiguration" in data:
        import aws_sdk_codebuild.types.compute_configuration

        out["compute_configuration"] = (
            aws_sdk_codebuild.types.compute_configuration.deserialize_aws_json_1_1(
                data["computeConfiguration"]
            )
        )
    if "scalingConfiguration" in data:
        import aws_sdk_codebuild.types.scaling_configuration_output

        out["scaling_configuration"] = (
            aws_sdk_codebuild.types.scaling_configuration_output.deserialize_aws_json_1_1(
                data["scalingConfiguration"]
            )
        )
    if "overflowBehavior" in data:
        import aws_sdk_codebuild.types.fleet_overflow_behavior

        out["overflow_behavior"] = (
            aws_sdk_codebuild.types.fleet_overflow_behavior.deserialize_aws_json_1_1(
                data["overflowBehavior"]
            )
        )
    if "vpcConfig" in data:
        import aws_sdk_codebuild.types.vpc_config

        out["vpc_config"] = aws_sdk_codebuild.types.vpc_config.deserialize_aws_json_1_1(
            data["vpcConfig"]
        )
    if "proxyConfiguration" in data:
        import aws_sdk_codebuild.types.proxy_configuration

        out["proxy_configuration"] = (
            aws_sdk_codebuild.types.proxy_configuration.deserialize_aws_json_1_1(
                data["proxyConfiguration"]
            )
        )
    if "imageId" in data:
        out["image_id"] = data["imageId"]
    if "fleetServiceRole" in data:
        out["fleet_service_role"] = data["fleetServiceRole"]
    if "tags" in data:
        import aws_sdk_codebuild.types.tag_list

        out["tags"] = aws_sdk_codebuild.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
