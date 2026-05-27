"""Generated from Smithy shape ``com.amazonaws.lambda#CreateFunctionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.architectures_list
    import aws_sdk_lambda.types.boolean
    import aws_sdk_lambda.types.capacity_provider_config
    import aws_sdk_lambda.types.code_signing_config_arn
    import aws_sdk_lambda.types.dead_letter_config
    import aws_sdk_lambda.types.description
    import aws_sdk_lambda.types.durable_config
    import aws_sdk_lambda.types.environment
    import aws_sdk_lambda.types.ephemeral_storage
    import aws_sdk_lambda.types.file_system_config_list
    import aws_sdk_lambda.types.function_code
    import aws_sdk_lambda.types.function_name
    import aws_sdk_lambda.types.function_version_latest_published
    import aws_sdk_lambda.types.handler
    import aws_sdk_lambda.types.image_config
    import aws_sdk_lambda.types.kms_key_arn
    import aws_sdk_lambda.types.layer_list
    import aws_sdk_lambda.types.logging_config
    import aws_sdk_lambda.types.memory_size
    import aws_sdk_lambda.types.package_type
    import aws_sdk_lambda.types.role_arn
    import aws_sdk_lambda.types.runtime
    import aws_sdk_lambda.types.snap_start
    import aws_sdk_lambda.types.tags
    import aws_sdk_lambda.types.tenancy_config
    import aws_sdk_lambda.types.timeout
    import aws_sdk_lambda.types.tracing_config
    import aws_sdk_lambda.types.vpc_config


class CreateFunctionRequest(TypedDict):
    function_name: "aws_sdk_lambda.types.function_name.FunctionName"
    """<p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>"""
    runtime: NotRequired["aws_sdk_lambda.types.runtime.Runtime"]
    """<p>The identifier of the function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html\"> runtime</a>. Runtime is required if the deployment package is a .zip file archive. Specifying a runtime results in an error if you're deploying a function using a container image.</p> <p>The following list includes deprecated runtimes. Lambda blocks creating new functions and updating existing functions shortly after each runtime is deprecated. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels\">Runtime use after deprecation</a>.</p> <p>For a list of all currently supported runtimes, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported\">Supported runtimes</a>.</p>"""
    role: "aws_sdk_lambda.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the function's execution role.</p>"""
    handler: NotRequired["aws_sdk_lambda.types.handler.Handler"]
    """<p>The name of the method within your code that Lambda calls to run your function. Handler is required if the deployment package is a .zip file archive. The format includes the file name. It can also include namespaces and other qualifiers, depending on the runtime. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/foundation-progmodel.html\">Lambda programming model</a>.</p>"""
    code: "aws_sdk_lambda.types.function_code.FunctionCode"
    """<p>The code for the function.</p>"""
    description: NotRequired["aws_sdk_lambda.types.description.Description"]
    """<p>A description of the function.</p>"""
    timeout: NotRequired["aws_sdk_lambda.types.timeout.Timeout"]
    """<p>The amount of time (in seconds) that Lambda allows a function to run before stopping it. The default is 3 seconds. The maximum allowed value is 900 seconds. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html\">Lambda execution environment</a>.</p>"""
    memory_size: NotRequired["aws_sdk_lambda.types.memory_size.MemorySize"]
    """<p>The amount of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-memory-console\">memory available to the function</a> at runtime. Increasing the function memory also increases its CPU allocation. The default value is 128 MB. The value can be any multiple of 1 MB.</p>"""
    publish: "aws_sdk_lambda.types.boolean.Boolean"
    """<p>Set to true to publish the first version of the function during creation.</p>"""
    vpc_config: NotRequired["aws_sdk_lambda.types.vpc_config.VpcConfig"]
    """<p>For network connectivity to Amazon Web Services resources in a VPC, specify a list of security groups and subnets in the VPC. When you connect a function to a VPC, it can access resources and the internet only through that VPC. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html\">Configuring a Lambda function to access resources in a VPC</a>.</p>"""
    package_type: NotRequired["aws_sdk_lambda.types.package_type.PackageType"]
    """<p>The type of deployment package. Set to <code>Image</code> for container image and set to <code>Zip</code> for .zip file archive.</p>"""
    dead_letter_config: NotRequired[
        "aws_sdk_lambda.types.dead_letter_config.DeadLetterConfig"
    ]
    """<p>A dead-letter queue configuration that specifies the queue or topic where Lambda sends asynchronous events when they fail processing. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq\">Dead-letter queues</a>.</p>"""
    environment: NotRequired["aws_sdk_lambda.types.environment.Environment"]
    """<p>Environment variables that are accessible from function code during execution.</p>"""
    kms_key_arn: NotRequired["aws_sdk_lambda.types.kms_key_arn.KMSKeyArn"]
    """<p>The ARN of the Key Management Service (KMS) customer managed key that's used to encrypt the following resources:</p> <ul> <li> <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-encryption\">environment variables</a>.</p> </li> <li> <p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart-security.html\">Lambda SnapStart</a> snapshots.</p> </li> <li> <p>When used with <code>SourceKMSKeyArn</code>, the unzipped version of the .zip deployment package that's used for function invocations. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html#enable-zip-custom-encryption\"> Specifying a customer managed key for Lambda</a>.</p> </li> <li> <p>The optimized version of the container image that's used for function invocations. Note that this is not the same key that's used to protect your container image in the Amazon Elastic Container Registry (Amazon ECR). For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-lifecycle\">Function lifecycle</a>.</p> </li> </ul> <p>If you don't provide a customer managed key, Lambda uses an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk\">Amazon Web Services owned key</a> or an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk\">Amazon Web Services managed key</a>.</p>"""
    tracing_config: NotRequired["aws_sdk_lambda.types.tracing_config.TracingConfig"]
    """<p>Set <code>Mode</code> to <code>Active</code> to sample and trace a subset of incoming requests with <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html\">X-Ray</a>.</p>"""
    tags: NotRequired["aws_sdk_lambda.types.tags.Tags"]
    """<p>A list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/tagging.html\">tags</a> to apply to the function.</p>"""
    layers: NotRequired["aws_sdk_lambda.types.layer_list.LayerList"]
    """<p>A list of <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html\">function layers</a> to add to the function's execution environment. Specify each layer by its ARN, including the version.</p>"""
    file_system_configs: NotRequired[
        "aws_sdk_lambda.types.file_system_config_list.FileSystemConfigList"
    ]
    """<p>Connection settings for an Amazon EFS file system or an Amazon S3 Files file system.</p>"""
    image_config: NotRequired["aws_sdk_lambda.types.image_config.ImageConfig"]
    """<p>Container image <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-parms\">configuration values</a> that override the values in the container image Dockerfile.</p>"""
    code_signing_config_arn: NotRequired[
        "aws_sdk_lambda.types.code_signing_config_arn.CodeSigningConfigArn"
    ]
    """<p>To enable code signing for this function, specify the ARN of a code-signing configuration. A code-signing configuration includes a set of signing profiles, which define the trusted publishers for this function.</p>"""
    architectures: NotRequired[
        "aws_sdk_lambda.types.architectures_list.ArchitecturesList"
    ]
    """<p>The instruction set architecture that the function supports. Enter a string array with one of the valid values (arm64 or x86_64). The default value is <code>x86_64</code>.</p>"""
    ephemeral_storage: NotRequired[
        "aws_sdk_lambda.types.ephemeral_storage.EphemeralStorage"
    ]
    """<p>The size of the function's <code>/tmp</code> directory in MB. The default value is 512, but can be any whole number between 512 and 10,240 MB. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html#configuration-ephemeral-storage\">Configuring ephemeral storage (console)</a>.</p>"""
    snap_start: NotRequired["aws_sdk_lambda.types.snap_start.SnapStart"]
    """<p>The function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html\">SnapStart</a> setting.</p>"""
    logging_config: NotRequired["aws_sdk_lambda.types.logging_config.LoggingConfig"]
    """<p>The function's Amazon CloudWatch Logs configuration settings.</p>"""
    capacity_provider_config: NotRequired[
        "aws_sdk_lambda.types.capacity_provider_config.CapacityProviderConfig"
    ]
    """<p>Configuration for the capacity provider that manages compute resources for Lambda functions.</p>"""
    publish_to: NotRequired[
        "aws_sdk_lambda.types.function_version_latest_published.FunctionVersionLatestPublished"
    ]
    """<p>Specifies where to publish the function version or configuration.</p>"""
    durable_config: NotRequired["aws_sdk_lambda.types.durable_config.DurableConfig"]
    """<p>Configuration settings for durable functions. Enables creating functions with durability that can remember their state and continue execution even after interruptions.</p>"""
    tenancy_config: NotRequired["aws_sdk_lambda.types.tenancy_config.TenancyConfig"]
    """<p>Configuration for multi-tenant applications that use Lambda functions. Defines tenant isolation settings and resource allocations. Required for functions supporting multiple tenants.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFunctionRequest) -> dict:
    out: dict = {}
    out["FunctionName"] = value["function_name"]
    if "runtime" in value:
        import aws_sdk_lambda.types.runtime

        out["Runtime"] = aws_sdk_lambda.types.runtime.serialize_json(value["runtime"])
    out["Role"] = value["role"]
    if "handler" in value:
        out["Handler"] = value["handler"]
    import aws_sdk_lambda.types.function_code

    out["Code"] = aws_sdk_lambda.types.function_code.serialize_json(value["code"])
    if "description" in value:
        out["Description"] = value["description"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "memory_size" in value:
        out["MemorySize"] = value["memory_size"]
    out["Publish"] = value.get("publish", False)
    if "vpc_config" in value:
        import aws_sdk_lambda.types.vpc_config

        out["VpcConfig"] = aws_sdk_lambda.types.vpc_config.serialize_json(
            value["vpc_config"]
        )
    if "package_type" in value:
        import aws_sdk_lambda.types.package_type

        out["PackageType"] = aws_sdk_lambda.types.package_type.serialize_json(
            value["package_type"]
        )
    if "dead_letter_config" in value:
        import aws_sdk_lambda.types.dead_letter_config

        out["DeadLetterConfig"] = (
            aws_sdk_lambda.types.dead_letter_config.serialize_json(
                value["dead_letter_config"]
            )
        )
    if "environment" in value:
        import aws_sdk_lambda.types.environment

        out["Environment"] = aws_sdk_lambda.types.environment.serialize_json(
            value["environment"]
        )
    if "kms_key_arn" in value:
        out["KMSKeyArn"] = value["kms_key_arn"]
    if "tracing_config" in value:
        import aws_sdk_lambda.types.tracing_config

        out["TracingConfig"] = aws_sdk_lambda.types.tracing_config.serialize_json(
            value["tracing_config"]
        )
    if "tags" in value:
        import aws_sdk_lambda.types.tags

        out["Tags"] = aws_sdk_lambda.types.tags.serialize_json(value["tags"])
    if "layers" in value:
        import aws_sdk_lambda.types.layer_list

        out["Layers"] = aws_sdk_lambda.types.layer_list.serialize_json(value["layers"])
    if "file_system_configs" in value:
        import aws_sdk_lambda.types.file_system_config_list

        out["FileSystemConfigs"] = (
            aws_sdk_lambda.types.file_system_config_list.serialize_json(
                value["file_system_configs"]
            )
        )
    if "image_config" in value:
        import aws_sdk_lambda.types.image_config

        out["ImageConfig"] = aws_sdk_lambda.types.image_config.serialize_json(
            value["image_config"]
        )
    if "code_signing_config_arn" in value:
        out["CodeSigningConfigArn"] = value["code_signing_config_arn"]
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
        import aws_sdk_lambda.types.snap_start

        out["SnapStart"] = aws_sdk_lambda.types.snap_start.serialize_json(
            value["snap_start"]
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
    if "publish_to" in value:
        import aws_sdk_lambda.types.function_version_latest_published

        out["PublishTo"] = (
            aws_sdk_lambda.types.function_version_latest_published.serialize_json(
                value["publish_to"]
            )
        )
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


def deserialize_json(data: dict) -> CreateFunctionRequest:
    out: CreateFunctionRequest = {}  # type: ignore[typeddict-item]
    if "FunctionName" in data:
        out["function_name"] = data["FunctionName"]
    else:
        raise DeserializationError("CreateFunctionRequest.function_name required")
    if "Runtime" in data:
        import aws_sdk_lambda.types.runtime

        out["runtime"] = aws_sdk_lambda.types.runtime.deserialize_json(data["Runtime"])
    if "Role" in data:
        out["role"] = data["Role"]
    else:
        raise DeserializationError("CreateFunctionRequest.role required")
    if "Handler" in data:
        out["handler"] = data["Handler"]
    if "Code" in data:
        import aws_sdk_lambda.types.function_code

        out["code"] = aws_sdk_lambda.types.function_code.deserialize_json(data["Code"])
    else:
        raise DeserializationError("CreateFunctionRequest.code required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Timeout" in data:
        out["timeout"] = data["Timeout"]
    if "MemorySize" in data:
        out["memory_size"] = data["MemorySize"]
    if "Publish" in data:
        out["publish"] = data["Publish"]
    else:
        out["publish"] = False
    if "VpcConfig" in data:
        import aws_sdk_lambda.types.vpc_config

        out["vpc_config"] = aws_sdk_lambda.types.vpc_config.deserialize_json(
            data["VpcConfig"]
        )
    if "PackageType" in data:
        import aws_sdk_lambda.types.package_type

        out["package_type"] = aws_sdk_lambda.types.package_type.deserialize_json(
            data["PackageType"]
        )
    if "DeadLetterConfig" in data:
        import aws_sdk_lambda.types.dead_letter_config

        out["dead_letter_config"] = (
            aws_sdk_lambda.types.dead_letter_config.deserialize_json(
                data["DeadLetterConfig"]
            )
        )
    if "Environment" in data:
        import aws_sdk_lambda.types.environment

        out["environment"] = aws_sdk_lambda.types.environment.deserialize_json(
            data["Environment"]
        )
    if "KMSKeyArn" in data:
        out["kms_key_arn"] = data["KMSKeyArn"]
    if "TracingConfig" in data:
        import aws_sdk_lambda.types.tracing_config

        out["tracing_config"] = aws_sdk_lambda.types.tracing_config.deserialize_json(
            data["TracingConfig"]
        )
    if "Tags" in data:
        import aws_sdk_lambda.types.tags

        out["tags"] = aws_sdk_lambda.types.tags.deserialize_json(data["Tags"])
    if "Layers" in data:
        import aws_sdk_lambda.types.layer_list

        out["layers"] = aws_sdk_lambda.types.layer_list.deserialize_json(data["Layers"])
    if "FileSystemConfigs" in data:
        import aws_sdk_lambda.types.file_system_config_list

        out["file_system_configs"] = (
            aws_sdk_lambda.types.file_system_config_list.deserialize_json(
                data["FileSystemConfigs"]
            )
        )
    if "ImageConfig" in data:
        import aws_sdk_lambda.types.image_config

        out["image_config"] = aws_sdk_lambda.types.image_config.deserialize_json(
            data["ImageConfig"]
        )
    if "CodeSigningConfigArn" in data:
        out["code_signing_config_arn"] = data["CodeSigningConfigArn"]
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
        import aws_sdk_lambda.types.snap_start

        out["snap_start"] = aws_sdk_lambda.types.snap_start.deserialize_json(
            data["SnapStart"]
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
    if "PublishTo" in data:
        import aws_sdk_lambda.types.function_version_latest_published

        out["publish_to"] = (
            aws_sdk_lambda.types.function_version_latest_published.deserialize_json(
                data["PublishTo"]
            )
        )
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
