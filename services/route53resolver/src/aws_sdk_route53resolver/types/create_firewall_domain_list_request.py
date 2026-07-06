"""Generated from Smithy shape ``com.amazonaws.route53resolver#CreateFirewallDomainListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.creator_request_id
    import aws_sdk_route53resolver.types.name
    import aws_sdk_route53resolver.types.tag_list


class CreateFirewallDomainListRequest(TypedDict, closed=True):
    creator_request_id: (
        "aws_sdk_route53resolver.types.creator_request_id.CreatorRequestId"
    )
    """<p>A unique string that identifies the request and that allows you to retry failed requests without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string, for example, a date/time stamp. </p>"""
    name: "aws_sdk_route53resolver.types.name.Name"
    """<p>A name that lets you identify the domain list to manage and use it.</p>"""
    tags: NotRequired["aws_sdk_route53resolver.types.tag_list.TagList"]
    """<p>A list of the tag keys and values that you want to associate with the domain list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFirewallDomainListRequest) -> dict:
    out: dict = {}
    out["CreatorRequestId"] = value["creator_request_id"]
    out["Name"] = value["name"]
    if "tags" in value:
        import aws_sdk_route53resolver.types.tag_list

        out["Tags"] = aws_sdk_route53resolver.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFirewallDomainListRequest:
    out: CreateFirewallDomainListRequest = {}  # type: ignore[typeddict-item]
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    else:
        raise DeserializationError(
            "CreateFirewallDomainListRequest.creator_request_id required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateFirewallDomainListRequest.name required")
    if "Tags" in data:
        import aws_sdk_route53resolver.types.tag_list

        out["tags"] = aws_sdk_route53resolver.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
