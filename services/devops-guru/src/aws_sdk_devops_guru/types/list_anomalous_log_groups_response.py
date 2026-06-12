"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListAnomalousLogGroupsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.anomalous_log_groups
    import aws_sdk_devops_guru.types.insight_id
    import aws_sdk_devops_guru.types.uuid_next_token


class ListAnomalousLogGroupsResponse(TypedDict):
    insight_id: "aws_sdk_devops_guru.types.insight_id.InsightId"
    """<p> The ID of the insight containing the log groups. </p>"""
    anomalous_log_groups: (
        "aws_sdk_devops_guru.types.anomalous_log_groups.AnomalousLogGroups"
    )
    """<p> The list of Amazon CloudWatch log groups that are related to an insight. </p>"""
    next_token: NotRequired["aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnomalousLogGroupsResponse) -> dict:
    out: dict = {}
    out["InsightId"] = value["insight_id"]
    import aws_sdk_devops_guru.types.anomalous_log_groups

    out["AnomalousLogGroups"] = (
        aws_sdk_devops_guru.types.anomalous_log_groups.serialize_json(
            value["anomalous_log_groups"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAnomalousLogGroupsResponse:
    out: ListAnomalousLogGroupsResponse = {}  # type: ignore[typeddict-item]
    if "InsightId" in data:
        out["insight_id"] = data["InsightId"]
    else:
        raise DeserializationError("ListAnomalousLogGroupsResponse.insight_id required")
    if "AnomalousLogGroups" in data:
        import aws_sdk_devops_guru.types.anomalous_log_groups

        out["anomalous_log_groups"] = (
            aws_sdk_devops_guru.types.anomalous_log_groups.deserialize_json(
                data["AnomalousLogGroups"]
            )
        )
    else:
        raise DeserializationError(
            "ListAnomalousLogGroupsResponse.anomalous_log_groups required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
