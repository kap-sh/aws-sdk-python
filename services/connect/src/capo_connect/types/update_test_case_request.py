"""Generated from Smithy shape ``com.amazonaws.connect#UpdateTestCaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id_or_arn
    import capo_connect.types.region_name
    import capo_connect.types.test_case_content
    import capo_connect.types.test_case_description
    import capo_connect.types.test_case_entry_point
    import capo_connect.types.test_case_id
    import capo_connect.types.test_case_initialization_data
    import capo_connect.types.test_case_name
    import capo_connect.types.test_case_status
    import capo_connect.types.timestamp


class UpdateTestCaseRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the Amazon Connect instance.</p>"""
    test_case_id: "capo_connect.types.test_case_id.TestCaseId"
    """<p>The identifier of the test case to update.</p>"""
    content: NotRequired["capo_connect.types.test_case_content.TestCaseContent"]
    """<p>The JSON string that represents the content of the test.</p>"""
    entry_point: NotRequired[
        "capo_connect.types.test_case_entry_point.TestCaseEntryPoint"
    ]
    """<p>Defines the starting point for your test.</p>"""
    initialization_data: NotRequired[
        "capo_connect.types.test_case_initialization_data.TestCaseInitializationData"
    ]
    """<p>Defines the test attributes for precise data representation.</p>"""
    name: NotRequired["capo_connect.types.test_case_name.TestCaseName"]
    """<p>The name of the test case.</p>"""
    description: NotRequired[
        "capo_connect.types.test_case_description.TestCaseDescription"
    ]
    """<p>The description of the test case.</p>"""
    status: NotRequired["capo_connect.types.test_case_status.TestCaseStatus"]
    """<p>Indicates the test status as either SAVED or PUBLISHED. The PUBLISHED status will initiate validation on the content. The SAVED status does not initiate validation of the content.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The time at which the resource was last modified.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The region in which the resource was last modified</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTestCaseRequest) -> dict:
    out: dict = {}
    if "content" in value:
        out["Content"] = value["content"]
    if "entry_point" in value:
        import capo_connect.types.test_case_entry_point

        out["EntryPoint"] = capo_connect.types.test_case_entry_point.serialize_json(
            value["entry_point"]
        )
    if "initialization_data" in value:
        out["InitializationData"] = value["initialization_data"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_connect.types.test_case_status

        out["Status"] = capo_connect.types.test_case_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> UpdateTestCaseRequest:
    out: UpdateTestCaseRequest = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        out["content"] = data["Content"]
    if "EntryPoint" in data:
        import capo_connect.types.test_case_entry_point

        out["entry_point"] = capo_connect.types.test_case_entry_point.deserialize_json(
            data["EntryPoint"]
        )
    if "InitializationData" in data:
        out["initialization_data"] = data["InitializationData"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import capo_connect.types.test_case_status

        out["status"] = capo_connect.types.test_case_status.deserialize_json(
            data["Status"]
        )
    return out
