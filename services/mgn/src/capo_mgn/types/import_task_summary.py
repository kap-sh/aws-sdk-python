"""Generated from Smithy shape ``com.amazonaws.mgn#ImportTaskSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.import_task_summary_applications
    import capo_mgn.types.import_task_summary_servers
    import capo_mgn.types.import_task_summary_waves


class ImportTaskSummary(TypedDict, closed=True):
    waves: NotRequired[
        "capo_mgn.types.import_task_summary_waves.ImportTaskSummaryWaves"
    ]
    """<p>Import task summary waves.</p>"""
    applications: NotRequired[
        "capo_mgn.types.import_task_summary_applications.ImportTaskSummaryApplications"
    ]
    """<p>Import task summary applications.</p>"""
    servers: NotRequired[
        "capo_mgn.types.import_task_summary_servers.ImportTaskSummaryServers"
    ]
    """<p>Import task summary servers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportTaskSummary) -> dict:
    out: dict = {}
    if "waves" in value:
        import capo_mgn.types.import_task_summary_waves

        out["waves"] = capo_mgn.types.import_task_summary_waves.serialize_json(
            value["waves"]
        )
    if "applications" in value:
        import capo_mgn.types.import_task_summary_applications

        out["applications"] = (
            capo_mgn.types.import_task_summary_applications.serialize_json(
                value["applications"]
            )
        )
    if "servers" in value:
        import capo_mgn.types.import_task_summary_servers

        out["servers"] = capo_mgn.types.import_task_summary_servers.serialize_json(
            value["servers"]
        )
    return out


def deserialize_json(data: dict) -> ImportTaskSummary:
    out: ImportTaskSummary = {}  # type: ignore[typeddict-item]
    if "waves" in data:
        import capo_mgn.types.import_task_summary_waves

        out["waves"] = capo_mgn.types.import_task_summary_waves.deserialize_json(
            data["waves"]
        )
    if "applications" in data:
        import capo_mgn.types.import_task_summary_applications

        out["applications"] = (
            capo_mgn.types.import_task_summary_applications.deserialize_json(
                data["applications"]
            )
        )
    if "servers" in data:
        import capo_mgn.types.import_task_summary_servers

        out["servers"] = capo_mgn.types.import_task_summary_servers.deserialize_json(
            data["servers"]
        )
    return out
