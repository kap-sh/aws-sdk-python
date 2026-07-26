"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestExecutionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.test_execution_api_mode
    import capo_lex_models_v2.types.test_execution_modality
    import capo_lex_models_v2.types.test_execution_status
    import capo_lex_models_v2.types.test_execution_target
    import capo_lex_models_v2.types.timestamp


class TestExecutionSummary(TypedDict, closed=True):
    test_execution_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the test execution.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time at which the test execution was created.</p>"""
    last_updated_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time at which the test execution was last updated.</p>"""
    test_execution_status: NotRequired[
        "capo_lex_models_v2.types.test_execution_status.TestExecutionStatus"
    ]
    """<p>The current status of the test execution.</p>"""
    test_set_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the test set used in the test execution.</p>"""
    test_set_name: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>The name of the test set used in the test execution.</p>"""
    target: NotRequired[
        "capo_lex_models_v2.types.test_execution_target.TestExecutionTarget"
    ]
    """<p>Contains information about the bot used for the test execution..</p>"""
    api_mode: NotRequired[
        "capo_lex_models_v2.types.test_execution_api_mode.TestExecutionApiMode"
    ]
    """<p>Specifies whether the API mode for the test execution is streaming or non-streaming.</p>"""
    test_execution_modality: NotRequired[
        "capo_lex_models_v2.types.test_execution_modality.TestExecutionModality"
    ]
    """<p>Specifies whether the data used for the test execution is written or spoken.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestExecutionSummary) -> dict:
    out: dict = {}
    if "test_execution_id" in value:
        out["testExecutionId"] = value["test_execution_id"]
    if "creation_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["creationDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_lex_models_v2.types.timestamp

        out["lastUpdatedDateTime"] = capo_lex_models_v2.types.timestamp.serialize_json(
            value["last_updated_date_time"]
        )
    if "test_execution_status" in value:
        import capo_lex_models_v2.types.test_execution_status

        out["testExecutionStatus"] = (
            capo_lex_models_v2.types.test_execution_status.serialize_json(
                value["test_execution_status"]
            )
        )
    if "test_set_id" in value:
        out["testSetId"] = value["test_set_id"]
    if "test_set_name" in value:
        out["testSetName"] = value["test_set_name"]
    if "target" in value:
        import capo_lex_models_v2.types.test_execution_target

        out["target"] = capo_lex_models_v2.types.test_execution_target.serialize_json(
            value["target"]
        )
    if "api_mode" in value:
        import capo_lex_models_v2.types.test_execution_api_mode

        out["apiMode"] = (
            capo_lex_models_v2.types.test_execution_api_mode.serialize_json(
                value["api_mode"]
            )
        )
    if "test_execution_modality" in value:
        import capo_lex_models_v2.types.test_execution_modality

        out["testExecutionModality"] = (
            capo_lex_models_v2.types.test_execution_modality.serialize_json(
                value["test_execution_modality"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestExecutionSummary:
    out: TestExecutionSummary = {}  # type: ignore[typeddict-item]
    if "testExecutionId" in data:
        out["test_execution_id"] = data["testExecutionId"]
    if "creationDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["creation_date_time"] = capo_lex_models_v2.types.timestamp.deserialize_json(
            data["creationDateTime"]
        )
    if "lastUpdatedDateTime" in data:
        import capo_lex_models_v2.types.timestamp

        out["last_updated_date_time"] = (
            capo_lex_models_v2.types.timestamp.deserialize_json(
                data["lastUpdatedDateTime"]
            )
        )
    if "testExecutionStatus" in data:
        import capo_lex_models_v2.types.test_execution_status

        out["test_execution_status"] = (
            capo_lex_models_v2.types.test_execution_status.deserialize_json(
                data["testExecutionStatus"]
            )
        )
    if "testSetId" in data:
        out["test_set_id"] = data["testSetId"]
    if "testSetName" in data:
        out["test_set_name"] = data["testSetName"]
    if "target" in data:
        import capo_lex_models_v2.types.test_execution_target

        out["target"] = capo_lex_models_v2.types.test_execution_target.deserialize_json(
            data["target"]
        )
    if "apiMode" in data:
        import capo_lex_models_v2.types.test_execution_api_mode

        out["api_mode"] = (
            capo_lex_models_v2.types.test_execution_api_mode.deserialize_json(
                data["apiMode"]
            )
        )
    if "testExecutionModality" in data:
        import capo_lex_models_v2.types.test_execution_modality

        out["test_execution_modality"] = (
            capo_lex_models_v2.types.test_execution_modality.deserialize_json(
                data["testExecutionModality"]
            )
        )
    return out
