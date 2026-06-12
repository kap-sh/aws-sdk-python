"""Generated from Smithy shape ``com.amazonaws.servicediscovery#CreateHttpNamespaceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.namespace_name_http
    import aws_sdk_servicediscovery.types.resource_description
    import aws_sdk_servicediscovery.types.resource_id
    import aws_sdk_servicediscovery.types.tag_list


class CreateHttpNamespaceRequest(TypedDict):
    name: "aws_sdk_servicediscovery.types.namespace_name_http.NamespaceNameHttp"
    """<p>The name that you want to assign to this namespace.</p>"""
    creator_request_id: NotRequired[
        "aws_sdk_servicediscovery.types.resource_id.ResourceId"
    ]
    """<p>A unique string that identifies the request and that allows failed <code>CreateHttpNamespace</code> requests to be retried without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string (for example, a date/time stamp).</p>"""
    description: NotRequired[
        "aws_sdk_servicediscovery.types.resource_description.ResourceDescription"
    ]
    """<p>A description for the namespace.</p>"""
    tags: NotRequired["aws_sdk_servicediscovery.types.tag_list.TagList"]
    """<p>The tags to add to the namespace. Each tag consists of a key and an optional value that you define. Tags keys can be up to 128 characters in length, and tag values can be up to 256 characters in length.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHttpNamespaceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_servicediscovery.types.tag_list

        out["Tags"] = aws_sdk_servicediscovery.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHttpNamespaceRequest:
    out: CreateHttpNamespaceRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateHttpNamespaceRequest.name required")
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_servicediscovery.types.tag_list

        out["tags"] = aws_sdk_servicediscovery.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
