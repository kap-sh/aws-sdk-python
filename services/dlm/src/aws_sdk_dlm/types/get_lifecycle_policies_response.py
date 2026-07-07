"""Generated from Smithy shape ``com.amazonaws.dlm#GetLifecyclePoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dlm.types.lifecycle_policy_summary_list


class GetLifecyclePoliciesResponse(TypedDict, closed=True):
    policies: NotRequired[
        "aws_sdk_dlm.types.lifecycle_policy_summary_list.LifecyclePolicySummaryList"
    ]
    """<p>Summary information about the lifecycle policies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLifecyclePoliciesResponse) -> dict:
    out: dict = {}
    if "policies" in value:
        import aws_sdk_dlm.types.lifecycle_policy_summary_list

        out["Policies"] = (
            aws_sdk_dlm.types.lifecycle_policy_summary_list.serialize_json(
                value["policies"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetLifecyclePoliciesResponse:
    out: GetLifecyclePoliciesResponse = {}  # type: ignore[typeddict-item]
    if "Policies" in data:
        import aws_sdk_dlm.types.lifecycle_policy_summary_list

        out["policies"] = (
            aws_sdk_dlm.types.lifecycle_policy_summary_list.deserialize_json(
                data["Policies"]
            )
        )
    return out
