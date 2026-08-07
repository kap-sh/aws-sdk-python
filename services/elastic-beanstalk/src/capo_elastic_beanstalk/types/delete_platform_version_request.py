"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DeletePlatformVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.platform_arn


class DeletePlatformVersionRequest(TypedDict, closed=True):
    platform_arn: NotRequired["capo_elastic_beanstalk.types.platform_arn.PlatformArn"]
    """<p>The ARN of the version of the custom platform.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeletePlatformVersionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "platform_arn" in value:
        pairs.append((f"{key_prefix}PlatformArn", str(value["platform_arn"])))


def deserialize_query(el: Element) -> DeletePlatformVersionRequest:
    out: DeletePlatformVersionRequest = {}  # type: ignore[typeddict-item]
    child_platform_arn = el.find("PlatformArn")
    if child_platform_arn is not None:
        out["platform_arn"] = str(child_platform_arn.text or "")
    return out
