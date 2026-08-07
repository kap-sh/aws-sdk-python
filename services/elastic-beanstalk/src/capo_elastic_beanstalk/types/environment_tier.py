"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentTier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.string


class EnvironmentTier(TypedDict, closed=True):
    name: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The name of this environment tier.</p> <p>Valid values:</p> <ul> <li> <p>For <i>Web server tier</i> – <code>WebServer</code> </p> </li> <li> <p>For <i>Worker tier</i> – <code>Worker</code> </p> </li> </ul>"""
    type: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The type of this environment tier.</p> <p>Valid values:</p> <ul> <li> <p>For <i>Web server tier</i> – <code>Standard</code> </p> </li> <li> <p>For <i>Worker tier</i> – <code>SQS/HTTP</code> </p> </li> </ul>"""
    version: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The version of this environment tier. When you don't set a value to it, Elastic Beanstalk uses the latest compatible worker tier version.</p> <note> <p>This member is deprecated. Any specific version that you set may become out of date. We recommend leaving it unspecified.</p> </note>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EnvironmentTier, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "type" in value:
        pairs.append((f"{key_prefix}Type", str(value["type"])))
    if "version" in value:
        pairs.append((f"{key_prefix}Version", str(value["version"])))


def deserialize_query(el: Element) -> EnvironmentTier:
    out: EnvironmentTier = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        out["type"] = str(child_type.text or "")
    child_version = el.find("Version")
    if child_version is not None:
        out["version"] = str(child_version.text or "")
    return out
