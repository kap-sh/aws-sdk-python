"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAliasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sage_maker_image_version_aliases


class ListAliasesResponse(TypedDict, closed=True):
    sage_maker_image_version_aliases: NotRequired[
        "aws_sdk_sagemaker.types.sage_maker_image_version_aliases.SageMakerImageVersionAliases"
    ]
    """<p>A list of SageMaker AI image version aliases.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>A token for getting the next set of aliases, if more aliases exist.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAliasesResponse) -> dict:
    out: dict = {}
    if "sage_maker_image_version_aliases" in value:
        import aws_sdk_sagemaker.types.sage_maker_image_version_aliases

        out["SageMakerImageVersionAliases"] = (
            aws_sdk_sagemaker.types.sage_maker_image_version_aliases.serialize_aws_json_1_1(
                value["sage_maker_image_version_aliases"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAliasesResponse:
    out: ListAliasesResponse = {}  # type: ignore[typeddict-item]
    if "SageMakerImageVersionAliases" in data:
        import aws_sdk_sagemaker.types.sage_maker_image_version_aliases

        out["sage_maker_image_version_aliases"] = (
            aws_sdk_sagemaker.types.sage_maker_image_version_aliases.deserialize_aws_json_1_1(
                data["SageMakerImageVersionAliases"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
