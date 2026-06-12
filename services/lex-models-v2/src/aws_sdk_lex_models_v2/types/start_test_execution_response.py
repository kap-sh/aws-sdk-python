"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#StartTestExecutionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.id
    import aws_sdk_lex_models_v2.types.test_execution_api_mode
    import aws_sdk_lex_models_v2.types.test_execution_modality
    import aws_sdk_lex_models_v2.types.test_execution_target
    import aws_sdk_lex_models_v2.types.timestamp


class StartTestExecutionResponse(TypedDict):
    test_execution_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The unique identifier of the test set execution.</p>"""
    creation_date_time: NotRequired["aws_sdk_lex_models_v2.types.timestamp.Timestamp"]
    """<p>The creation date and time for the test set execution.</p>"""
    test_set_id: NotRequired["aws_sdk_lex_models_v2.types.id.Id"]
    """<p>The test set Id for the test set execution.</p>"""
    target: NotRequired[
        "aws_sdk_lex_models_v2.types.test_execution_target.TestExecutionTarget"
    ]
    """<p>The target bot for the test set execution.</p>"""
    api_mode: NotRequired[
        "aws_sdk_lex_models_v2.types.test_execution_api_mode.TestExecutionApiMode"
    ]
    """<p>Indicates whether we use streaming or non-streaming APIs for the test set execution. For streaming, StartConversation Amazon Lex Runtime API is used. Whereas for non-streaming, RecognizeUtterance and RecognizeText Amazon Lex Runtime API are used.</p>"""
    test_execution_modality: NotRequired[
        "aws_sdk_lex_models_v2.types.test_execution_modality.TestExecutionModality"
    ]
    """<p>Indicates whether audio or text is used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTestExecutionResponse) -> dict:
    out: dict = {}
    if "test_execution_id" in value:
        out["testExecutionId"] = value["test_execution_id"]
    if "creation_date_time" in value:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creationDateTime"] = aws_sdk_lex_models_v2.types.timestamp.serialize_json(
            value["creation_date_time"]
        )
    if "test_set_id" in value:
        out["testSetId"] = value["test_set_id"]
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


def deserialize_json(data: dict) -> StartTestExecutionResponse:
    out: StartTestExecutionResponse = {}  # type: ignore[typeddict-item]
    if "testExecutionId" in data:
        out["test_execution_id"] = data["testExecutionId"]
    if "creationDateTime" in data:
        import aws_sdk_lex_models_v2.types.timestamp

        out["creation_date_time"] = (
            aws_sdk_lex_models_v2.types.timestamp.deserialize_json(
                data["creationDateTime"]
            )
        )
    if "testSetId" in data:
        out["test_set_id"] = data["testSetId"]
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
