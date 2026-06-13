"""Generated from Smithy shape ``com.amazonaws.emr#ListNotebookExecutionsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.date
    import aws_sdk_emr.types.marker
    import aws_sdk_emr.types.notebook_execution_status
    import aws_sdk_emr.types.xml_string
    import aws_sdk_emr.types.xml_string_max_len256

ListNotebookExecutionsInput = TypedDict(
    "ListNotebookExecutionsInput",
    {
        "editor_id": NotRequired[
            "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
        ],
        "status": NotRequired[
            "aws_sdk_emr.types.notebook_execution_status.NotebookExecutionStatus"
        ],
        "from": NotRequired["aws_sdk_emr.types.date.Date"],
        "to": NotRequired["aws_sdk_emr.types.date.Date"],
        "marker": NotRequired["aws_sdk_emr.types.marker.Marker"],
        "execution_engine_id": NotRequired["aws_sdk_emr.types.xml_string.XmlString"],
    },
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListNotebookExecutionsInput) -> dict:
    out: dict = {}
    if "editor_id" in value:
        out["EditorId"] = value["editor_id"]
    if "status" in value:
        import aws_sdk_emr.types.notebook_execution_status

        out["Status"] = (
            aws_sdk_emr.types.notebook_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "from" in value:
        import aws_sdk_emr.types.date

        out["From"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(value["from"])
    if "to" in value:
        import aws_sdk_emr.types.date

        out["To"] = aws_sdk_emr.types.date.serialize_aws_json_1_1(value["to"])
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
        import aws_sdk_emr.types.notebook_execution_status

        out["status"] = (
            aws_sdk_emr.types.notebook_execution_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "From" in data:
        import aws_sdk_emr.types.date

        out["from"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(data["From"])
    if "To" in data:
        import aws_sdk_emr.types.date

        out["to"] = aws_sdk_emr.types.date.deserialize_aws_json_1_1(data["To"])
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "ExecutionEngineId" in data:
        out["execution_engine_id"] = data["ExecutionEngineId"]
    return out
