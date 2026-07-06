"""Generated from Smithy shape ``com.amazonaws.ecs#ListTaskDefinitionFamiliesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.task_definition_family_status


class ListTaskDefinitionFamiliesRequest(TypedDict, closed=True):
    family_prefix: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>familyPrefix</code> is a string that's used to filter the results of <code>ListTaskDefinitionFamilies</code>. If you specify a <code>familyPrefix</code>, only task definition family names that begin with the <code>familyPrefix</code> string are returned.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.task_definition_family_status.TaskDefinitionFamilyStatus"
    ]
    """<p>The task definition family status to filter the <code>ListTaskDefinitionFamilies</code> results with. By default, both <code>ACTIVE</code> and <code>INACTIVE</code> task definition families are listed. If this parameter is set to <code>ACTIVE</code>, only task definition families that have an <code>ACTIVE</code> task definition revision are returned. If this parameter is set to <code>INACTIVE</code>, only task definition families that do not have any <code>ACTIVE</code> task definition revisions are returned. If you paginate the resulting output, be sure to keep the <code>status</code> value constant in each subsequent request.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a <code>ListTaskDefinitionFamilies</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it is possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    max_results: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of task definition family results that <code>ListTaskDefinitionFamilies</code> returned in paginated output. When this parameter is used, <code>ListTaskDefinitions</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListTaskDefinitionFamilies</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListTaskDefinitionFamilies</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTaskDefinitionFamiliesRequest) -> dict:
    out: dict = {}
    if "family_prefix" in value:
        out["familyPrefix"] = value["family_prefix"]
    if "status" in value:
        import aws_sdk_ecs.types.task_definition_family_status

        out["status"] = (
            aws_sdk_ecs.types.task_definition_family_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTaskDefinitionFamiliesRequest:
    out: ListTaskDefinitionFamiliesRequest = {}  # type: ignore[typeddict-item]
    if "familyPrefix" in data:
        out["family_prefix"] = data["familyPrefix"]
    if "status" in data:
        import aws_sdk_ecs.types.task_definition_family_status

        out["status"] = (
            aws_sdk_ecs.types.task_definition_family_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
