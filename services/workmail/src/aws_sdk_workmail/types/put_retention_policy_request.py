"""Generated from Smithy shape ``com.amazonaws.workmail#PutRetentionPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.folder_configurations
    import aws_sdk_workmail.types.organization_id
    import aws_sdk_workmail.types.policy_description
    import aws_sdk_workmail.types.short_string


class PutRetentionPolicyRequest(TypedDict):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The organization ID.</p>"""
    id: NotRequired["aws_sdk_workmail.types.short_string.ShortString"]
    """<p>The retention policy ID.</p>"""
    name: "aws_sdk_workmail.types.short_string.ShortString"
    """<p>The retention policy name.</p>"""
    description: NotRequired[
        "aws_sdk_workmail.types.policy_description.PolicyDescription"
    ]
    """<p>The retention policy description.</p>"""
    folder_configurations: (
        "aws_sdk_workmail.types.folder_configurations.FolderConfigurations"
    )
    """<p>The retention policy folder configurations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRetentionPolicyRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    if "id" in value:
        out["Id"] = value["id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_workmail.types.folder_configurations

    out["FolderConfigurations"] = (
        aws_sdk_workmail.types.folder_configurations.serialize_aws_json_1_1(
            value["folder_configurations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRetentionPolicyRequest:
    out: PutRetentionPolicyRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("PutRetentionPolicyRequest.organization_id required")
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("PutRetentionPolicyRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "FolderConfigurations" in data:
        import aws_sdk_workmail.types.folder_configurations

        out["folder_configurations"] = (
            aws_sdk_workmail.types.folder_configurations.deserialize_aws_json_1_1(
                data["FolderConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "PutRetentionPolicyRequest.folder_configurations required"
        )
    return out
