"""Generated from Smithy shape ``com.amazonaws.route53domains#DeleteTagsForDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53_domains.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.domain_name
    import aws_sdk_route_53_domains.types.tag_key_list


class DeleteTagsForDomainRequest(TypedDict, closed=True):
    domain_name: "aws_sdk_route_53_domains.types.domain_name.DomainName"
    """<p>The domain for which you want to delete one or more tags.</p>"""
    tags_to_delete: "aws_sdk_route_53_domains.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTagsForDomainRequest) -> dict:
    out: dict = {}
    out["DomainName"] = value["domain_name"]
    import aws_sdk_route_53_domains.types.tag_key_list

    out["TagsToDelete"] = (
        aws_sdk_route_53_domains.types.tag_key_list.serialize_aws_json_1_1(
            value["tags_to_delete"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTagsForDomainRequest:
    out: DeleteTagsForDomainRequest = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    else:
        raise DeserializationError("DeleteTagsForDomainRequest.domain_name required")
    if "TagsToDelete" in data:
        import aws_sdk_route_53_domains.types.tag_key_list

        out["tags_to_delete"] = (
            aws_sdk_route_53_domains.types.tag_key_list.deserialize_aws_json_1_1(
                data["TagsToDelete"]
            )
        )
    else:
        raise DeserializationError("DeleteTagsForDomainRequest.tags_to_delete required")
    return out
