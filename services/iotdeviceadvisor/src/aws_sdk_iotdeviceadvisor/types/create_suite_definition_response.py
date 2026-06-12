"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#CreateSuiteDefinitionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.amazon_resource_name
    import aws_sdk_iotdeviceadvisor.types.suite_definition_name
    import aws_sdk_iotdeviceadvisor.types.timestamp
    import aws_sdk_iotdeviceadvisor.types.uuid


class CreateSuiteDefinitionResponse(TypedDict):
    suite_definition_id: NotRequired["aws_sdk_iotdeviceadvisor.types.uuid.UUID"]
    """<p>The UUID of the test suite created.</p>"""
    suite_definition_arn: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the test suite.</p>"""
    suite_definition_name: NotRequired[
        "aws_sdk_iotdeviceadvisor.types.suite_definition_name.SuiteDefinitionName"
    ]
    """<p>The suite definition name of the test suite. This is a required parameter.</p>"""
    created_at: NotRequired["aws_sdk_iotdeviceadvisor.types.timestamp.Timestamp"]
    """<p>The timestamp of when the test suite was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSuiteDefinitionResponse) -> dict:
    out: dict = {}
    if "suite_definition_id" in value:
        out["suiteDefinitionId"] = value["suite_definition_id"]
    if "suite_definition_arn" in value:
        out["suiteDefinitionArn"] = value["suite_definition_arn"]
    if "suite_definition_name" in value:
        out["suiteDefinitionName"] = value["suite_definition_name"]
    if "created_at" in value:
        import aws_sdk_iotdeviceadvisor.types.timestamp

        out["createdAt"] = aws_sdk_iotdeviceadvisor.types.timestamp.serialize_json(
            value["created_at"]
        )
    return out


def deserialize_json(data: dict) -> CreateSuiteDefinitionResponse:
    out: CreateSuiteDefinitionResponse = {}  # type: ignore[typeddict-item]
    if "suiteDefinitionId" in data:
        out["suite_definition_id"] = data["suiteDefinitionId"]
    if "suiteDefinitionArn" in data:
        out["suite_definition_arn"] = data["suiteDefinitionArn"]
    if "suiteDefinitionName" in data:
        out["suite_definition_name"] = data["suiteDefinitionName"]
    if "createdAt" in data:
        import aws_sdk_iotdeviceadvisor.types.timestamp

        out["created_at"] = aws_sdk_iotdeviceadvisor.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    return out
