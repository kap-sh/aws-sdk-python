"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ListComponentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.application_component_list
    import aws_sdk_application_insights.types.pagination_token


class ListComponentsResponse(TypedDict, closed=True):
    application_component_list: NotRequired[
        "aws_sdk_application_insights.types.application_component_list.ApplicationComponentList"
    ]
    """<p>The list of application components.</p>"""
    next_token: NotRequired[
        "aws_sdk_application_insights.types.pagination_token.PaginationToken"
    ]
    """<p>The token to request the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListComponentsResponse) -> dict:
    out: dict = {}
    if "application_component_list" in value:
        import aws_sdk_application_insights.types.application_component_list

        out["ApplicationComponentList"] = (
            aws_sdk_application_insights.types.application_component_list.serialize_aws_json_1_1(
                value["application_component_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListComponentsResponse:
    out: ListComponentsResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationComponentList" in data:
        import aws_sdk_application_insights.types.application_component_list

        out["application_component_list"] = (
            aws_sdk_application_insights.types.application_component_list.deserialize_aws_json_1_1(
                data["ApplicationComponentList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
