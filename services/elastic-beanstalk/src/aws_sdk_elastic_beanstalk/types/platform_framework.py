"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#PlatformFramework``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.string


class PlatformFramework(TypedDict, closed=True):
    name: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    """<p>The name of the framework.</p>"""
    version: NotRequired["aws_sdk_elastic_beanstalk.types.string.String"]
    """<p>The version of the framework.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PlatformFramework, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "version" in value:
        pairs.append((f"{prefix}.Version", str(value["version"])))


def deserialize_query(el: Element) -> PlatformFramework:
    out: PlatformFramework = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_version = el.find("Version")
    if child_version is not None:
        out["version"] = str(child_version.text or "")
    return out
