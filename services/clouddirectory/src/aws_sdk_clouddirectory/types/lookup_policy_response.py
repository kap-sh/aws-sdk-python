"""Generated from Smithy shape ``com.amazonaws.clouddirectory#LookupPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.next_token
    import aws_sdk_clouddirectory.types.policy_to_path_list


class LookupPolicyResponse(TypedDict, closed=True):
    policy_to_path_list: NotRequired[
        "aws_sdk_clouddirectory.types.policy_to_path_list.PolicyToPathList"
    ]
    r"""<p>Provides list of path to policies. Policies contain <code>PolicyId</code>, <code>ObjectIdentifier</code>, and <code>PolicyType</code>. For more information, see <a href=\"https://docs.aws.amazon.com/clouddirectory/latest/developerguide/key_concepts_directory.html#key_concepts_policies\">Policies</a>.</p>"""
    next_token: NotRequired["aws_sdk_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LookupPolicyResponse) -> dict:
    out: dict = {}
    if "policy_to_path_list" in value:
        import aws_sdk_clouddirectory.types.policy_to_path_list

        out["PolicyToPathList"] = (
            aws_sdk_clouddirectory.types.policy_to_path_list.serialize_json(
                value["policy_to_path_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> LookupPolicyResponse:
    out: LookupPolicyResponse = {}  # type: ignore[typeddict-item]
    if "PolicyToPathList" in data:
        import aws_sdk_clouddirectory.types.policy_to_path_list

        out["policy_to_path_list"] = (
            aws_sdk_clouddirectory.types.policy_to_path_list.deserialize_json(
                data["PolicyToPathList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
