"""Generated from Smithy shape ``com.amazonaws.redshift#ServerlessIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class ServerlessIdentifier(TypedDict, closed=True):
    namespace_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The unique identifier for the serverless namespace.</p>"""
    workgroup_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The unique identifier for the workgroup associated with the serverless namespace.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerlessIdentifier, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "namespace_identifier" in value:
        pairs.append(
            (f"{key_prefix}NamespaceIdentifier", str(value["namespace_identifier"]))
        )
    if "workgroup_identifier" in value:
        pairs.append(
            (f"{key_prefix}WorkgroupIdentifier", str(value["workgroup_identifier"]))
        )


def deserialize_query(el: Element) -> ServerlessIdentifier:
    out: ServerlessIdentifier = {}  # type: ignore[typeddict-item]
    child_namespace_identifier = el.find("NamespaceIdentifier")
    if child_namespace_identifier is not None:
        out["namespace_identifier"] = str(child_namespace_identifier.text or "")
    child_workgroup_identifier = el.find("WorkgroupIdentifier")
    if child_workgroup_identifier is not None:
        out["workgroup_identifier"] = str(child_workgroup_identifier.text or "")
    return out
