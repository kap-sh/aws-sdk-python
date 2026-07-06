"""Generated from Smithy shape ``com.amazonaws.configservice#ListResourceEvaluationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.resource_evaluations
    import aws_sdk_config_service.types.string


class ListResourceEvaluationsResponse(TypedDict, closed=True):
    resource_evaluations: NotRequired[
        "aws_sdk_config_service.types.resource_evaluations.ResourceEvaluations"
    ]
    """<p>Returns a <code>ResourceEvaluations</code> object.</p>"""
    next_token: NotRequired["aws_sdk_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceEvaluationsResponse) -> dict:
    out: dict = {}
    if "resource_evaluations" in value:
        import aws_sdk_config_service.types.resource_evaluations

        out["ResourceEvaluations"] = (
            aws_sdk_config_service.types.resource_evaluations.serialize_aws_json_1_1(
                value["resource_evaluations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceEvaluationsResponse:
    out: ListResourceEvaluationsResponse = {}  # type: ignore[typeddict-item]
    if "ResourceEvaluations" in data:
        import aws_sdk_config_service.types.resource_evaluations

        out["resource_evaluations"] = (
            aws_sdk_config_service.types.resource_evaluations.deserialize_aws_json_1_1(
                data["ResourceEvaluations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
