"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ListTagsForResourceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.resource_arn


class ListTagsForResourceMessage(TypedDict, closed=True):
    resource_arn: "aws_sdk_elastic_beanstalk.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resouce for which a tag list is requested.</p> <p>Must be the ARN of an Elastic Beanstalk resource.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListTagsForResourceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.ResourceArn", str(value["resource_arn"])))


def deserialize_query(el: Element) -> ListTagsForResourceMessage:
    out: ListTagsForResourceMessage = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    else:
        raise DeserializationError("ListTagsForResourceMessage.resource_arn required")
    return out
