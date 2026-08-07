"""Generated from Smithy shape ``com.amazonaws.neptune#DBParameterGroupNameMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.string


class DBParameterGroupNameMessage(TypedDict, closed=True):
    db_parameter_group_name: NotRequired["capo_neptune.types.string.String"]
    """<p>Provides the name of the DB parameter group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBParameterGroupNameMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_parameter_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBParameterGroupName", str(value["db_parameter_group_name"]))
        )


def deserialize_query(el: Element) -> DBParameterGroupNameMessage:
    out: DBParameterGroupNameMessage = {}  # type: ignore[typeddict-item]
    child_db_parameter_group_name = el.find("DBParameterGroupName")
    if child_db_parameter_group_name is not None:
        out["db_parameter_group_name"] = str(child_db_parameter_group_name.text or "")
    return out
