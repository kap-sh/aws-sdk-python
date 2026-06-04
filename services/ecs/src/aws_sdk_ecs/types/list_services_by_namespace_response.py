"""Generated from Smithy shape ``com.amazonaws.ecs#ListServicesByNamespaceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.string_list


class ListServicesByNamespaceResponse(TypedDict):
    service_arns: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The list of full ARN entries for each service that's associated with the specified namespace.</p>"""
    next_token: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future <code>ListServicesByNamespace</code> request. When the results of a <code>ListServicesByNamespace</code> request exceed <code>maxResults</code>, this value can be used to retrieve the next page of results. When there are no more results to return, this value is <code>null</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServicesByNamespaceResponse) -> dict:
    out: dict = {}
    if "service_arns" in value:
        import aws_sdk_ecs.types.string_list

        out["serviceArns"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
            value["service_arns"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServicesByNamespaceResponse:
    out: ListServicesByNamespaceResponse = {}  # type: ignore[typeddict-item]
    if "serviceArns" in data:
        import aws_sdk_ecs.types.string_list

        out["service_arns"] = aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
            data["serviceArns"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
