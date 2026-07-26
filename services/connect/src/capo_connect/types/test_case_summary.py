"""Generated from Smithy shape ``com.amazonaws.connect#TestCaseSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.contact_flow_name
    import capo_connect.types.region_name
    import capo_connect.types.test_case_id
    import capo_connect.types.test_case_status
    import capo_connect.types.timestamp


class TestCaseSummary(TypedDict, closed=True):
    id: NotRequired["capo_connect.types.test_case_id.TestCaseId"]
    """<p>The identifier of the test case.</p>"""
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the test case.</p>"""
    name: NotRequired["capo_connect.types.contact_flow_name.ContactFlowName"]
    """<p>The name of the test case.</p>"""
    status: NotRequired["capo_connect.types.test_case_status.TestCaseStatus"]
    """<p>The status of the test case.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The time at which the test case was last modified.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The region in which the test case was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestCaseSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
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
    return out


def deserialize_json(data: dict) -> TestCaseSummary:
    out: TestCaseSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
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
    return out
