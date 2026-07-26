"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DescribeTestExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.failure_reasons
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.name
    import capo_lex_models_v2.types.test_execution_api_mode
    import capo_lex_models_v2.types.test_execution_modality
    import capo_lex_models_v2.types.test_execution_status
    import capo_lex_models_v2.types.test_execution_target
    import capo_lex_models_v2.types.timestamp


class DescribeTestExecutionResponse(TypedDict, closed=True):
    test_execution_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The execution Id for the test set execution.</p>"""
    creation_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The execution creation date and time for the test set execution.</p>"""
    last_updated_date_time: NotRequired["capo_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The date and time of the last update for the execution.</p>"""
    test_execution_status: NotRequired[
        "capo_lex_models_v2.types.test_execution_status.TestExecutionStatus"
    ]
    """<p>The test execution status for the test execution.</p>"""
    test_set_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The test set Id for the test set execution.</p>"""
    test_set_name: NotRequired["capo_lex_models_v2.types.name.Name"]
    """<p>The test set name of the test set execution.</p>"""
    target: NotRequired[
        "capo_lex_models_v2.types.test_execution_target.TestExecutionTarget"
    ]
    """<p>The target bot for the test set execution details.</p>"""
    api_mode: NotRequired[
        "capo_lex_models_v2.types.test_execution_api_mode.TestExecutionApiMode"
    ]
    """<p>Indicates whether we use streaming or non-streaming APIs are used for the test set execution. For streaming, <code>StartConversation</code> Amazon Lex Runtime API is used. Whereas for non-streaming, <code>RecognizeUtterance</code> and <code>RecognizeText</code> Amazon Lex Runtime API is used.</p>"""
    test_execution_modality: NotRequired[
        "capo_lex_models_v2.types.test_execution_modality.TestExecutionModality"
    ]
    """<p>Indicates whether test set is audio or text.</p>"""
    failure_reasons: NotRequired[
        "capo_lex_models_v2.types.failure_reasons.FailureReasons"
    ]
    """<p>Reasons for the failure of the test set execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTestExecutionResponse) -> dict:
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
    if "failure_reasons" in value:
        import capo_lex_models_v2.types.failure_reasons

        out["failureReasons"] = capo_lex_models_v2.types.failure_reasons.serialize_json(
            value["failure_reasons"]
        )
    return out


def deserialize_json(data: dict) -> DescribeTestExecutionResponse:
    out: DescribeTestExecutionResponse = {}  # type: ignore[typeddict-item]
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
    if "failureReasons" in data:
        import capo_lex_models_v2.types.failure_reasons

        out["failure_reasons"] = (
            capo_lex_models_v2.types.failure_reasons.deserialize_json(
                data["failureReasons"]
            )
        )
    return out
