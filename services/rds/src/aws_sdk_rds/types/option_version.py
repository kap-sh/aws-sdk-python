"""Generated from Smithy shape ``com.amazonaws.rds#OptionVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.boolean
    import aws_sdk_rds.types.string


class OptionVersion(TypedDict, closed=True):
    version: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The version of the option.</p>"""
    is_default: NotRequired["aws_sdk_rds.types.boolean.Boolean"]
    """<p>Indicates whether the version is the default version of the option.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionVersion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "version" in value:
        pairs.append((f"{prefix}.Version", str(value["version"])))
    if "is_default" in value:
        pairs.append(
            (f"{prefix}.IsDefault", "true" if value["is_default"] else "false")
        )


def deserialize_query(el: Element) -> OptionVersion:
    out: OptionVersion = {}  # type: ignore[typeddict-item]
    child_version = el.find("Version")
    if child_version is not None:
        out["version"] = str(child_version.text or "")
    child_is_default = el.find("IsDefault")
    if child_is_default is not None:
        out["is_default"] = (child_is_default.text or "").lower() == "true"
    return out
