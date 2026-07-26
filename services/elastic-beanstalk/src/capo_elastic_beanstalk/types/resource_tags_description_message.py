"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ResourceTagsDescriptionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.resource_arn
    import capo_elastic_beanstalk.types.tag_list


class ResourceTagsDescriptionMessage(TypedDict, closed=True):
    resource_arn: NotRequired["capo_elastic_beanstalk.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the resource for which a tag list was requested.</p>"""
    resource_tags: NotRequired["capo_elastic_beanstalk.types.tag_list.TagList"]
    """<p>A list of tag key-value pairs.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceTagsDescriptionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_arn" in value:
        pairs.append((f"{prefix}.ResourceArn", str(value["resource_arn"])))
    if "resource_tags" in value:
        import capo_elastic_beanstalk.types.tag_list

        capo_elastic_beanstalk.types.tag_list.serialize_query(
            value["resource_tags"], pairs, f"{prefix}.ResourceTags"
        )


def deserialize_query(el: Element) -> ResourceTagsDescriptionMessage:
    out: ResourceTagsDescriptionMessage = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    child_resource_tags = el.find("ResourceTags")
    if child_resource_tags is not None:
        import capo_elastic_beanstalk.types.tag_list

        out["resource_tags"] = capo_elastic_beanstalk.types.tag_list.deserialize_query(
            child_resource_tags
        )
    return out
