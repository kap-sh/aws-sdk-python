"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentLink``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.string


class EnvironmentLink(TypedDict, closed=True):
    link_name: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The name of the link.</p>"""
    environment_name: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The name of the linked environment (the dependency).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EnvironmentLink, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "link_name" in value:
        pairs.append((f"{key_prefix}LinkName", str(value["link_name"])))
    if "environment_name" in value:
        pairs.append((f"{key_prefix}EnvironmentName", str(value["environment_name"])))


def deserialize_query(el: Element) -> EnvironmentLink:
    out: EnvironmentLink = {}  # type: ignore[typeddict-item]
    child_link_name = el.find("LinkName")
    if child_link_name is not None:
        out["link_name"] = str(child_link_name.text or "")
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    return out
