"""Generated from Smithy shape ``com.amazonaws.connect#CreateTestCaseRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id_or_arn
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.test_case_content
    import aws_sdk_connect.types.test_case_description
    import aws_sdk_connect.types.test_case_entry_point
    import aws_sdk_connect.types.test_case_id
    import aws_sdk_connect.types.test_case_initialization_data
    import aws_sdk_connect.types.test_case_name
    import aws_sdk_connect.types.test_case_status
    import aws_sdk_connect.types.timestamp


class CreateTestCaseRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id_or_arn.InstanceIdOrArn"
    """<p>The identifier of the Amazon Connect instance.</p>"""
    name: "aws_sdk_connect.types.test_case_name.TestCaseName"
    """<p>The name of the test.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.test_case_description.TestCaseDescription"
    ]
    """<p>The description of the test.</p>"""
    content: "aws_sdk_connect.types.test_case_content.TestCaseContent"
    """<p>The JSON string that represents the content of the test.</p>"""
    entry_point: NotRequired[
        "aws_sdk_connect.types.test_case_entry_point.TestCaseEntryPoint"
    ]
    """<p>Defines the starting point for your test.</p>"""
    initialization_data: NotRequired[
        "aws_sdk_connect.types.test_case_initialization_data.TestCaseInitializationData"
    ]
    """<p>Defines the initial custom attributes for your test.</p>"""
    status: NotRequired["aws_sdk_connect.types.test_case_status.TestCaseStatus"]
    """<p>Indicates the test status as either SAVED or PUBLISHED. The PUBLISHED status will initiate validation on the content. The SAVED status does not initiate validation of the content.</p>"""
    test_case_id: NotRequired["aws_sdk_connect.types.test_case_id.TestCaseId"]
    """<p>Id of the test case if you want to create it in a replica region using Amazon Connect Global Resiliency</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The time at which the resource was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The region in which the resource was last modified</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTestCaseRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Content"] = value["content"]
    if "entry_point" in value:
        import aws_sdk_connect.types.test_case_entry_point

        out["EntryPoint"] = aws_sdk_connect.types.test_case_entry_point.serialize_json(
            value["entry_point"]
        )
    if "initialization_data" in value:
        out["InitializationData"] = value["initialization_data"]
    if "status" in value:
        import aws_sdk_connect.types.test_case_status

        out["Status"] = aws_sdk_connect.types.test_case_status.serialize_json(
            value["status"]
        )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateTestCaseRequest:
    out: CreateTestCaseRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateTestCaseRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Content" in data:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("CreateTestCaseRequest.content required")
    if "EntryPoint" in data:
        import aws_sdk_connect.types.test_case_entry_point

        out["entry_point"] = (
            aws_sdk_connect.types.test_case_entry_point.deserialize_json(
                data["EntryPoint"]
            )
        )
    if "InitializationData" in data:
        out["initialization_data"] = data["InitializationData"]
    if "Status" in data:
        import aws_sdk_connect.types.test_case_status

        out["status"] = aws_sdk_connect.types.test_case_status.deserialize_json(
            data["Status"]
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
