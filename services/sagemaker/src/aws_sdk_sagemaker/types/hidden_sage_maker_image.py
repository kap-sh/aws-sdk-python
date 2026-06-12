"""Generated from Smithy shape ``com.amazonaws.sagemaker#HiddenSageMakerImage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.sage_maker_image_name
    import aws_sdk_sagemaker.types.version_aliases_list


class HiddenSageMakerImage(TypedDict):
    sage_maker_image_name: NotRequired[
        "aws_sdk_sagemaker.types.sage_maker_image_name.SageMakerImageName"
    ]
    """<p> The SageMaker image name that you are hiding from the Studio user interface. </p>"""
    version_aliases: NotRequired[
        "aws_sdk_sagemaker.types.version_aliases_list.VersionAliasesList"
    ]
    """<p> The version aliases you are hiding from the Studio user interface. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HiddenSageMakerImage) -> dict:
    out: dict = {}
    if "sage_maker_image_name" in value:
        import aws_sdk_sagemaker.types.sage_maker_image_name

        out["SageMakerImageName"] = (
            aws_sdk_sagemaker.types.sage_maker_image_name.serialize_aws_json_1_1(
                value["sage_maker_image_name"]
            )
        )
    if "version_aliases" in value:
        import aws_sdk_sagemaker.types.version_aliases_list

        out["VersionAliases"] = (
            aws_sdk_sagemaker.types.version_aliases_list.serialize_aws_json_1_1(
                value["version_aliases"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HiddenSageMakerImage:
    out: HiddenSageMakerImage = {}  # type: ignore[typeddict-item]
    if "SageMakerImageName" in data:
        import aws_sdk_sagemaker.types.sage_maker_image_name

        out["sage_maker_image_name"] = (
            aws_sdk_sagemaker.types.sage_maker_image_name.deserialize_aws_json_1_1(
                data["SageMakerImageName"]
            )
        )
    if "VersionAliases" in data:
        import aws_sdk_sagemaker.types.version_aliases_list

        out["version_aliases"] = (
            aws_sdk_sagemaker.types.version_aliases_list.deserialize_aws_json_1_1(
                data["VersionAliases"]
            )
        )
    return out
