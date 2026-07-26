"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateSpaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.domain_id
    import capo_sagemaker.types.non_empty_string64
    import capo_sagemaker.types.ownership_settings
    import capo_sagemaker.types.space_name
    import capo_sagemaker.types.space_settings
    import capo_sagemaker.types.space_sharing_settings
    import capo_sagemaker.types.tag_list


class CreateSpaceRequest(TypedDict, closed=True):
    domain_id: NotRequired["capo_sagemaker.types.domain_id.DomainId"]
    """<p>The ID of the associated domain.</p>"""
    space_name: NotRequired["capo_sagemaker.types.space_name.SpaceName"]
    """<p>The name of the space.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>Tags to associated with the space. Each tag consists of a key and an optional value. Tag keys must be unique for each resource. Tags are searchable using the <code>Search</code> API.</p>"""
    space_settings: NotRequired["capo_sagemaker.types.space_settings.SpaceSettings"]
    """<p>A collection of space settings.</p>"""
    ownership_settings: NotRequired[
        "capo_sagemaker.types.ownership_settings.OwnershipSettings"
    ]
    """<p>A collection of ownership settings.</p>"""
    space_sharing_settings: NotRequired[
        "capo_sagemaker.types.space_sharing_settings.SpaceSharingSettings"
    ]
    """<p>A collection of space sharing settings.</p>"""
    space_display_name: NotRequired[
        "capo_sagemaker.types.non_empty_string64.NonEmptyString64"
    ]
    """<p>The name of the space that appears in the SageMaker Studio UI.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSpaceRequest) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "space_name" in value:
        out["SpaceName"] = value["space_name"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "space_settings" in value:
        import capo_sagemaker.types.space_settings

        out["SpaceSettings"] = (
            capo_sagemaker.types.space_settings.serialize_aws_json_1_1(
                value["space_settings"]
            )
        )
    if "ownership_settings" in value:
        import capo_sagemaker.types.ownership_settings

        out["OwnershipSettings"] = (
            capo_sagemaker.types.ownership_settings.serialize_aws_json_1_1(
                value["ownership_settings"]
            )
        )
    if "space_sharing_settings" in value:
        import capo_sagemaker.types.space_sharing_settings

        out["SpaceSharingSettings"] = (
            capo_sagemaker.types.space_sharing_settings.serialize_aws_json_1_1(
                value["space_sharing_settings"]
            )
        )
    if "space_display_name" in value:
        out["SpaceDisplayName"] = value["space_display_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSpaceRequest:
    out: CreateSpaceRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "SpaceName" in data:
        out["space_name"] = data["SpaceName"]
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "SpaceSettings" in data:
        import capo_sagemaker.types.space_settings

        out["space_settings"] = (
            capo_sagemaker.types.space_settings.deserialize_aws_json_1_1(
                data["SpaceSettings"]
            )
        )
    if "OwnershipSettings" in data:
        import capo_sagemaker.types.ownership_settings

        out["ownership_settings"] = (
            capo_sagemaker.types.ownership_settings.deserialize_aws_json_1_1(
                data["OwnershipSettings"]
            )
        )
    if "SpaceSharingSettings" in data:
        import capo_sagemaker.types.space_sharing_settings

        out["space_sharing_settings"] = (
            capo_sagemaker.types.space_sharing_settings.deserialize_aws_json_1_1(
                data["SpaceSharingSettings"]
            )
        )
    if "SpaceDisplayName" in data:
        out["space_display_name"] = data["SpaceDisplayName"]
    return out
