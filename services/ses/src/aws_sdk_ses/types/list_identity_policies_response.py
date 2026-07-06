"""Generated from Smithy shape ``com.amazonaws.ses#ListIdentityPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.policy_name_list


class ListIdentityPoliciesResponse(TypedDict, closed=True):
    policy_names: "aws_sdk_ses.types.policy_name_list.PolicyNameList"
    """<p>A list of names of policies that apply to the specified identity.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListIdentityPoliciesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_ses.types.policy_name_list

    aws_sdk_ses.types.policy_name_list.serialize_query(
        value["policy_names"], pairs, f"{prefix}.PolicyNames"
    )


def deserialize_query(el: Element) -> ListIdentityPoliciesResponse:
    out: ListIdentityPoliciesResponse = {}  # type: ignore[typeddict-item]
    child_policy_names = el.find("PolicyNames")
    if child_policy_names is not None:
        import aws_sdk_ses.types.policy_name_list

        out["policy_names"] = aws_sdk_ses.types.policy_name_list.deserialize_query(
            child_policy_names
        )
    else:
        raise DeserializationError("ListIdentityPoliciesResponse.policy_names required")
    return out
