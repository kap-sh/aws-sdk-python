"""Generated from Smithy shape ``com.amazonaws.workmail#GetDefaultRetentionPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workmail.types.folder_configurations
    import aws_sdk_workmail.types.short_string
    import aws_sdk_workmail.types.string


class GetDefaultRetentionPolicyResponse(TypedDict, closed=True):
    id: NotRequired["aws_sdk_workmail.types.short_string.ShortString"]
    """<p>The retention policy ID.</p>"""
    name: NotRequired["aws_sdk_workmail.types.short_string.ShortString"]
    """<p>The retention policy name.</p>"""
    description: NotRequired["aws_sdk_workmail.types.string.String"]
    """<p>The retention policy description.</p>"""
    folder_configurations: NotRequired[
        "aws_sdk_workmail.types.folder_configurations.FolderConfigurations"
    ]
    """<p>The retention policy folder configurations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDefaultRetentionPolicyResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "folder_configurations" in value:
        import aws_sdk_workmail.types.folder_configurations

        out["FolderConfigurations"] = (
            aws_sdk_workmail.types.folder_configurations.serialize_aws_json_1_1(
                value["folder_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDefaultRetentionPolicyResponse:
    out: GetDefaultRetentionPolicyResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "FolderConfigurations" in data:
        import aws_sdk_workmail.types.folder_configurations

        out["folder_configurations"] = (
            aws_sdk_workmail.types.folder_configurations.deserialize_aws_json_1_1(
                data["FolderConfigurations"]
            )
        )
    return out
