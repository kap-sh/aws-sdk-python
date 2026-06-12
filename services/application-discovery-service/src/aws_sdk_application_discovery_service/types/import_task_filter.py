"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#ImportTaskFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.import_task_filter_name
    import aws_sdk_application_discovery_service.types.import_task_filter_value_list


class ImportTaskFilter(TypedDict):
    name: NotRequired[
        "aws_sdk_application_discovery_service.types.import_task_filter_name.ImportTaskFilterName"
    ]
    """<p>The name, status, or import task ID for a specific import task.</p>"""
    values: NotRequired[
        "aws_sdk_application_discovery_service.types.import_task_filter_value_list.ImportTaskFilterValueList"
    ]
    """<p>An array of strings that you can provide to match against a specific name, status, or import task ID to filter the results for your import task queries.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportTaskFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_application_discovery_service.types.import_task_filter_name

        out["name"] = (
            aws_sdk_application_discovery_service.types.import_task_filter_name.serialize_aws_json_1_1(
                value["name"]
            )
        )
    if "values" in value:
        import aws_sdk_application_discovery_service.types.import_task_filter_value_list

        out["values"] = (
            aws_sdk_application_discovery_service.types.import_task_filter_value_list.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportTaskFilter:
    out: ImportTaskFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import aws_sdk_application_discovery_service.types.import_task_filter_name

        out["name"] = (
            aws_sdk_application_discovery_service.types.import_task_filter_name.deserialize_aws_json_1_1(
                data["name"]
            )
        )
    if "values" in data:
        import aws_sdk_application_discovery_service.types.import_task_filter_value_list

        out["values"] = (
            aws_sdk_application_discovery_service.types.import_task_filter_value_list.deserialize_aws_json_1_1(
                data["values"]
            )
        )
    return out
