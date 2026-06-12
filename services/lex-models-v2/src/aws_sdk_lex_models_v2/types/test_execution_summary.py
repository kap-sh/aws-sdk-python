"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestExecutionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.name
    import aws_sdk_lex_models_v2.types.test_execution_api_mode
    import aws_sdk_lex_models_v2.types.test_execution_modality
    import aws_sdk_lex_models_v2.types.test_execution_status
    import aws_sdk_lex_models_v2.types.test_execution_target
    import aws_sdk_lex_models_v2.types.timestamp


class TestExecutionSummary(TypedDict):
    test_execution_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the test execution.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time at which the test execution was created.</p>"""
    last_updated_date_time: NotRequired[
        "aws_sdk_lex_models_v2.types.timestamp.Timestamp"
    ]
    """<p>The date and time at which the test execution was last updated.</p>"""
    test_execution_status: NotRequired[
        "aws_sdk_lex_models_v2.types.test_execution_status.TestExecutionStatus"
    ]
    """<p>The current status of the test execution.</p>"""
    test_set_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the test set used in the test execution.</p>"""
    test_set_name: NotRequired["aws_sdk_lex_models_v2.types.name.Name"]
    """<p>The name of the test set used in the test execution.</p>"""
    target: NotRequired[
        "aws_sdk_lex_models_v2.types.test_execution_target.TestExecutionTarget"
    ]
    """<p>Contains information about the bot used for the test execution..</p>"""
    api_mode: NotRequired[
        "aws_sdk_lex_models_v2.types.test_execution_api_mode.TestExecutionApiMode"
    ]
    """<p>Specifies whether the API mode for the test execution is streaming or non-streaming.</p>"""
    test_execution_modality: NotRequired[
        "aws_sdk_lex_models_v2.types.test_execution_modality.TestExecutionModality"
    ]
    """<p>Specifies whether the data used for the test execution is written or spoken.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestExecutionSummary) -> dict:
    out: dict = {}
    if "test_execution_id" in value:
        out["testExecutionId"] = value["test_execution_id"]
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = (
            aws_sdk_lex_models_v2.types.timestamp.serialize_json(
                value["last_updated_date_time"]
            )
        )
    if "test_execution_status" in value:
        import aws_sdk_lex_models_v2.types.test_execution_status

        out["testExecutionStatus"] = (
            aws_sdk_lex_models_v2.types.test_execution_status.serialize_json(
                value["test_execution_status"]
            )
        )
    if "test_set_id" in value:
        out["testSetId"] = value["test_set_id"]
    if "test_set_name" in value:
        out["testSetName"] = value["test_set_name"]
    if "target" in value:
        import aws_sdk_lex_models_v2.types.test_execution_target

        out["target"] = (
            aws_sdk_lex_models_v2.types.test_execution_target.serialize_json(
                value["target"]
            )
        )
    if "api_mode" in value:
        import aws_sdk_lex_models_v2.types.test_execution_api_mode

        out["apiMode"] = (
            aws_sdk_lex_models_v2.types.test_execution_api_mode.serialize_json(
                value["api_mode"]
            )
        )
    if "test_execution_modality" in value:
        import aws_sdk_lex_models_v2.types.test_execution_modality

        out["testExecutionModality"] = (
            aws_sdk_lex_models_v2.types.test_execution_modality.serialize_json(
                value["test_execution_modality"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestExecutionSummary:
    out: TestExecutionSummary = {}  # type: ignore[typeddict-item]
    if "testExecutionId" in data:
        out["test_execution_id"] = data["testExecutionId"]
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    if "testExecutionStatus" in data:
        import aws_sdk_lex_models_v2.types.test_execution_status

        out["test_execution_status"] = (
            aws_sdk_lex_models_v2.types.test_execution_status.deserialize_json(
                data["testExecutionStatus"]
            )
        )
    if "testSetId" in data:
        out["test_set_id"] = data["testSetId"]
    if "testSetName" in data:
        out["test_set_name"] = data["testSetName"]
    if "target" in data:
        import aws_sdk_lex_models_v2.types.test_execution_target

        out["target"] = (
            aws_sdk_lex_models_v2.types.test_execution_target.deserialize_json(
                data["target"]
            )
        )
    if "apiMode" in data:
        import aws_sdk_lex_models_v2.types.test_execution_api_mode

        out["api_mode"] = (
            aws_sdk_lex_models_v2.types.test_execution_api_mode.deserialize_json(
                data["apiMode"]
            )
        )
    if "testExecutionModality" in data:
        import aws_sdk_lex_models_v2.types.test_execution_modality

        out["test_execution_modality"] = (
            aws_sdk_lex_models_v2.types.test_execution_modality.deserialize_json(
                data["testExecutionModality"]
            )
        )
    return out
