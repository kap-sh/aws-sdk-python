"""Generated from Smithy shape ``com.amazonaws.applicationcostprofiler#ListReportDefinitionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_applicationcostprofiler.types.report_definition_list
    import aws_sdk_applicationcostprofiler.types.token


class ListReportDefinitionsResult(TypedDict):
    report_definitions: NotRequired[
        "aws_sdk_applicationcostprofiler.types.report_definition_list.ReportDefinitionList"
    ]
    """<p>The retrieved reports.</p>"""
    next_token: NotRequired["aws_sdk_applicationcostprofiler.types.token.Token"]
    """<p>The value of the next token, if it exists. Null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReportDefinitionsResult) -> dict:
    out: dict = {}
    if "report_definitions" in value:
        import aws_sdk_applicationcostprofiler.types.report_definition_list

        out["reportDefinitions"] = (
            aws_sdk_applicationcostprofiler.types.report_definition_list.serialize_json(
                value["report_definitions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListReportDefinitionsResult:
    out: ListReportDefinitionsResult = {}  # type: ignore[typeddict-item]
    if "reportDefinitions" in data:
        import aws_sdk_applicationcostprofiler.types.report_definition_list

        out["report_definitions"] = (
            aws_sdk_applicationcostprofiler.types.report_definition_list.deserialize_json(
                data["reportDefinitions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
