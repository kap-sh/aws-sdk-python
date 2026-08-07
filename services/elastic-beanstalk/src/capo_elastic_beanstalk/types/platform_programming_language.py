"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#PlatformProgrammingLanguage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.string


class PlatformProgrammingLanguage(TypedDict, closed=True):
    name: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The name of the programming language.</p>"""
    version: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The version of the programming language.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PlatformProgrammingLanguage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "version" in value:
        pairs.append((f"{key_prefix}Version", str(value["version"])))


def deserialize_query(el: Element) -> PlatformProgrammingLanguage:
    out: PlatformProgrammingLanguage = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_version = el.find("Version")
    if child_version is not None:
        out["version"] = str(child_version.text or "")
    return out
