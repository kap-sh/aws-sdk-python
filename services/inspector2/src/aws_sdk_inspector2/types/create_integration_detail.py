"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateIntegrationDetail``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.create_git_lab_self_managed_integration_detail


class _CreateIntegrationDetail_gitlabSelfManaged(TypedDict, closed=True):
    gitlabSelfManaged: "aws_sdk_inspector2.types.create_git_lab_self_managed_integration_detail.CreateGitLabSelfManagedIntegrationDetail"


CreateIntegrationDetail: TypeAlias = _CreateIntegrationDetail_gitlabSelfManaged


# --- restJson1 ser/de ---
def serialize_json(value: CreateIntegrationDetail) -> dict:
    if "gitlabSelfManaged" in value:
        import aws_sdk_inspector2.types.create_git_lab_self_managed_integration_detail

        return {
            "gitlabSelfManaged": aws_sdk_inspector2.types.create_git_lab_self_managed_integration_detail.serialize_json(
                value["gitlabSelfManaged"]
            )
        }
    else:
        raise SerializationError("CreateIntegrationDetail: no variant present")


def deserialize_json(data: dict) -> CreateIntegrationDetail:
    if "gitlabSelfManaged" in data:
        import aws_sdk_inspector2.types.create_git_lab_self_managed_integration_detail

        return {
            "gitlabSelfManaged": aws_sdk_inspector2.types.create_git_lab_self_managed_integration_detail.deserialize_json(
                data["gitlabSelfManaged"]
            )
        }
    else:
        raise DeserializationError("CreateIntegrationDetail: no recognized variant key")
