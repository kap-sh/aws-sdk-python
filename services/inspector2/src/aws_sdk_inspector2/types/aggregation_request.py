"""Generated from Smithy shape ``com.amazonaws.inspector2#AggregationRequest``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_aggregation
    import aws_sdk_inspector2.types.ami_aggregation
    import aws_sdk_inspector2.types.aws_ecr_container_aggregation
    import aws_sdk_inspector2.types.code_repository_aggregation
    import aws_sdk_inspector2.types.ec2_instance_aggregation
    import aws_sdk_inspector2.types.finding_type_aggregation
    import aws_sdk_inspector2.types.image_layer_aggregation
    import aws_sdk_inspector2.types.lambda_function_aggregation
    import aws_sdk_inspector2.types.lambda_layer_aggregation
    import aws_sdk_inspector2.types.package_aggregation
    import aws_sdk_inspector2.types.repository_aggregation
    import aws_sdk_inspector2.types.title_aggregation


class _AggregationRequest_accountAggregation(TypedDict, closed=True):
    accountAggregation: (
        "aws_sdk_inspector2.types.account_aggregation.AccountAggregation"
    )


class _AggregationRequest_amiAggregation(TypedDict, closed=True):
    amiAggregation: "aws_sdk_inspector2.types.ami_aggregation.AmiAggregation"


class _AggregationRequest_awsEcrContainerAggregation(TypedDict, closed=True):
    awsEcrContainerAggregation: "aws_sdk_inspector2.types.aws_ecr_container_aggregation.AwsEcrContainerAggregation"


class _AggregationRequest_ec2InstanceAggregation(TypedDict, closed=True):
    ec2InstanceAggregation: (
        "aws_sdk_inspector2.types.ec2_instance_aggregation.Ec2InstanceAggregation"
    )


class _AggregationRequest_findingTypeAggregation(TypedDict, closed=True):
    findingTypeAggregation: (
        "aws_sdk_inspector2.types.finding_type_aggregation.FindingTypeAggregation"
    )


class _AggregationRequest_imageLayerAggregation(TypedDict, closed=True):
    imageLayerAggregation: (
        "aws_sdk_inspector2.types.image_layer_aggregation.ImageLayerAggregation"
    )


class _AggregationRequest_packageAggregation(TypedDict, closed=True):
    packageAggregation: (
        "aws_sdk_inspector2.types.package_aggregation.PackageAggregation"
    )


class _AggregationRequest_repositoryAggregation(TypedDict, closed=True):
    repositoryAggregation: (
        "aws_sdk_inspector2.types.repository_aggregation.RepositoryAggregation"
    )


class _AggregationRequest_titleAggregation(TypedDict, closed=True):
    titleAggregation: "aws_sdk_inspector2.types.title_aggregation.TitleAggregation"


class _AggregationRequest_lambdaLayerAggregation(TypedDict, closed=True):
    lambdaLayerAggregation: (
        "aws_sdk_inspector2.types.lambda_layer_aggregation.LambdaLayerAggregation"
    )


class _AggregationRequest_lambdaFunctionAggregation(TypedDict, closed=True):
    lambdaFunctionAggregation: (
        "aws_sdk_inspector2.types.lambda_function_aggregation.LambdaFunctionAggregation"
    )


class _AggregationRequest_codeRepositoryAggregation(TypedDict, closed=True):
    codeRepositoryAggregation: (
        "aws_sdk_inspector2.types.code_repository_aggregation.CodeRepositoryAggregation"
    )


AggregationRequest: TypeAlias = (
    _AggregationRequest_accountAggregation
    | _AggregationRequest_amiAggregation
    | _AggregationRequest_awsEcrContainerAggregation
    | _AggregationRequest_ec2InstanceAggregation
    | _AggregationRequest_findingTypeAggregation
    | _AggregationRequest_imageLayerAggregation
    | _AggregationRequest_packageAggregation
    | _AggregationRequest_repositoryAggregation
    | _AggregationRequest_titleAggregation
    | _AggregationRequest_lambdaLayerAggregation
    | _AggregationRequest_lambdaFunctionAggregation
    | _AggregationRequest_codeRepositoryAggregation
)


# --- restJson1 ser/de ---
def serialize_json(value: AggregationRequest) -> dict:
    if "accountAggregation" in value:
        import aws_sdk_inspector2.types.account_aggregation

        return {
            "accountAggregation": aws_sdk_inspector2.types.account_aggregation.serialize_json(
                value["accountAggregation"]
            )
        }
    elif "amiAggregation" in value:
        import aws_sdk_inspector2.types.ami_aggregation

        return {
            "amiAggregation": aws_sdk_inspector2.types.ami_aggregation.serialize_json(
                value["amiAggregation"]
            )
        }
    elif "awsEcrContainerAggregation" in value:
        import aws_sdk_inspector2.types.aws_ecr_container_aggregation

        return {
            "awsEcrContainerAggregation": aws_sdk_inspector2.types.aws_ecr_container_aggregation.serialize_json(
                value["awsEcrContainerAggregation"]
            )
        }
    elif "ec2InstanceAggregation" in value:
        import aws_sdk_inspector2.types.ec2_instance_aggregation

        return {
            "ec2InstanceAggregation": aws_sdk_inspector2.types.ec2_instance_aggregation.serialize_json(
                value["ec2InstanceAggregation"]
            )
        }
    elif "findingTypeAggregation" in value:
        import aws_sdk_inspector2.types.finding_type_aggregation

        return {
            "findingTypeAggregation": aws_sdk_inspector2.types.finding_type_aggregation.serialize_json(
                value["findingTypeAggregation"]
            )
        }
    elif "imageLayerAggregation" in value:
        import aws_sdk_inspector2.types.image_layer_aggregation

        return {
            "imageLayerAggregation": aws_sdk_inspector2.types.image_layer_aggregation.serialize_json(
                value["imageLayerAggregation"]
            )
        }
    elif "packageAggregation" in value:
        import aws_sdk_inspector2.types.package_aggregation

        return {
            "packageAggregation": aws_sdk_inspector2.types.package_aggregation.serialize_json(
                value["packageAggregation"]
            )
        }
    elif "repositoryAggregation" in value:
        import aws_sdk_inspector2.types.repository_aggregation

        return {
            "repositoryAggregation": aws_sdk_inspector2.types.repository_aggregation.serialize_json(
                value["repositoryAggregation"]
            )
        }
    elif "titleAggregation" in value:
        import aws_sdk_inspector2.types.title_aggregation

        return {
            "titleAggregation": aws_sdk_inspector2.types.title_aggregation.serialize_json(
                value["titleAggregation"]
            )
        }
    elif "lambdaLayerAggregation" in value:
        import aws_sdk_inspector2.types.lambda_layer_aggregation

        return {
            "lambdaLayerAggregation": aws_sdk_inspector2.types.lambda_layer_aggregation.serialize_json(
                value["lambdaLayerAggregation"]
            )
        }
    elif "lambdaFunctionAggregation" in value:
        import aws_sdk_inspector2.types.lambda_function_aggregation

        return {
            "lambdaFunctionAggregation": aws_sdk_inspector2.types.lambda_function_aggregation.serialize_json(
                value["lambdaFunctionAggregation"]
            )
        }
    elif "codeRepositoryAggregation" in value:
        import aws_sdk_inspector2.types.code_repository_aggregation

        return {
            "codeRepositoryAggregation": aws_sdk_inspector2.types.code_repository_aggregation.serialize_json(
                value["codeRepositoryAggregation"]
            )
        }
    else:
        raise SerializationError("AggregationRequest: no variant present")


def deserialize_json(data: dict) -> AggregationRequest:
    if "accountAggregation" in data:
        import aws_sdk_inspector2.types.account_aggregation

        return {
            "accountAggregation": aws_sdk_inspector2.types.account_aggregation.deserialize_json(
                data["accountAggregation"]
            )
        }
    elif "amiAggregation" in data:
        import aws_sdk_inspector2.types.ami_aggregation

        return {
            "amiAggregation": aws_sdk_inspector2.types.ami_aggregation.deserialize_json(
                data["amiAggregation"]
            )
        }
    elif "awsEcrContainerAggregation" in data:
        import aws_sdk_inspector2.types.aws_ecr_container_aggregation

        return {
            "awsEcrContainerAggregation": aws_sdk_inspector2.types.aws_ecr_container_aggregation.deserialize_json(
                data["awsEcrContainerAggregation"]
            )
        }
    elif "ec2InstanceAggregation" in data:
        import aws_sdk_inspector2.types.ec2_instance_aggregation

        return {
            "ec2InstanceAggregation": aws_sdk_inspector2.types.ec2_instance_aggregation.deserialize_json(
                data["ec2InstanceAggregation"]
            )
        }
    elif "findingTypeAggregation" in data:
        import aws_sdk_inspector2.types.finding_type_aggregation

        return {
            "findingTypeAggregation": aws_sdk_inspector2.types.finding_type_aggregation.deserialize_json(
                data["findingTypeAggregation"]
            )
        }
    elif "imageLayerAggregation" in data:
        import aws_sdk_inspector2.types.image_layer_aggregation

        return {
            "imageLayerAggregation": aws_sdk_inspector2.types.image_layer_aggregation.deserialize_json(
                data["imageLayerAggregation"]
            )
        }
    elif "packageAggregation" in data:
        import aws_sdk_inspector2.types.package_aggregation

        return {
            "packageAggregation": aws_sdk_inspector2.types.package_aggregation.deserialize_json(
                data["packageAggregation"]
            )
        }
    elif "repositoryAggregation" in data:
        import aws_sdk_inspector2.types.repository_aggregation

        return {
            "repositoryAggregation": aws_sdk_inspector2.types.repository_aggregation.deserialize_json(
                data["repositoryAggregation"]
            )
        }
    elif "titleAggregation" in data:
        import aws_sdk_inspector2.types.title_aggregation

        return {
            "titleAggregation": aws_sdk_inspector2.types.title_aggregation.deserialize_json(
                data["titleAggregation"]
            )
        }
    elif "lambdaLayerAggregation" in data:
        import aws_sdk_inspector2.types.lambda_layer_aggregation

        return {
            "lambdaLayerAggregation": aws_sdk_inspector2.types.lambda_layer_aggregation.deserialize_json(
                data["lambdaLayerAggregation"]
            )
        }
    elif "lambdaFunctionAggregation" in data:
        import aws_sdk_inspector2.types.lambda_function_aggregation

        return {
            "lambdaFunctionAggregation": aws_sdk_inspector2.types.lambda_function_aggregation.deserialize_json(
                data["lambdaFunctionAggregation"]
            )
        }
    elif "codeRepositoryAggregation" in data:
        import aws_sdk_inspector2.types.code_repository_aggregation

        return {
            "codeRepositoryAggregation": aws_sdk_inspector2.types.code_repository_aggregation.deserialize_json(
                data["codeRepositoryAggregation"]
            )
        }
    else:
        raise DeserializationError("AggregationRequest: no recognized variant key")
