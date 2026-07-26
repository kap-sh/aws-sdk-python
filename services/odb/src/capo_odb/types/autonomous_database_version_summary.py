"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabaseVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.db_workload


class AutonomousDatabaseVersionSummary(TypedDict, closed=True):
    db_workload: NotRequired["capo_odb.types.db_workload.DbWorkload"]
    """<p>The intended use of the Autonomous Database that the version supports, such as transaction processing, data warehouse, JSON database, or APEX.</p>"""
    details: NotRequired["str"]
    """<p>Additional details about the Autonomous Database software version.</p>"""
    version: NotRequired["str"]
    """<p>The Oracle Database software version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabaseVersionSummary) -> dict:
    out: dict = {}
    if "db_workload" in value:
        import capo_odb.types.db_workload

        out["dbWorkload"] = capo_odb.types.db_workload.serialize_aws_json_1_0(
            value["db_workload"]
        )
    if "details" in value:
        out["details"] = value["details"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AutonomousDatabaseVersionSummary:
    out: AutonomousDatabaseVersionSummary = {}  # type: ignore[typeddict-item]
    if "dbWorkload" in data:
        import capo_odb.types.db_workload

        out["db_workload"] = capo_odb.types.db_workload.deserialize_aws_json_1_0(
            data["dbWorkload"]
        )
    if "details" in data:
        out["details"] = data["details"]
    if "version" in data:
        out["version"] = data["version"]
    return out
