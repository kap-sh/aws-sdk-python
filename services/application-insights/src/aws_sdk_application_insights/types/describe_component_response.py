"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeComponentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.application_component
    import aws_sdk_application_insights.types.resource_list


class DescribeComponentResponse(TypedDict, closed=True):
    application_component: NotRequired[
        "aws_sdk_application_insights.types.application_component.ApplicationComponent"
    ]
    resource_list: NotRequired[
        "aws_sdk_application_insights.types.resource_list.ResourceList"
    ]
    """<p>The list of resource ARNs that belong to the component.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeComponentResponse) -> dict:
    out: dict = {}
    if "application_component" in value:
        import aws_sdk_application_insights.types.application_component

        out["ApplicationComponent"] = (
            aws_sdk_application_insights.types.application_component.serialize_aws_json_1_1(
                value["application_component"]
            )
        )
    if "resource_list" in value:
        import aws_sdk_application_insights.types.resource_list

        out["ResourceList"] = (
            aws_sdk_application_insights.types.resource_list.serialize_aws_json_1_1(
                value["resource_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeComponentResponse:
    out: DescribeComponentResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationComponent" in data:
        import aws_sdk_application_insights.types.application_component

        out["application_component"] = (
            aws_sdk_application_insights.types.application_component.deserialize_aws_json_1_1(
                data["ApplicationComponent"]
            )
        )
    if "ResourceList" in data:
        import aws_sdk_application_insights.types.resource_list

        out["resource_list"] = (
            aws_sdk_application_insights.types.resource_list.deserialize_aws_json_1_1(
                data["ResourceList"]
            )
        )
    return out
