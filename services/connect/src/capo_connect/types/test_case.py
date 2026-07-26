"""Generated from Smithy shape ``com.amazonaws.connect#TestCase``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.region_name
    import capo_connect.types.tag_map
    import capo_connect.types.test_case_content
    import capo_connect.types.test_case_description
    import capo_connect.types.test_case_entry_point
    import capo_connect.types.test_case_id
    import capo_connect.types.test_case_initialization_data
    import capo_connect.types.test_case_name
    import capo_connect.types.test_case_sha256
    import capo_connect.types.test_case_status
    import capo_connect.types.timestamp


class TestCase(TypedDict, closed=True):
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the test case.</p>"""
    id: NotRequired["capo_connect.types.test_case_id.TestCaseId"]
    """<p>The identifier of the test case.</p>"""
    name: NotRequired["capo_connect.types.test_case_name.TestCaseName"]
    """<p>The name of the test case.</p>"""
    content: NotRequired["capo_connect.types.test_case_content.TestCaseContent"]
    """<p>The JSON string that represents the content of the test.</p>"""
    entry_point: NotRequired[
        "capo_connect.types.test_case_entry_point.TestCaseEntryPoint"
    ]
    """<p>Defines the starting point for the test, including channel type and parameters.</p>"""
    initialization_data: NotRequired[
        "capo_connect.types.test_case_initialization_data.TestCaseInitializationData"
    ]
    """<p>Defines the test attributes for precise data representation. The value must be a valid JSON string.</p>"""
    description: NotRequired[
        "capo_connect.types.test_case_description.TestCaseDescription"
    ]
    """<p>The description of the test case.</p>"""
    status: NotRequired["capo_connect.types.test_case_status.TestCaseStatus"]
    """<p>Indicates the test status as either SAVED or PUBLISHED.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The time at which the test case was last modified.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The region in which the test case was last modified.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    test_case_sha256: NotRequired["capo_connect.types.test_case_sha256.TestCaseSha256"]
    """<p>The SHA256 hash of the test case content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestCase) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "content" in value:
        out["Content"] = value["content"]
    if "entry_point" in value:
        import capo_connect.types.test_case_entry_point

        out["EntryPoint"] = capo_connect.types.test_case_entry_point.serialize_json(
            value["entry_point"]
        )
    if "initialization_data" in value:
        out["InitializationData"] = value["initialization_data"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_connect.types.test_case_status

        out["Status"] = capo_connect.types.test_case_status.serialize_json(
            value["status"]
        )
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    if "test_case_sha256" in value:
        out["TestCaseSha256"] = value["test_case_sha256"]
    return out


def deserialize_json(data: dict) -> TestCase:
    out: TestCase = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Content" in data:
        out["content"] = data["Content"]
    if "EntryPoint" in data:
        import capo_connect.types.test_case_entry_point

        out["entry_point"] = capo_connect.types.test_case_entry_point.deserialize_json(
            data["EntryPoint"]
        )
    if "InitializationData" in data:
        out["initialization_data"] = data["InitializationData"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import capo_connect.types.test_case_status

        out["status"] = capo_connect.types.test_case_status.deserialize_json(
            data["Status"]
        )
    if "LastModifiedTime" in data:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    if "Tags" in data:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    if "TestCaseSha256" in data:
        out["test_case_sha256"] = data["TestCaseSha256"]
    return out
