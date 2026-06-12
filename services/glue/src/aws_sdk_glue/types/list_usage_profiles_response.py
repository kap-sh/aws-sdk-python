"""Generated from Smithy shape ``com.amazonaws.glue#ListUsageProfilesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.orchestration_token
    import aws_sdk_glue.types.usage_profile_definition_list


class ListUsageProfilesResponse(TypedDict):
    profiles: NotRequired[
        "aws_sdk_glue.types.usage_profile_definition_list.UsageProfileDefinitionList"
    ]
    """<p>A list of usage profile (<code>UsageProfileDefinition</code>) objects.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.orchestration_token.OrchestrationToken"]
    """<p>A continuation token, present if the current list segment is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUsageProfilesResponse) -> dict:
    out: dict = {}
    if "profiles" in value:
        import aws_sdk_glue.types.usage_profile_definition_list

        out["Profiles"] = (
            aws_sdk_glue.types.usage_profile_definition_list.serialize_aws_json_1_1(
                value["profiles"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUsageProfilesResponse:
    out: ListUsageProfilesResponse = {}  # type: ignore[typeddict-item]
    if "Profiles" in data:
        import aws_sdk_glue.types.usage_profile_definition_list

        out["profiles"] = (
            aws_sdk_glue.types.usage_profile_definition_list.deserialize_aws_json_1_1(
                data["Profiles"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
