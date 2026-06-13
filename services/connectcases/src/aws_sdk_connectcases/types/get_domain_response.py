"""Generated from Smithy shape ``com.amazonaws.connectcases#GetDomainResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.created_time
    import aws_sdk_connectcases.types.domain_arn
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.domain_name
    import aws_sdk_connectcases.types.domain_status
    import aws_sdk_connectcases.types.tags


class GetDomainResponse(TypedDict):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    domain_arn: "aws_sdk_connectcases.types.domain_arn.DomainArn"
    """<p>The Amazon Resource Name (ARN) for the Cases domain.</p>"""
    name: "aws_sdk_connectcases.types.domain_name.DomainName"
    """<p>The name of the Cases domain.</p>"""
    created_time: "aws_sdk_connectcases.types.created_time.CreatedTime"
    """<p>The timestamp when the Cases domain was created.</p>"""
    domain_status: "aws_sdk_connectcases.types.domain_status.DomainStatus"
    """<p>The status of the Cases domain.</p>"""
    tags: NotRequired["aws_sdk_connectcases.types.tags.Tags"]
    """<p>A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainResponse) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["domainArn"] = value["domain_arn"]
    out["name"] = value["name"]
    import aws_sdk_connectcases.types.created_time

    out["createdTime"] = aws_sdk_connectcases.types.created_time.serialize_json(
        value["created_time"]
    )
    out["domainStatus"] = value["domain_status"]
    if "tags" in value:
        import aws_sdk_connectcases.types.tags

        out["tags"] = aws_sdk_connectcases.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetDomainResponse:
    out: GetDomainResponse = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError("GetDomainResponse.domain_id required")
    if "domainArn" in data:
        out["domain_arn"] = data["domainArn"]
    else:
        raise DeserializationError("GetDomainResponse.domain_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetDomainResponse.name required")
    if "createdTime" in data:
        import aws_sdk_connectcases.types.created_time

        out["created_time"] = aws_sdk_connectcases.types.created_time.deserialize_json(
            data["createdTime"]
        )
    else:
        raise DeserializationError("GetDomainResponse.created_time required")
    if "domainStatus" in data:
        out["domain_status"] = data["domainStatus"]
    else:
        raise DeserializationError("GetDomainResponse.domain_status required")
    if "tags" in data:
        import aws_sdk_connectcases.types.tags

        out["tags"] = aws_sdk_connectcases.types.tags.deserialize_json(data["tags"])
    return out
