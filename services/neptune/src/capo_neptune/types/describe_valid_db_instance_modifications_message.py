"""Generated from Smithy shape ``com.amazonaws.neptune#DescribeValidDBInstanceModificationsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.string


class DescribeValidDBInstanceModificationsMessage(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>The customer identifier or the ARN of your DB instance.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeValidDBInstanceModificationsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )


def deserialize_query(el: Element) -> DescribeValidDBInstanceModificationsMessage:
    out: DescribeValidDBInstanceModificationsMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    return out
