"""Generated from Smithy shape ``com.amazonaws.batch#DescribeSchedulingPoliciesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.scheduling_policy_detail_list


class DescribeSchedulingPoliciesResponse(TypedDict):
    scheduling_policies: NotRequired[
        "aws_sdk_batch.types.scheduling_policy_detail_list.SchedulingPolicyDetailList"
    ]
    """<p>The list of scheduling policies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSchedulingPoliciesResponse) -> dict:
    out: dict = {}
    if "scheduling_policies" in value:
        import aws_sdk_batch.types.scheduling_policy_detail_list

        out["schedulingPolicies"] = (
            aws_sdk_batch.types.scheduling_policy_detail_list.serialize_json(
                value["scheduling_policies"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeSchedulingPoliciesResponse:
    out: DescribeSchedulingPoliciesResponse = {}  # type: ignore[typeddict-item]
    if "schedulingPolicies" in data:
        import aws_sdk_batch.types.scheduling_policy_detail_list

        out["scheduling_policies"] = (
            aws_sdk_batch.types.scheduling_policy_detail_list.deserialize_json(
                data["schedulingPolicies"]
            )
        )
    return out
