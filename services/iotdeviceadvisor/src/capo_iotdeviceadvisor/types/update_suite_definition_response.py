"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#UpdateSuiteDefinitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotdeviceadvisor.types.amazon_resource_name
    import capo_iotdeviceadvisor.types.suite_definition_name
    import capo_iotdeviceadvisor.types.suite_definition_version
    import capo_iotdeviceadvisor.types.timestamp
    import capo_iotdeviceadvisor.types.uuid


class UpdateSuiteDefinitionResponse(TypedDict, closed=True):
    suite_definition_id: NotRequired["capo_iotdeviceadvisor.types.uuid.UUID"]
    """<p>Suite definition ID of the updated test suite.</p>"""
    suite_definition_arn: NotRequired[
        "capo_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>Amazon Resource Name (ARN) of the updated test suite.</p>"""
    suite_definition_name: NotRequired[
        "capo_iotdeviceadvisor.types.suite_definition_name.SuiteDefinitionName"
    ]
    """<p>Updates the suite definition name. This is a required parameter.</p>"""
    suite_definition_version: NotRequired[
        "capo_iotdeviceadvisor.types.suite_definition_version.SuiteDefinitionVersion"
    ]
    """<p>Suite definition version of the updated test suite.</p>"""
    created_at: NotRequired["capo_iotdeviceadvisor.types.timestamp.Timestamp"]
    """<p>Timestamp of when the test suite was created.</p>"""
    last_updated_at: NotRequired["capo_iotdeviceadvisor.types.timestamp.Timestamp"]
    """<p>Timestamp of when the test suite was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSuiteDefinitionResponse) -> dict:
    out: dict = {}
    if "suite_definition_id" in value:
        out["suiteDefinitionId"] = value["suite_definition_id"]
    if "suite_definition_arn" in value:
        out["suiteDefinitionArn"] = value["suite_definition_arn"]
    if "suite_definition_name" in value:
        out["suiteDefinitionName"] = value["suite_definition_name"]
    if "suite_definition_version" in value:
        out["suiteDefinitionVersion"] = value["suite_definition_version"]
    if "created_at" in value:
        import capo_iotdeviceadvisor.types.timestamp

        out["createdAt"] = capo_iotdeviceadvisor.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_iotdeviceadvisor.types.timestamp

        out["lastUpdatedAt"] = capo_iotdeviceadvisor.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> UpdateSuiteDefinitionResponse:
    out: UpdateSuiteDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "suiteDefinitionId" in data:
        out["suite_definition_id"] = data["suiteDefinitionId"]
    if "suiteDefinitionArn" in data:
        out["suite_definition_arn"] = data["suiteDefinitionArn"]
    if "suiteDefinitionName" in data:
        out["suite_definition_name"] = data["suiteDefinitionName"]
    if "suiteDefinitionVersion" in data:
        out["suite_definition_version"] = data["suiteDefinitionVersion"]
    if "createdAt" in data:
        import capo_iotdeviceadvisor.types.timestamp

        out["created_at"] = capo_iotdeviceadvisor.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import capo_iotdeviceadvisor.types.timestamp

        out["last_updated_at"] = capo_iotdeviceadvisor.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    return out
