"""Generated from Smithy shape ``com.amazonaws.batch#DescribeServiceEnvironmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.service_environment_detail_list
    import capo_batch.types.string


class DescribeServiceEnvironmentsResponse(TypedDict, closed=True):
    service_environments: NotRequired[
        "capo_batch.types.service_environment_detail_list.ServiceEnvironmentDetailList"
    ]
    """<p>The list of service environments that match the request.</p>"""
    next_token: NotRequired["capo_batch.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>DescribeServiceEnvironments</code> request. When the results of a <code>DescribeServiceEnvironments</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeServiceEnvironmentsResponse) -> dict:
    out: dict = {}
    if "service_environments" in value:
        import capo_batch.types.service_environment_detail_list

        out["serviceEnvironments"] = (
            capo_batch.types.service_environment_detail_list.serialize_json(
                value["service_environments"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeServiceEnvironmentsResponse:
    out: DescribeServiceEnvironmentsResponse = {}  # type: ignore[typeddict-item]
    if "serviceEnvironments" in data:
        import capo_batch.types.service_environment_detail_list

        out["service_environments"] = (
            capo_batch.types.service_environment_detail_list.deserialize_json(
                data["serviceEnvironments"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
