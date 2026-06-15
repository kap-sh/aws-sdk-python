"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsLambdaFunctionDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_lambda_function_code
    import aws_sdk_securityhub.types.aws_lambda_function_dead_letter_config
    import aws_sdk_securityhub.types.aws_lambda_function_environment
    import aws_sdk_securityhub.types.aws_lambda_function_layer_list
    import aws_sdk_securityhub.types.aws_lambda_function_tracing_config
    import aws_sdk_securityhub.types.aws_lambda_function_vpc_config
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.non_empty_string_list


class AwsLambdaFunctionDetails(TypedDict):
    code: NotRequired[
        "aws_sdk_securityhub.types.aws_lambda_function_code.AwsLambdaFunctionCode"
    ]
    """<p>An <code>AwsLambdaFunctionCode</code> object.</p>"""
    code_sha256: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The SHA256 hash of the function's deployment package.</p>"""
    dead_letter_config: NotRequired[
        "aws_sdk_securityhub.types.aws_lambda_function_dead_letter_config.AwsLambdaFunctionDeadLetterConfig"
    ]
    """<p>The function's dead letter queue.</p>"""
    environment: NotRequired[
        "aws_sdk_securityhub.types.aws_lambda_function_environment.AwsLambdaFunctionEnvironment"
    ]
    """<p>The function's environment variables.</p>"""
    function_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the function.</p>"""
    handler: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The function that Lambda calls to begin executing your function.</p>"""
    kms_key_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The KMS key that is used to encrypt the function's environment variables. This key is only returned if you've configured a customer managed customer managed key.</p>"""
    last_modified: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>Indicates when the function was last updated.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    layers: NotRequired[
        "aws_sdk_securityhub.types.aws_lambda_function_layer_list.AwsLambdaFunctionLayerList"
    ]
    """<p>The function's layers.</p>"""
    master_arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>For Lambda@Edge functions, the ARN of the master function.</p>"""
    memory_size: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The memory that is allocated to the function.</p>"""
    revision_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The latest updated revision of the function or alias.</p>"""
    role: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The function's execution role.</p>"""
    runtime: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The runtime environment for the Lambda function.</p>"""
    timeout: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The amount of time that Lambda allows a function to run before stopping it.</p>"""
    tracing_config: NotRequired[
        "aws_sdk_securityhub.types.aws_lambda_function_tracing_config.AwsLambdaFunctionTracingConfig"
    ]
    """<p>The function's X-Ray tracing configuration.</p>"""
    vpc_config: NotRequired[
        "aws_sdk_securityhub.types.aws_lambda_function_vpc_config.AwsLambdaFunctionVpcConfig"
    ]
    """<p>The function's networking configuration.</p>"""
    version: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The version of the Lambda function.</p>"""
    architectures: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The instruction set architecture that the function uses. Valid values are <code>x86_64</code> or <code>arm64</code>.</p>"""
    package_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The type of deployment package that's used to deploy the function code to Lambda. Set to <code>Image</code> for a container image and <code>Zip</code> for a .zip file archive. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsLambdaFunctionDetails) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_securityhub.types.aws_lambda_function_code

        out["Code"] = aws_sdk_securityhub.types.aws_lambda_function_code.serialize_json(
            value["code"]
        )
    if "code_sha256" in value:
        out["CodeSha256"] = value["code_sha256"]
    if "dead_letter_config" in value:
        import aws_sdk_securityhub.types.aws_lambda_function_dead_letter_config

        out["DeadLetterConfig"] = (
            aws_sdk_securityhub.types.aws_lambda_function_dead_letter_config.serialize_json(
                value["dead_letter_config"]
            )
        )
    if "environment" in value:
        import aws_sdk_securityhub.types.aws_lambda_function_environment

        out["Environment"] = (
            aws_sdk_securityhub.types.aws_lambda_function_environment.serialize_json(
                value["environment"]
            )
        )
    if "function_name" in value:
        out["FunctionName"] = value["function_name"]
    if "handler" in value:
        out["Handler"] = value["handler"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "last_modified" in value:
        out["LastModified"] = value["last_modified"]
    if "layers" in value:
        import aws_sdk_securityhub.types.aws_lambda_function_layer_list

        out["Layers"] = (
            aws_sdk_securityhub.types.aws_lambda_function_layer_list.serialize_json(
                value["layers"]
            )
        )
    if "master_arn" in value:
        out["MasterArn"] = value["master_arn"]
    if "memory_size" in value:
        out["MemorySize"] = value["memory_size"]
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    if "role" in value:
        out["Role"] = value["role"]
    if "runtime" in value:
        out["Runtime"] = value["runtime"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "tracing_config" in value:
        import aws_sdk_securityhub.types.aws_lambda_function_tracing_config

        out["TracingConfig"] = (
            aws_sdk_securityhub.types.aws_lambda_function_tracing_config.serialize_json(
                value["tracing_config"]
            )
        )
    if "vpc_config" in value:
        import aws_sdk_securityhub.types.aws_lambda_function_vpc_config

        out["VpcConfig"] = (
            aws_sdk_securityhub.types.aws_lambda_function_vpc_config.serialize_json(
                value["vpc_config"]
            )
        )
    if "version" in value:
        out["Version"] = value["version"]
    if "architectures" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["Architectures"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["architectures"]
            )
        )
    if "package_type" in value:
        out["PackageType"] = value["package_type"]
    return out


def deserialize_json(data: dict) -> AwsLambdaFunctionDetails:
    out: AwsLambdaFunctionDetails = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import aws_sdk_securityhub.types.aws_lambda_function_code

        out["code"] = (
            aws_sdk_securityhub.types.aws_lambda_function_code.deserialize_json(
                data["Code"]
            )
        )
    if "CodeSha256" in data:
        out["code_sha256"] = data["CodeSha256"]
    if "DeadLetterConfig" in data:
        import aws_sdk_securityhub.types.aws_lambda_function_dead_letter_config

        out["dead_letter_config"] = (
            aws_sdk_securityhub.types.aws_lambda_function_dead_letter_config.deserialize_json(
                data["DeadLetterConfig"]
            )
        )
    if "Environment" in data:
        import aws_sdk_securityhub.types.aws_lambda_function_environment

        out["environment"] = (
            aws_sdk_securityhub.types.aws_lambda_function_environment.deserialize_json(
                data["Environment"]
            )
        )
    if "FunctionName" in data:
        out["function_name"] = data["FunctionName"]
    if "Handler" in data:
        out["handler"] = data["Handler"]
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if "LastModified" in data:
        out["last_modified"] = data["LastModified"]
    if "Layers" in data:
        import aws_sdk_securityhub.types.aws_lambda_function_layer_list

        out["layers"] = (
            aws_sdk_securityhub.types.aws_lambda_function_layer_list.deserialize_json(
                data["Layers"]
            )
        )
    if "MasterArn" in data:
        out["master_arn"] = data["MasterArn"]
    if "MemorySize" in data:
        out["memory_size"] = data["MemorySize"]
    if "RevisionId" in data:
        out["revision_id"] = data["RevisionId"]
    if "Role" in data:
        out["role"] = data["Role"]
    if "Runtime" in data:
        out["runtime"] = data["Runtime"]
    if "Timeout" in data:
        out["timeout"] = data["Timeout"]
    if "TracingConfig" in data:
        import aws_sdk_securityhub.types.aws_lambda_function_tracing_config

        out["tracing_config"] = (
            aws_sdk_securityhub.types.aws_lambda_function_tracing_config.deserialize_json(
                data["TracingConfig"]
            )
        )
    if "VpcConfig" in data:
        import aws_sdk_securityhub.types.aws_lambda_function_vpc_config

        out["vpc_config"] = (
            aws_sdk_securityhub.types.aws_lambda_function_vpc_config.deserialize_json(
                data["VpcConfig"]
            )
        )
    if "Version" in data:
        out["version"] = data["Version"]
    if "Architectures" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["architectures"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["Architectures"]
            )
        )
    if "PackageType" in data:
        out["package_type"] = data["PackageType"]
    return out
