"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListProfilesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.max_results
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.profile_name_prefix
    import aws_sdk_wellarchitected.types.profile_owner_type


class ListProfilesInput(TypedDict):
    profile_name_prefix: NotRequired[
        "aws_sdk_wellarchitected.types.profile_name_prefix.ProfileNamePrefix"
    ]
    """<p>An optional string added to the beginning of each profile name returned in the results.</p>"""
    profile_owner_type: NotRequired[
        "aws_sdk_wellarchitected.types.profile_owner_type.ProfileOwnerType"
    ]
    """<p>Profile owner type.</p>"""
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired["aws_sdk_wellarchitected.types.max_results.MaxResults"]


# --- restJson1 ser/de ---
def serialize_json(value: ListProfilesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListProfilesInput:
    out: ListProfilesInput = {}  # type: ignore[typeddict-item]
    return out
