"""Generated from Smithy shape ``com.amazonaws.emr#ListNotebookExecutionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.date
    import capo_emr.types.marker
    import capo_emr.types.notebook_execution_status
    import capo_emr.types.xml_string
    import capo_emr.types.xml_string_max_len256

ListNotebookExecutionsInput = TypedDict(
    "ListNotebookExecutionsInput",
    {
        "editor_id": NotRequired[
            "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ],
        "status": NotRequired[
            "capo_emr.types.notebook_execution_status.NotebookExecutionStatus"
        ],
        "from": NotRequired["capo_emr.types.date.Date"],
        "to": NotRequired["capo_emr.types.date.Date"],
        "marker": NotRequired["capo_emr.types.marker.Marker"],
        "execution_engine_id": NotRequired["capo_emr.types.xml_string.XmlString"],
    },
    closed=True,
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListNotebookExecutionsInput) -> dict:
    out: dict = {}
    if "editor_id" in value:
        out["EditorId"] = value["editor_id"]
    if "status" in value:
        import capo_emr.types.notebook_execution_status

        out["Status"] = capo_emr.types.notebook_execution_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "from" in value:
        import capo_emr.types.date

        out["From"] = capo_emr.types.date.serialize_aws_json_1_1(value["from"])
    if "to" in value:
        import capo_emr.types.date

        out["To"] = capo_emr.types.date.serialize_aws_json_1_1(value["to"])
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "execution_engine_id" in value:
        out["ExecutionEngineId"] = value["execution_engine_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListNotebookExecutionsInput:
    out: ListNotebookExecutionsInput = {}  # type: ignore[typeddict-item]
    if "EditorId" in data:
        out["editor_id"] = data["EditorId"]
    if "Status" in data:
        import capo_emr.types.notebook_execution_status

        out["status"] = (
            capo_emr.types.notebook_execution_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "From" in data:
        import capo_emr.types.date

        out["from"] = capo_emr.types.date.deserialize_aws_json_1_1(data["From"])
    if "To" in data:
        import capo_emr.types.date

        out["to"] = capo_emr.types.date.deserialize_aws_json_1_1(data["To"])
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "ExecutionEngineId" in data:
        out["execution_engine_id"] = data["ExecutionEngineId"]
    return out
