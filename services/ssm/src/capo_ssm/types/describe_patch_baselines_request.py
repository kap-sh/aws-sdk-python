"""Generated from Smithy shape ``com.amazonaws.ssm#DescribePatchBaselinesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.next_token
    import capo_ssm.types.patch_baseline_max_results
    import capo_ssm.types.patch_orchestrator_filter_list


class DescribePatchBaselinesRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_ssm.types.patch_orchestrator_filter_list.PatchOrchestratorFilterList"
    ]
    """<p>Each element in the array is a structure containing a key-value pair.</p> <p>Supported keys for <code>DescribePatchBaselines</code> include the following:</p> <ul> <li> <p> <b> <code>NAME_PREFIX</code> </b> </p> <p>Sample values: <code>AWS-</code> | <code>My-</code> </p> </li> <li> <p> <b> <code>OWNER</code> </b> </p> <p>Sample values: <code>AWS</code> | <code>Self</code> </p> </li> <li> <p> <b> <code>OPERATING_SYSTEM</code> </b> </p> <p>Sample values: <code>AMAZON_LINUX</code> | <code>SUSE</code> | <code>WINDOWS</code> </p> </li> </ul>"""
    max_results: NotRequired[
        "capo_ssm.types.patch_baseline_max_results.PatchBaselineMaxResults"
    ]
    """<p>The maximum number of patch baselines to return (per page).</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePatchBaselinesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_ssm.types.patch_orchestrator_filter_list

        out["Filters"] = (
            capo_ssm.types.patch_orchestrator_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePatchBaselinesRequest:
    out: DescribePatchBaselinesRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import capo_ssm.types.patch_orchestrator_filter_list

        out["filters"] = (
            capo_ssm.types.patch_orchestrator_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
