"""Generated from Smithy shape ``com.amazonaws.inspector2#ResourceScanMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.code_repository_metadata
    import capo_inspector2.types.ec2_metadata
    import capo_inspector2.types.ecr_container_image_metadata
    import capo_inspector2.types.ecr_repository_metadata
    import capo_inspector2.types.lambda_function_metadata


class ResourceScanMetadata(TypedDict, closed=True):
    ecr_repository: NotRequired[
        "capo_inspector2.types.ecr_repository_metadata.EcrRepositoryMetadata"
    ]
    """<p>An object that contains details about the repository an Amazon ECR image resides in.</p>"""
    ecr_image: NotRequired[
        "capo_inspector2.types.ecr_container_image_metadata.EcrContainerImageMetadata"
    ]
    """<p>An object that contains details about the container metadata for an Amazon ECR image.</p>"""
    ec2: NotRequired["capo_inspector2.types.ec2_metadata.Ec2Metadata"]
    """<p>An object that contains metadata details for an Amazon EC2 instance.</p>"""
    lambda_function: NotRequired[
        "capo_inspector2.types.lambda_function_metadata.LambdaFunctionMetadata"
    ]
    """<p>An object that contains metadata details for an Amazon Web Services Lambda function.</p>"""
    code_repository: NotRequired[
        "capo_inspector2.types.code_repository_metadata.CodeRepositoryMetadata"
    ]
    """<p>Contains metadata about scan coverage for a code repository resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceScanMetadata) -> dict:
    out: dict = {}
    if "ecr_repository" in value:
        import capo_inspector2.types.ecr_repository_metadata

        out["ecrRepository"] = (
            capo_inspector2.types.ecr_repository_metadata.serialize_json(
                value["ecr_repository"]
            )
        )
    if "ecr_image" in value:
        import capo_inspector2.types.ecr_container_image_metadata

        out["ecrImage"] = (
            capo_inspector2.types.ecr_container_image_metadata.serialize_json(
                value["ecr_image"]
            )
        )
    if "ec2" in value:
        import capo_inspector2.types.ec2_metadata

        out["ec2"] = capo_inspector2.types.ec2_metadata.serialize_json(value["ec2"])
    if "lambda_function" in value:
        import capo_inspector2.types.lambda_function_metadata

        out["lambdaFunction"] = (
            capo_inspector2.types.lambda_function_metadata.serialize_json(
                value["lambda_function"]
            )
        )
    if "code_repository" in value:
        import capo_inspector2.types.code_repository_metadata

        out["codeRepository"] = (
            capo_inspector2.types.code_repository_metadata.serialize_json(
                value["code_repository"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceScanMetadata:
    out: ResourceScanMetadata = {}  # type: ignore[typeddict-item]
    if "ecrRepository" in data:
        import capo_inspector2.types.ecr_repository_metadata

        out["ecr_repository"] = (
            capo_inspector2.types.ecr_repository_metadata.deserialize_json(
                data["ecrRepository"]
            )
        )
    if "ecrImage" in data:
        import capo_inspector2.types.ecr_container_image_metadata

        out["ecr_image"] = (
            capo_inspector2.types.ecr_container_image_metadata.deserialize_json(
                data["ecrImage"]
            )
        )
    if "ec2" in data:
        import capo_inspector2.types.ec2_metadata

        out["ec2"] = capo_inspector2.types.ec2_metadata.deserialize_json(data["ec2"])
    if "lambdaFunction" in data:
        import capo_inspector2.types.lambda_function_metadata

        out["lambda_function"] = (
            capo_inspector2.types.lambda_function_metadata.deserialize_json(
                data["lambdaFunction"]
            )
        )
    if "codeRepository" in data:
        import capo_inspector2.types.code_repository_metadata

        out["code_repository"] = (
            capo_inspector2.types.code_repository_metadata.deserialize_json(
                data["codeRepository"]
            )
        )
    return out
