"""Generated from Smithy shape ``com.amazonaws.rds#ModifyDBShardGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_shard_group_identifier
    import aws_sdk_rds.types.double_optional
    import aws_sdk_rds.types.integer_optional


class ModifyDBShardGroupMessage(TypedDict, closed=True):
    db_shard_group_identifier: NotRequired[
        "aws_sdk_rds.types.db_shard_group_identifier.DBShardGroupIdentifier"
    ]
    """<p>The name of the DB shard group to modify.</p>"""
    max_acu: NotRequired["aws_sdk_rds.types.double_optional.DoubleOptional"]
    """<p>The maximum capacity of the DB shard group in Aurora capacity units (ACUs).</p>"""
    min_acu: NotRequired["aws_sdk_rds.types.double_optional.DoubleOptional"]
    """<p>The minimum capacity of the DB shard group in Aurora capacity units (ACUs).</p>"""
    compute_redundancy: NotRequired[
        "aws_sdk_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>Specifies whether to create standby DB shard groups for the DB shard group. Valid values are the following:</p> <ul> <li> <p>0 - Creates a DB shard group without a standby DB shard group. This is the default value.</p> </li> <li> <p>1 - Creates a DB shard group with a standby DB shard group in a different Availability Zone (AZ).</p> </li> <li> <p>2 - Creates a DB shard group with two standby DB shard groups in two different AZs.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyDBShardGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_shard_group_identifier" in value:
        pairs.append(
            (
                f"{prefix}.DBShardGroupIdentifier",
                str(value["db_shard_group_identifier"]),
            )
        )
    if "max_acu" in value:
        pairs.append((f"{prefix}.MaxACU", str(value["max_acu"])))
    if "min_acu" in value:
        pairs.append((f"{prefix}.MinACU", str(value["min_acu"])))
    if "compute_redundancy" in value:
        pairs.append((f"{prefix}.ComputeRedundancy", str(value["compute_redundancy"])))


def deserialize_query(el: Element) -> ModifyDBShardGroupMessage:
    out: ModifyDBShardGroupMessage = {}  # type: ignore[typeddict-item]
    child_db_shard_group_identifier = el.find("DBShardGroupIdentifier")
    if child_db_shard_group_identifier is not None:
        out["db_shard_group_identifier"] = str(
            child_db_shard_group_identifier.text or ""
        )
    child_max_acu = el.find("MaxACU")
    if child_max_acu is not None:
        out["max_acu"] = float(child_max_acu.text or "")
    child_min_acu = el.find("MinACU")
    if child_min_acu is not None:
        out["min_acu"] = float(child_min_acu.text or "")
    child_compute_redundancy = el.find("ComputeRedundancy")
    if child_compute_redundancy is not None:
        out["compute_redundancy"] = int(child_compute_redundancy.text or "")
    return out
