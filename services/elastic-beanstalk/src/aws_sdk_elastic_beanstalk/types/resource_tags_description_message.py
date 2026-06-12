"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ResourceTagsDescriptionMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.resource_arn
    import aws_sdk_elastic_beanstalk.types.tag_list


class ResourceTagsDescriptionMessage(TypedDict):
    resource_arn: NotRequired[
        "aws_sdk_elastic_beanstalk.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the resource for which a tag list was requested.</p>"""
    resource_tags: NotRequired["aws_sdk_elastic_beanstalk.types.tag_list.TagList"]
    """<p>A list of tag key-value pairs.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceTagsDescriptionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_arn" in value:
        pairs.append((f"{prefix}.ResourceArn", str(value["resource_arn"])))
    if "resource_tags" in value:
        import aws_sdk_elastic_beanstalk.types.tag_list

        aws_sdk_elastic_beanstalk.types.tag_list.serialize_query(
            value["resource_tags"], pairs, f"{prefix}.ResourceTags"
        )


def deserialize_query(el: Element) -> ResourceTagsDescriptionMessage:
    out: ResourceTagsDescriptionMessage = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    child_resource_tags = el.find("ResourceTags")
    if child_resource_tags is not None:
        import aws_sdk_elastic_beanstalk.types.tag_list

        out["resource_tags"] = (
            aws_sdk_elastic_beanstalk.types.tag_list.deserialize_query(
                child_resource_tags
            )
        )
    return out
