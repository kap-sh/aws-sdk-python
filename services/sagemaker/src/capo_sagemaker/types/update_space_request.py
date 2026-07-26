"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateSpaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.domain_id
    import capo_sagemaker.types.non_empty_string64
    import capo_sagemaker.types.space_name
    import capo_sagemaker.types.space_settings


class UpdateSpaceRequest(TypedDict, closed=True):
    domain_id: NotRequired["capo_sagemaker.types.domain_id.DomainId"]
    """<p>The ID of the associated domain.</p>"""
    space_name: NotRequired["capo_sagemaker.types.space_name.SpaceName"]
    """<p>The name of the space.</p>"""
    space_settings: NotRequired["capo_sagemaker.types.space_settings.SpaceSettings"]
    """<p>A collection of space settings.</p>"""
    space_display_name: NotRequired[
        "capo_sagemaker.types.non_empty_string64.NonEmptyString64"
    ]
    """<p>The name of the space that appears in the Amazon SageMaker Studio UI.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSpaceRequest) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "space_name" in value:
        out["SpaceName"] = value["space_name"]
    if "space_settings" in value:
        import capo_sagemaker.types.space_settings

        out["SpaceSettings"] = (
            capo_sagemaker.types.space_settings.serialize_aws_json_1_1(
                value["space_settings"]
            )
        )
    if "space_display_name" in value:
        out["SpaceDisplayName"] = value["space_display_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSpaceRequest:
    out: UpdateSpaceRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "SpaceName" in data:
        out["space_name"] = data["SpaceName"]
    if "SpaceSettings" in data:
        import capo_sagemaker.types.space_settings

        out["space_settings"] = (
            capo_sagemaker.types.space_settings.deserialize_aws_json_1_1(
                data["SpaceSettings"]
            )
        )
    if "SpaceDisplayName" in data:
        out["space_display_name"] = data["SpaceDisplayName"]
    return out
