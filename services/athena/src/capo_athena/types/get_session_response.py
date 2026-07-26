"""Generated from Smithy shape ``com.amazonaws.athena#GetSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.description_string
    import capo_athena.types.engine_configuration
    import capo_athena.types.monitoring_configuration
    import capo_athena.types.name_string
    import capo_athena.types.session_configuration
    import capo_athena.types.session_id
    import capo_athena.types.session_statistics
    import capo_athena.types.session_status
    import capo_athena.types.work_group_name


class GetSessionResponse(TypedDict, closed=True):
    session_id: NotRequired["capo_athena.types.session_id.SessionId"]
    """<p>The session ID.</p>"""
    description: NotRequired["capo_athena.types.description_string.DescriptionString"]
    """<p>The session description.</p>"""
    work_group: NotRequired["capo_athena.types.work_group_name.WorkGroupName"]
    """<p>The workgroup to which the session belongs.</p>"""
    engine_version: NotRequired["capo_athena.types.name_string.NameString"]
    """<p>The engine version used by the session (for example, <code>PySpark engine version 3</code>). You can get a list of engine versions by calling <a>ListEngineVersions</a>.</p>"""
    engine_configuration: NotRequired[
        "capo_athena.types.engine_configuration.EngineConfiguration"
    ]
    """<p>Contains engine configuration information like DPU usage.</p>"""
    notebook_version: NotRequired["capo_athena.types.name_string.NameString"]
    """<p>The notebook version.</p>"""
    monitoring_configuration: NotRequired[
        "capo_athena.types.monitoring_configuration.MonitoringConfiguration"
    ]
    session_configuration: NotRequired[
        "capo_athena.types.session_configuration.SessionConfiguration"
    ]
    """<p>Contains the workgroup configuration information used by the session.</p>"""
    status: NotRequired["capo_athena.types.session_status.SessionStatus"]
    """<p>Contains information about the status of the session.</p>"""
    statistics: NotRequired["capo_athena.types.session_statistics.SessionStatistics"]
    """<p>Contains the DPU execution time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSessionResponse) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "work_group" in value:
        out["WorkGroup"] = value["work_group"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "engine_configuration" in value:
        import capo_athena.types.engine_configuration

        out["EngineConfiguration"] = (
            capo_athena.types.engine_configuration.serialize_aws_json_1_1(
                value["engine_configuration"]
            )
        )
    if "notebook_version" in value:
        out["NotebookVersion"] = value["notebook_version"]
    if "monitoring_configuration" in value:
        import capo_athena.types.monitoring_configuration

        out["MonitoringConfiguration"] = (
            capo_athena.types.monitoring_configuration.serialize_aws_json_1_1(
                value["monitoring_configuration"]
            )
        )
    if "session_configuration" in value:
        import capo_athena.types.session_configuration

        out["SessionConfiguration"] = (
            capo_athena.types.session_configuration.serialize_aws_json_1_1(
                value["session_configuration"]
            )
        )
    if "status" in value:
        import capo_athena.types.session_status

        out["Status"] = capo_athena.types.session_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "statistics" in value:
        import capo_athena.types.session_statistics

        out["Statistics"] = capo_athena.types.session_statistics.serialize_aws_json_1_1(
            value["statistics"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSessionResponse:
    out: GetSessionResponse = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "WorkGroup" in data:
        out["work_group"] = data["WorkGroup"]
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "EngineConfiguration" in data:
        import capo_athena.types.engine_configuration

        out["engine_configuration"] = (
            capo_athena.types.engine_configuration.deserialize_aws_json_1_1(
                data["EngineConfiguration"]
            )
        )
    if "NotebookVersion" in data:
        out["notebook_version"] = data["NotebookVersion"]
    if "MonitoringConfiguration" in data:
        import capo_athena.types.monitoring_configuration

        out["monitoring_configuration"] = (
            capo_athena.types.monitoring_configuration.deserialize_aws_json_1_1(
                data["MonitoringConfiguration"]
            )
        )
    if "SessionConfiguration" in data:
        import capo_athena.types.session_configuration

        out["session_configuration"] = (
            capo_athena.types.session_configuration.deserialize_aws_json_1_1(
                data["SessionConfiguration"]
            )
        )
    if "Status" in data:
        import capo_athena.types.session_status

        out["status"] = capo_athena.types.session_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "Statistics" in data:
        import capo_athena.types.session_statistics

        out["statistics"] = (
            capo_athena.types.session_statistics.deserialize_aws_json_1_1(
                data["Statistics"]
            )
        )
    return out
