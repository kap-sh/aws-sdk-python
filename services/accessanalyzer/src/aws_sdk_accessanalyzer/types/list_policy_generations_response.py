"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListPolicyGenerationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.policy_generation_list
    import aws_sdk_accessanalyzer.types.token


class ListPolicyGenerationsResponse(TypedDict):
    policy_generations: (
        "aws_sdk_accessanalyzer.types.policy_generation_list.PolicyGenerationList"
    )
    """<p>A <code>PolicyGeneration</code> object that contains details about the generated policy.</p>"""
    next_token: NotRequired["aws_sdk_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyGenerationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_accessanalyzer.types.policy_generation_list

    out["policyGenerations"] = (
        aws_sdk_accessanalyzer.types.policy_generation_list.serialize_json(
            value["policy_generations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPolicyGenerationsResponse:
    out: ListPolicyGenerationsResponse = {}  # type: ignore[typeddict-item]
    if "policyGenerations" in data:
        import aws_sdk_accessanalyzer.types.policy_generation_list

        out["policy_generations"] = (
            aws_sdk_accessanalyzer.types.policy_generation_list.deserialize_json(
                data["policyGenerations"]
            )
        )
    else:
        raise DeserializationError(
            "ListPolicyGenerationsResponse.policy_generations required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
