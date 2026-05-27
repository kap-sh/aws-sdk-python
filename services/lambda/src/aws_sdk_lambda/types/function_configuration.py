"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.architectures_list
    import aws_sdk_lambda.types.arn
    import aws_sdk_lambda.types.capacity_provider_config
    import aws_sdk_lambda.types.dead_letter_config
    import aws_sdk_lambda.types.description
    import aws_sdk_lambda.types.durable_config
    import aws_sdk_lambda.types.environment_response
    import aws_sdk_lambda.types.ephemeral_storage
    import aws_sdk_lambda.types.file_system_config_list
    import aws_sdk_lambda.types.function_arn
    import aws_sdk_lambda.types.handler
    import aws_sdk_lambda.types.image_config_response
    import aws_sdk_lambda.types.kms_key_arn
    import aws_sdk_lambda.types.last_update_status
    import aws_sdk_lambda.types.last_update_status_reason
    import aws_sdk_lambda.types.last_update_status_reason_code
    import aws_sdk_lambda.types.layers_reference_list
    import aws_sdk_lambda.types.logging_config
    import aws_sdk_lambda.types.long
    import aws_sdk_lambda.types.memory_size
    import aws_sdk_lambda.types.name_spaced_function_arn
    import aws_sdk_lambda.types.namespaced_function_name
    import aws_sdk_lambda.types.package_type
    import aws_sdk_lambda.types.role_arn
    import aws_sdk_lambda.types.runtime
    import aws_sdk_lambda.types.runtime_version_config
    import aws_sdk_lambda.types.snap_start_response
    import aws_sdk_lambda.types.state
    import aws_sdk_lambda.types.state_reason
    import aws_sdk_lambda.types.state_reason_code
    import aws_sdk_lambda.types.string
    import aws_sdk_lambda.types.tenancy_config
    import aws_sdk_lambda.types.timeout
    import aws_sdk_lambda.types.timestamp
    import aws_sdk_lambda.types.tracing_config_response
    import aws_sdk_lambda.types.version
    import aws_sdk_lambda.types.vpc_config_response


class FunctionConfiguration(TypedDict):
    function_name: NotRequired[
        "aws_sdk_lambda.types.namespaced_function_name.NamespacedFunctionName"
    ]
    """<p>The name of the function.</p>"""
    function_arn: NotRequired[
        "aws_sdk_lambda.types.name_spaced_function_arn.NameSpacedFunctionArn"
    ]
    """<p>The function's Amazon Resource Name (ARN).</p>"""
    runtime: NotRequired["aws_sdk_lambda.types.runtime.Runtime"]
    """<p>The identifier of the function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html\"> runtime</a>. Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if you're deploying a function using a container image.</p> <p>The following list includes deprecated runtimes. Lambda blocks creating new functions and updating existing functions shortly after each runtime is deprecated. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels\">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported\">Supported runtimes</a>.</p>"""
    role: NotRequired["aws_sdk_lambda.types.role_arn.RoleArn"]
    """<p>The function's execution role.</p>"""
    handler: NotRequired["aws_sdk_lambda.types.handler.Handler"]
    """<p>The function that Lambda calls to begin running your function.</p>"""
    code_size: "aws_sdk_lambda.types.long.Long"
    """<p>The size of the function's deployment package, in bytes.</p>"""
    description: NotRequired["aws_sdk_lambda.types.description.Description"]
    """<p>The function's description.</p>"""
    timeout: NotRequired["aws_sdk_lambda.types.timeout.Timeout"]
    """<p>The amount of time in seconds that Lambda allows a function to run before stopping it.</p>"""
    memory_size: NotRequired["aws_sdk_lambda.types.memory_size.MemorySize"]
    """<p>The amount of memory available to the function at runtime.</p>"""
    last_modified: NotRequired["aws_sdk_lambda.types.timestamp.Timestamp"]
    """<p>The date and time that the function was last updated, in <a href=\"https://www.w3.org/TR/NOTE-datetime\">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    code_sha256: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The SHA256 hash of the function's deployment package.</p>"""
    version: NotRequired["aws_sdk_lambda.types.version.Version"]
    """<p>The version of the Lambda function.</p>"""
    vpc_config: NotRequired[
        "aws_sdk_lambda.types.vpc_config_response.VpcConfigResponse"
    ]
    """<p>The function's networking configuration.</p>"""
    dead_letter_config: NotRequired[
        "aws_sdk_lambda.types.dead_letter_config.DeadLetterConfig"
    ]
    """<p>The function's dead letter queue.</p>"""
    environment: NotRequired[
        "aws_sdk_lambda.types.environment_response.EnvironmentResponse"
    ]
    """<p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html\">environment variables</a>. Omitted from CloudTrail logs.</p>"""
    kms_key_arn: NotRequired["aws_sdk_lambda.types.kms_key_arn.KMSKeyArn"]
    """<p>The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt the following resources:</p> <ul> <li> <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption\">environment variables</a>.</p> </li> <li> <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html\">Lambda SnapStart</a> snapshots.</p> </li> <li> <p>When used with <code>SourceKMSKeyArn</code>, the unzipped version of the .zip deployment package that's used for function invocations. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html#enable-zip-custom-encryption\"> Specifying a customer managed key for Lambda</a>.</p> </li> <li> <p>The optimized version of the container image that's used for function invocations. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-lifecycle\">Function lifecycle</a>.</p> </li> </ul> <p>If you don't provide a customer managed key, Lambda uses an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk\">Amazon Web Services owned key</a> or an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk\">Amazon Web Services managed key</a>.</p>"""
    tracing_config: NotRequired[
        "aws_sdk_lambda.types.tracing_config_response.TracingConfigResponse"
    ]
    """<p>The function's X-Ray tracing configuration.</p>"""
    master_arn: NotRequired["aws_sdk_lambda.types.function_arn.FunctionArn"]
    """<p>For Lambda@Edge functions, the ARN of the main function.</p>"""
    revision_id: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The latest updated revision of the function or alias.</p>"""
    layers: NotRequired[
        "aws_sdk_lambda.types.layers_reference_list.LayersReferenceList"
    ]
    """<p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html\">layers</a>.</p>"""
    state: NotRequired["aws_sdk_lambda.types.state.State"]
    """<p>The current state of the function. When the state is <code>Inactive</code>, you can reactivate the function by invoking it.</p>"""
    state_reason: NotRequired["aws_sdk_lambda.types.state_reason.StateReason"]
    """<p>The reason for the function's current state.</p>"""
    state_reason_code: NotRequired[
        "aws_sdk_lambda.types.state_reason_code.StateReasonCode"
    ]
    """<p>The reason code for the function's current state. When the code is <code>Creating</code>, you can't invoke or modify the function.</p>"""
    last_update_status: NotRequired[
        "aws_sdk_lambda.types.last_update_status.LastUpdateStatus"
    ]
    """<p>The status of the last update that was performed on the function. This is first set to <code>Successful</code> after function creation completes.</p>"""
    last_update_status_reason: NotRequired[
        "aws_sdk_lambda.types.last_update_status_reason.LastUpdateStatusReason"
    ]
    """<p>The reason for the last update that was performed on the function.</p>"""
    last_update_status_reason_code: NotRequired[
        "aws_sdk_lambda.types.last_update_status_reason_code.LastUpdateStatusReasonCode"
    ]
    """<p>The reason code for the last update that was performed on the function.</p>"""
    file_system_configs: NotRequired[
        "aws_sdk_lambda.types.file_system_config_list.FileSystemConfigList"
    ]
    """<p>Connection settings for an <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html\">Amazon EFS file system</a> or an <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html\">Amazon S3 Files file system</a>.</p>"""
    package_type: NotRequired["aws_sdk_lambda.types.package_type.PackageType"]
    """<p>The type of deployment package. Set to <code>Image</code> for container image and set <code>Zip</code> for .zip file archive.</p>"""
    image_config_response: NotRequired[
        "aws_sdk_lambda.types.image_config_response.ImageConfigResponse"
    ]
    """<p>The function's image configuration values.</p>"""
    signing_profile_version_arn: NotRequired["aws_sdk_lambda.types.arn.Arn"]
    """<p>The ARN of the signing profile version.</p>"""
    signing_job_arn: NotRequired["aws_sdk_lambda.types.arn.Arn"]
    """<p>The ARN of the signing job.</p>"""
    architectures: NotRequired[
        "aws_sdk_lambda.types.architectures_list.ArchitecturesList"
    ]
    """<p>The instruction set architecture that the function supports. Architecture is a string array with one of the valid values. The default architecture value is <code>x86_64</code>.</p>"""
    ephemeral_storage: NotRequired[
        "aws_sdk_lambda.types.ephemeral_storage.EphemeralStorage"
    ]
    """<p>The size of the function's <code>/tmp</code> directory in MB. The default value is 512, but can be any whole number between 512 and 10,240 MB. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-ephemeral-storage\">Configuring ephemeral storage (console)</a>.</p>"""
    snap_start: NotRequired[
        "aws_sdk_lambda.types.snap_start_response.SnapStartResponse"
    ]
    """<p>Set <code>ApplyOn</code> to <code>PublishedVersions</code> to create a snapshot of the initialized execution environment when you publish a function version. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html\">Improving startup performance with Lambda SnapStart</a>.</p>"""
    runtime_version_config: NotRequired[
        "aws_sdk_lambda.types.runtime_version_config.RuntimeVersionConfig"
    ]
    """<p>The ARN of the runtime and any errors that occured.</p>"""
    logging_config: NotRequired["aws_sdk_lambda.types.logging_config.LoggingConfig"]
    """<p>The function's Amazon CloudWatch Logs configuration settings.</p>"""
    capacity_provider_config: NotRequired[
        "aws_sdk_lambda.types.capacity_provider_config.CapacityProviderConfig"
    ]
    """<p>Configuration for the capacity provider that manages compute resources for Lambda functions.</p>"""
    config_sha256: NotRequired["aws_sdk_lambda.types.string.String"]
    """<p>The SHA256 hash of the function configuration.</p>"""
    durable_config: NotRequired["aws_sdk_lambda.types.durable_config.DurableConfig"]
    """<p>The function's durable execution configuration settings, if the function is configured for durability.</p>"""
    tenancy_config: NotRequired["aws_sdk_lambda.types.tenancy_config.TenancyConfig"]
    """<p>The function's tenant isolation configuration settings. Determines whether the Lambda function runs on a shared or dedicated infrastructure per unique tenant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionConfiguration) -> dict:
    out: dict = {}
    if "function_name" in value:
        out["FunctionName"] = value["function_name"]
    if "function_arn" in value:
        out["FunctionArn"] = value["function_arn"]
    if "runtime" in value:
        import aws_sdk_lambda.types.runtime

        out["Runtime"] = aws_sdk_lambda.types.runtime.serialize_json(value["runtime"])
    if "role" in value:
        out["Role"] = value["role"]
    if "handler" in value:
        out["Handler"] = value["handler"]
    out["CodeSize"] = value.get("code_size", 0)
    if "description" in value:
        out["Description"] = value["description"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "memory_size" in value:
        out["MemorySize"] = value["memory_size"]
    if "last_modified" in value:
        out["LastModified"] = value["last_modified"]
    if "code_sha256" in value:
        out["CodeSha256"] = value["code_sha256"]
    if "version" in value:
        out["Version"] = value["version"]
    if "vpc_config" in value:
        import aws_sdk_lambda.types.vpc_config_response

        out["VpcConfig"] = aws_sdk_lambda.types.vpc_config_response.serialize_json(
            value["vpc_config"]
        )
    if "dead_letter_config" in value:
        import aws_sdk_lambda.types.dead_letter_config

        out["DeadLetterConfig"] = (
            aws_sdk_lambda.types.dead_letter_config.serialize_json(
                value["dead_letter_config"]
            )
        )
    if "environment" in value:
        import aws_sdk_lambda.types.environment_response

        out["Environment"] = aws_sdk_lambda.types.environment_response.serialize_json(
            value["environment"]
        )
    if "kms_key_arn" in value:
        out["KMSKeyArn"] = value["kms_key_arn"]
    if "tracing_config" in value:
        import aws_sdk_lambda.types.tracing_config_response

        out["TracingConfig"] = (
            aws_sdk_lambda.types.tracing_config_response.serialize_json(
                value["tracing_config"]
            )
        )
    if "master_arn" in value:
        out["MasterArn"] = value["master_arn"]
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    if "layers" in value:
        import aws_sdk_lambda.types.layers_reference_list

        out["Layers"] = aws_sdk_lambda.types.layers_reference_list.serialize_json(
            value["layers"]
        )
    if "state" in value:
        import aws_sdk_lambda.types.state

        out["State"] = aws_sdk_lambda.types.state.serialize_json(value["state"])
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "state_reason_code" in value:
        import aws_sdk_lambda.types.state_reason_code

        out["StateReasonCode"] = aws_sdk_lambda.types.state_reason_code.serialize_json(
            value["state_reason_code"]
        )
    if "last_update_status" in value:
        import aws_sdk_lambda.types.last_update_status

        out["LastUpdateStatus"] = (
            aws_sdk_lambda.types.last_update_status.serialize_json(
                value["last_update_status"]
            )
        )
    if "last_update_status_reason" in value:
        out["LastUpdateStatusReason"] = value["last_update_status_reason"]
    if "last_update_status_reason_code" in value:
        import aws_sdk_lambda.types.last_update_status_reason_code

        out["LastUpdateStatusReasonCode"] = (
            aws_sdk_lambda.types.last_update_status_reason_code.serialize_json(
                value["last_update_status_reason_code"]
            )
        )
    if "file_system_configs" in value:
        import aws_sdk_lambda.types.file_system_config_list

        out["FileSystemConfigs"] = (
            aws_sdk_lambda.types.file_system_config_list.serialize_json(
                value["file_system_configs"]
            )
        )
    if "package_type" in value:
        import aws_sdk_lambda.types.package_type

        out["PackageType"] = aws_sdk_lambda.types.package_type.serialize_json(
            value["package_type"]
        )
    if "image_config_response" in value:
        import aws_sdk_lambda.types.image_config_response

        out["ImageConfigResponse"] = (
            aws_sdk_lambda.types.image_config_response.serialize_json(
                value["image_config_response"]
            )
        )
    if "signing_profile_version_arn" in value:
        out["SigningProfileVersionArn"] = value["signing_profile_version_arn"]
    if "signing_job_arn" in value:
        out["SigningJobArn"] = value["signing_job_arn"]
    if "architectures" in value:
        import aws_sdk_lambda.types.architectures_list

        out["Architectures"] = aws_sdk_lambda.types.architectures_list.serialize_json(
            value["architectures"]
        )
    if "ephemeral_storage" in value:
        import aws_sdk_lambda.types.ephemeral_storage

        out["EphemeralStorage"] = aws_sdk_lambda.types.ephemeral_storage.serialize_json(
            value["ephemeral_storage"]
        )
    if "snap_start" in value:
        import aws_sdk_lambda.types.snap_start_response

        out["SnapStart"] = aws_sdk_lambda.types.snap_start_response.serialize_json(
            value["snap_start"]
        )
    if "runtime_version_config" in value:
        import aws_sdk_lambda.types.runtime_version_config

        out["RuntimeVersionConfig"] = (
            aws_sdk_lambda.types.runtime_version_config.serialize_json(
                value["runtime_version_config"]
            )
        )
    if "logging_config" in value:
        import aws_sdk_lambda.types.logging_config

        out["LoggingConfig"] = aws_sdk_lambda.types.logging_config.serialize_json(
            value["logging_config"]
        )
    if "capacity_provider_config" in value:
        import aws_sdk_lambda.types.capacity_provider_config

        out["CapacityProviderConfig"] = (
            aws_sdk_lambda.types.capacity_provider_config.serialize_json(
                value["capacity_provider_config"]
            )
        )
    if "config_sha256" in value:
        out["ConfigSha256"] = value["config_sha256"]
    if "durable_config" in value:
        import aws_sdk_lambda.types.durable_config

        out["DurableConfig"] = aws_sdk_lambda.types.durable_config.serialize_json(
            value["durable_config"]
        )
    if "tenancy_config" in value:
        import aws_sdk_lambda.types.tenancy_config

        out["TenancyConfig"] = aws_sdk_lambda.types.tenancy_config.serialize_json(
            value["tenancy_config"]
        )
    return out


def deserialize_json(data: dict) -> FunctionConfiguration:
    out: FunctionConfiguration = {}  # type: ignore[typeddict-item]
    if "FunctionName" in data:
        out["function_name"] = data["FunctionName"]
    if "FunctionArn" in data:
        out["function_arn"] = data["FunctionArn"]
    if "Runtime" in data:
        import aws_sdk_lambda.types.runtime

        out["runtime"] = aws_sdk_lambda.types.runtime.deserialize_json(data["Runtime"])
    if "Role" in data:
        out["role"] = data["Role"]
    if "Handler" in data:
        out["handler"] = data["Handler"]
    if "CodeSize" in data:
        out["code_size"] = data["CodeSize"]
    else:
        out["code_size"] = 0
    if "Description" in data:
        out["description"] = data["Description"]
    if "Timeout" in data:
        out["timeout"] = data["Timeout"]
    if "MemorySize" in data:
        out["memory_size"] = data["MemorySize"]
    if "LastModified" in data:
        out["last_modified"] = data["LastModified"]
    if "CodeSha256" in data:
        out["code_sha256"] = data["CodeSha256"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "VpcConfig" in data:
        import aws_sdk_lambda.types.vpc_config_response

        out["vpc_config"] = aws_sdk_lambda.types.vpc_config_response.deserialize_json(
            data["VpcConfig"]
        )
    if "DeadLetterConfig" in data:
        import aws_sdk_lambda.types.dead_letter_config

        out["dead_letter_config"] = (
            aws_sdk_lambda.types.dead_letter_config.deserialize_json(
                data["DeadLetterConfig"]
            )
        )
    if "Environment" in data:
        import aws_sdk_lambda.types.environment_response

        out["environment"] = aws_sdk_lambda.types.environment_response.deserialize_json(
            data["Environment"]
        )
    if "KMSKeyArn" in data:
        out["kms_key_arn"] = data["KMSKeyArn"]
    if "TracingConfig" in data:
        import aws_sdk_lambda.types.tracing_config_response

        out["tracing_config"] = (
            aws_sdk_lambda.types.tracing_config_response.deserialize_json(
                data["TracingConfig"]
            )
        )
    if "MasterArn" in data:
        out["master_arn"] = data["MasterArn"]
    if "RevisionId" in data:
        out["revision_id"] = data["RevisionId"]
    if "Layers" in data:
        import aws_sdk_lambda.types.layers_reference_list

        out["layers"] = aws_sdk_lambda.types.layers_reference_list.deserialize_json(
            data["Layers"]
        )
    if "State" in data:
        import aws_sdk_lambda.types.state

        out["state"] = aws_sdk_lambda.types.state.deserialize_json(data["State"])
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    if "StateReasonCode" in data:
        import aws_sdk_lambda.types.state_reason_code

        out["state_reason_code"] = (
            aws_sdk_lambda.types.state_reason_code.deserialize_json(
                data["StateReasonCode"]
            )
        )
    if "LastUpdateStatus" in data:
        import aws_sdk_lambda.types.last_update_status

        out["last_update_status"] = (
            aws_sdk_lambda.types.last_update_status.deserialize_json(
                data["LastUpdateStatus"]
            )
        )
    if "LastUpdateStatusReason" in data:
        out["last_update_status_reason"] = data["LastUpdateStatusReason"]
    if "LastUpdateStatusReasonCode" in data:
        import aws_sdk_lambda.types.last_update_status_reason_code

        out["last_update_status_reason_code"] = (
            aws_sdk_lambda.types.last_update_status_reason_code.deserialize_json(
                data["LastUpdateStatusReasonCode"]
            )
        )
    if "FileSystemConfigs" in data:
        import aws_sdk_lambda.types.file_system_config_list

        out["file_system_configs"] = (
            aws_sdk_lambda.types.file_system_config_list.deserialize_json(
                data["FileSystemConfigs"]
            )
        )
    if "PackageType" in data:
        import aws_sdk_lambda.types.package_type

        out["package_type"] = aws_sdk_lambda.types.package_type.deserialize_json(
            data["PackageType"]
        )
    if "ImageConfigResponse" in data:
        import aws_sdk_lambda.types.image_config_response

        out["image_config_response"] = (
            aws_sdk_lambda.types.image_config_response.deserialize_json(
                data["ImageConfigResponse"]
            )
        )
    if "SigningProfileVersionArn" in data:
        out["signing_profile_version_arn"] = data["SigningProfileVersionArn"]
    if "SigningJobArn" in data:
        out["signing_job_arn"] = data["SigningJobArn"]
    if "Architectures" in data:
        import aws_sdk_lambda.types.architectures_list

        out["architectures"] = aws_sdk_lambda.types.architectures_list.deserialize_json(
            data["Architectures"]
        )
    if "EphemeralStorage" in data:
        import aws_sdk_lambda.types.ephemeral_storage

        out["ephemeral_storage"] = (
            aws_sdk_lambda.types.ephemeral_storage.deserialize_json(
                data["EphemeralStorage"]
            )
        )
    if "SnapStart" in data:
        import aws_sdk_lambda.types.snap_start_response

        out["snap_start"] = aws_sdk_lambda.types.snap_start_response.deserialize_json(
            data["SnapStart"]
        )
    if "RuntimeVersionConfig" in data:
        import aws_sdk_lambda.types.runtime_version_config

        out["runtime_version_config"] = (
            aws_sdk_lambda.types.runtime_version_config.deserialize_json(
                data["RuntimeVersionConfig"]
            )
        )
    if "LoggingConfig" in data:
        import aws_sdk_lambda.types.logging_config

        out["logging_config"] = aws_sdk_lambda.types.logging_config.deserialize_json(
            data["LoggingConfig"]
        )
    if "CapacityProviderConfig" in data:
        import aws_sdk_lambda.types.capacity_provider_config

        out["capacity_provider_config"] = (
            aws_sdk_lambda.types.capacity_provider_config.deserialize_json(
                data["CapacityProviderConfig"]
            )
        )
    if "ConfigSha256" in data:
        out["config_sha256"] = data["ConfigSha256"]
    if "DurableConfig" in data:
        import aws_sdk_lambda.types.durable_config

        out["durable_config"] = aws_sdk_lambda.types.durable_config.deserialize_json(
            data["DurableConfig"]
        )
    if "TenancyConfig" in data:
        import aws_sdk_lambda.types.tenancy_config

        out["tenancy_config"] = aws_sdk_lambda.types.tenancy_config.deserialize_json(
            data["TenancyConfig"]
        )
    return out
