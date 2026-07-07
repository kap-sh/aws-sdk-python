"""Generated from Smithy shape ``com.amazonaws.fms#AppsListDataSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.apps_list
    import aws_sdk_fms.types.list_id
    import aws_sdk_fms.types.resource_arn
    import aws_sdk_fms.types.resource_name


class AppsListDataSummary(TypedDict, closed=True):
    list_arn: NotRequired["aws_sdk_fms.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the applications list.</p>"""
    list_id: NotRequired["aws_sdk_fms.types.list_id.ListId"]
    """<p>The ID of the applications list.</p>"""
    list_name: NotRequired["aws_sdk_fms.types.resource_name.ResourceName"]
    """<p>The name of the applications list.</p>"""
    apps_list: NotRequired["aws_sdk_fms.types.apps_list.AppsList"]
    """<p>An array of <code>App</code> objects in the Firewall Manager applications list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AppsListDataSummary) -> dict:
    out: dict = {}
    if "list_arn" in value:
        out["ListArn"] = value["list_arn"]
    if "list_id" in value:
        out["ListId"] = value["list_id"]
    if "list_name" in value:
        out["ListName"] = value["list_name"]
    if "apps_list" in value:
        import aws_sdk_fms.types.apps_list

        out["AppsList"] = aws_sdk_fms.types.apps_list.serialize_aws_json_1_1(
            value["apps_list"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AppsListDataSummary:
    out: AppsListDataSummary = {}  # type: ignore[typeddict-item]
    if "ListArn" in data:
        out["list_arn"] = data["ListArn"]
    if "ListId" in data:
        out["list_id"] = data["ListId"]
    if "ListName" in data:
        out["list_name"] = data["ListName"]
    if "AppsList" in data:
        import aws_sdk_fms.types.apps_list

        out["apps_list"] = aws_sdk_fms.types.apps_list.deserialize_aws_json_1_1(
            data["AppsList"]
        )
    return out
