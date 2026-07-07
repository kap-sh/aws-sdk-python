"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAliasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.image_name
    import aws_sdk_sagemaker.types.image_version_number
    import aws_sdk_sagemaker.types.max_results
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.sage_maker_image_version_alias


class ListAliasesRequest(TypedDict, closed=True):
    image_name: NotRequired["aws_sdk_sagemaker.types.image_name.ImageName"]
    """<p>The name of the image.</p>"""
    alias: NotRequired[
        "aws_sdk_sagemaker.types.sage_maker_image_version_alias.SageMakerImageVersionAlias"
    ]
    """<p>The alias of the image version.</p>"""
    version: NotRequired[
        "aws_sdk_sagemaker.types.image_version_number.ImageVersionNumber"
    ]
    """<p>The version of the image. If image version is not specified, the aliases of all versions of the image are listed.</p>"""
    max_results: NotRequired["aws_sdk_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of aliases to return.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the previous call to <code>ListAliases</code> didn't return the full set of aliases, the call returns a token for retrieving the next set of aliases.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAliasesRequest) -> dict:
    out: dict = {}
    if "image_name" in value:
        out["ImageName"] = value["image_name"]
    if "alias" in value:
        out["Alias"] = value["alias"]
    if "version" in value:
        out["Version"] = value["version"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAliasesRequest:
    out: ListAliasesRequest = {}  # type: ignore[typeddict-item]
    if "ImageName" in data:
        out["image_name"] = data["ImageName"]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
