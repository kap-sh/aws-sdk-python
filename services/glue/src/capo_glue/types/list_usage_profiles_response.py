"""Generated from Smithy shape ``com.amazonaws.glue#ListUsageProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.orchestration_token
    import capo_glue.types.usage_profile_definition_list


class ListUsageProfilesResponse(TypedDict, closed=True):
    profiles: NotRequired[
        "capo_glue.types.usage_profile_definition_list.UsageProfileDefinitionList"
    ]
    """<p>A list of usage profile (<code>UsageProfileDefinition</code>) objects.</p>"""
    next_token: NotRequired["capo_glue.types.orchestration_token.OrchestrationToken"]
    """<p>A continuation token, present if the current list segment is not the last.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUsageProfilesResponse) -> dict:
    out: dict = {}
    if "profiles" in value:
        import capo_glue.types.usage_profile_definition_list

        out["Profiles"] = (
            capo_glue.types.usage_profile_definition_list.serialize_aws_json_1_1(
                value["profiles"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUsageProfilesResponse:
    out: ListUsageProfilesResponse = {}  # type: ignore[typeddict-item]
    if "Profiles" in data:
        import capo_glue.types.usage_profile_definition_list

        out["profiles"] = (
            capo_glue.types.usage_profile_definition_list.deserialize_aws_json_1_1(
                data["Profiles"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
