"""Generated from Smithy shape ``com.amazonaws.inspector2#AggregationResponse``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_aggregation_response
    import aws_sdk_inspector2.types.ami_aggregation_response
    import aws_sdk_inspector2.types.aws_ecr_container_aggregation_response
    import aws_sdk_inspector2.types.code_repository_aggregation_response
    import aws_sdk_inspector2.types.ec2_instance_aggregation_response
    import aws_sdk_inspector2.types.finding_type_aggregation_response
    import aws_sdk_inspector2.types.image_layer_aggregation_response
    import aws_sdk_inspector2.types.lambda_function_aggregation_response
    import aws_sdk_inspector2.types.lambda_layer_aggregation_response
    import aws_sdk_inspector2.types.package_aggregation_response
    import aws_sdk_inspector2.types.repository_aggregation_response
    import aws_sdk_inspector2.types.title_aggregation_response


class _AggregationResponse_accountAggregation(TypedDict, closed=True):
    accountAggregation: "aws_sdk_inspector2.types.account_aggregation_response.AccountAggregationResponse"


class _AggregationResponse_amiAggregation(TypedDict, closed=True):
    amiAggregation: (
        "aws_sdk_inspector2.types.ami_aggregation_response.AmiAggregationResponse"
    )


class _AggregationResponse_awsEcrContainerAggregation(TypedDict, closed=True):
    awsEcrContainerAggregation: "aws_sdk_inspector2.types.aws_ecr_container_aggregation_response.AwsEcrContainerAggregationResponse"


class _AggregationResponse_ec2InstanceAggregation(TypedDict, closed=True):
    ec2InstanceAggregation: "aws_sdk_inspector2.types.ec2_instance_aggregation_response.Ec2InstanceAggregationResponse"


class _AggregationResponse_findingTypeAggregation(TypedDict, closed=True):
    findingTypeAggregation: "aws_sdk_inspector2.types.finding_type_aggregation_response.FindingTypeAggregationResponse"


class _AggregationResponse_imageLayerAggregation(TypedDict, closed=True):
    imageLayerAggregation: "aws_sdk_inspector2.types.image_layer_aggregation_response.ImageLayerAggregationResponse"


class _AggregationResponse_packageAggregation(TypedDict, closed=True):
    packageAggregation: "aws_sdk_inspector2.types.package_aggregation_response.PackageAggregationResponse"


class _AggregationResponse_repositoryAggregation(TypedDict, closed=True):
    repositoryAggregation: "aws_sdk_inspector2.types.repository_aggregation_response.RepositoryAggregationResponse"


class _AggregationResponse_titleAggregation(TypedDict, closed=True):
    titleAggregation: (
        "aws_sdk_inspector2.types.title_aggregation_response.TitleAggregationResponse"
    )


class _AggregationResponse_lambdaLayerAggregation(TypedDict, closed=True):
    lambdaLayerAggregation: "aws_sdk_inspector2.types.lambda_layer_aggregation_response.LambdaLayerAggregationResponse"


class _AggregationResponse_lambdaFunctionAggregation(TypedDict, closed=True):
    lambdaFunctionAggregation: "aws_sdk_inspector2.types.lambda_function_aggregation_response.LambdaFunctionAggregationResponse"


class _AggregationResponse_codeRepositoryAggregation(TypedDict, closed=True):
    codeRepositoryAggregation: "aws_sdk_inspector2.types.code_repository_aggregation_response.CodeRepositoryAggregationResponse"


AggregationResponse: TypeAlias = (
    _AggregationResponse_accountAggregation
    | _AggregationResponse_amiAggregation
    | _AggregationResponse_awsEcrContainerAggregation
    | _AggregationResponse_ec2InstanceAggregation
    | _AggregationResponse_findingTypeAggregation
    | _AggregationResponse_imageLayerAggregation
    | _AggregationResponse_packageAggregation
    | _AggregationResponse_repositoryAggregation
    | _AggregationResponse_titleAggregation
    | _AggregationResponse_lambdaLayerAggregation
    | _AggregationResponse_lambdaFunctionAggregation
    | _AggregationResponse_codeRepositoryAggregation
)


# --- restJson1 ser/de ---
def serialize_json(value: AggregationResponse) -> dict:
    if "accountAggregation" in value:
        import aws_sdk_inspector2.types.account_aggregation_response

        return {
            "accountAggregation": aws_sdk_inspector2.types.account_aggregation_response.serialize_json(
                value["accountAggregation"]
            )
        }
    elif "amiAggregation" in value:
        import aws_sdk_inspector2.types.ami_aggregation_response

        return {
            "amiAggregation": aws_sdk_inspector2.types.ami_aggregation_response.serialize_json(
                value["amiAggregation"]
            )
        }
    elif "awsEcrContainerAggregation" in value:
        import aws_sdk_inspector2.types.aws_ecr_container_aggregation_response

        return {
            "awsEcrContainerAggregation": aws_sdk_inspector2.types.aws_ecr_container_aggregation_response.serialize_json(
                value["awsEcrContainerAggregation"]
            )
        }
    elif "ec2InstanceAggregation" in value:
        import aws_sdk_inspector2.types.ec2_instance_aggregation_response

        return {
            "ec2InstanceAggregation": aws_sdk_inspector2.types.ec2_instance_aggregation_response.serialize_json(
                value["ec2InstanceAggregation"]
            )
        }
    elif "findingTypeAggregation" in value:
        import aws_sdk_inspector2.types.finding_type_aggregation_response

        return {
            "findingTypeAggregation": aws_sdk_inspector2.types.finding_type_aggregation_response.serialize_json(
                value["findingTypeAggregation"]
            )
        }
    elif "imageLayerAggregation" in value:
        import aws_sdk_inspector2.types.image_layer_aggregation_response

        return {
            "imageLayerAggregation": aws_sdk_inspector2.types.image_layer_aggregation_response.serialize_json(
                value["imageLayerAggregation"]
            )
        }
    elif "packageAggregation" in value:
        import aws_sdk_inspector2.types.package_aggregation_response

        return {
            "packageAggregation": aws_sdk_inspector2.types.package_aggregation_response.serialize_json(
                value["packageAggregation"]
            )
        }
    elif "repositoryAggregation" in value:
        import aws_sdk_inspector2.types.repository_aggregation_response

        return {
            "repositoryAggregation": aws_sdk_inspector2.types.repository_aggregation_response.serialize_json(
                value["repositoryAggregation"]
            )
        }
    elif "titleAggregation" in value:
        import aws_sdk_inspector2.types.title_aggregation_response

        return {
            "titleAggregation": aws_sdk_inspector2.types.title_aggregation_response.serialize_json(
                value["titleAggregation"]
            )
        }
    elif "lambdaLayerAggregation" in value:
        import aws_sdk_inspector2.types.lambda_layer_aggregation_response

        return {
            "lambdaLayerAggregation": aws_sdk_inspector2.types.lambda_layer_aggregation_response.serialize_json(
                value["lambdaLayerAggregation"]
            )
        }
    elif "lambdaFunctionAggregation" in value:
        import aws_sdk_inspector2.types.lambda_function_aggregation_response

        return {
            "lambdaFunctionAggregation": aws_sdk_inspector2.types.lambda_function_aggregation_response.serialize_json(
                value["lambdaFunctionAggregation"]
            )
        }
    elif "codeRepositoryAggregation" in value:
        import aws_sdk_inspector2.types.code_repository_aggregation_response

        return {
            "codeRepositoryAggregation": aws_sdk_inspector2.types.code_repository_aggregation_response.serialize_json(
                value["codeRepositoryAggregation"]
            )
        }
    else:
        raise SerializationError("AggregationResponse: no variant present")


def deserialize_json(data: dict) -> AggregationResponse:
    if "accountAggregation" in data:
        import aws_sdk_inspector2.types.account_aggregation_response

        return {
            "accountAggregation": aws_sdk_inspector2.types.account_aggregation_response.deserialize_json(
                data["accountAggregation"]
            )
        }
    elif "amiAggregation" in data:
        import aws_sdk_inspector2.types.ami_aggregation_response

        return {
            "amiAggregation": aws_sdk_inspector2.types.ami_aggregation_response.deserialize_json(
                data["amiAggregation"]
            )
        }
    elif "awsEcrContainerAggregation" in data:
        import aws_sdk_inspector2.types.aws_ecr_container_aggregation_response

        return {
            "awsEcrContainerAggregation": aws_sdk_inspector2.types.aws_ecr_container_aggregation_response.deserialize_json(
                data["awsEcrContainerAggregation"]
            )
        }
    elif "ec2InstanceAggregation" in data:
        import aws_sdk_inspector2.types.ec2_instance_aggregation_response

        return {
            "ec2InstanceAggregation": aws_sdk_inspector2.types.ec2_instance_aggregation_response.deserialize_json(
                data["ec2InstanceAggregation"]
            )
        }
    elif "findingTypeAggregation" in data:
        import aws_sdk_inspector2.types.finding_type_aggregation_response

        return {
            "findingTypeAggregation": aws_sdk_inspector2.types.finding_type_aggregation_response.deserialize_json(
                data["findingTypeAggregation"]
            )
        }
    elif "imageLayerAggregation" in data:
        import aws_sdk_inspector2.types.image_layer_aggregation_response

        return {
            "imageLayerAggregation": aws_sdk_inspector2.types.image_layer_aggregation_response.deserialize_json(
                data["imageLayerAggregation"]
            )
        }
    elif "packageAggregation" in data:
        import aws_sdk_inspector2.types.package_aggregation_response

        return {
            "packageAggregation": aws_sdk_inspector2.types.package_aggregation_response.deserialize_json(
                data["packageAggregation"]
            )
        }
    elif "repositoryAggregation" in data:
        import aws_sdk_inspector2.types.repository_aggregation_response

        return {
            "repositoryAggregation": aws_sdk_inspector2.types.repository_aggregation_response.deserialize_json(
                data["repositoryAggregation"]
            )
        }
    elif "titleAggregation" in data:
        import aws_sdk_inspector2.types.title_aggregation_response

        return {
            "titleAggregation": aws_sdk_inspector2.types.title_aggregation_response.deserialize_json(
                data["titleAggregation"]
            )
        }
    elif "lambdaLayerAggregation" in data:
        import aws_sdk_inspector2.types.lambda_layer_aggregation_response

        return {
            "lambdaLayerAggregation": aws_sdk_inspector2.types.lambda_layer_aggregation_response.deserialize_json(
                data["lambdaLayerAggregation"]
            )
        }
    elif "lambdaFunctionAggregation" in data:
        import aws_sdk_inspector2.types.lambda_function_aggregation_response

        return {
            "lambdaFunctionAggregation": aws_sdk_inspector2.types.lambda_function_aggregation_response.deserialize_json(
                data["lambdaFunctionAggregation"]
            )
        }
    elif "codeRepositoryAggregation" in data:
        import aws_sdk_inspector2.types.code_repository_aggregation_response

        return {
            "codeRepositoryAggregation": aws_sdk_inspector2.types.code_repository_aggregation_response.deserialize_json(
                data["codeRepositoryAggregation"]
            )
        }
    else:
        raise DeserializationError("AggregationResponse: no recognized variant key")
