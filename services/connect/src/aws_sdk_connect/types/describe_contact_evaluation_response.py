"""Generated from Smithy shape ``com.amazonaws.connect#DescribeContactEvaluationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation
    import aws_sdk_connect.types.evaluation_form_content


class DescribeContactEvaluationResponse(TypedDict, closed=True):
    evaluation: "aws_sdk_connect.types.evaluation.Evaluation"
    """<p>Information about the evaluation form completed for a specific contact.</p>"""
    evaluation_form: (
        "aws_sdk_connect.types.evaluation_form_content.EvaluationFormContent"
    )
    """<p>Information about the evaluation form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeContactEvaluationResponse) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.evaluation

    out["Evaluation"] = aws_sdk_connect.types.evaluation.serialize_json(
        value["evaluation"]
    )
    import aws_sdk_connect.types.evaluation_form_content

    out["EvaluationForm"] = (
        aws_sdk_connect.types.evaluation_form_content.serialize_json(
            value["evaluation_form"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeContactEvaluationResponse:
    out: DescribeContactEvaluationResponse = {}  # type: ignore[typeddict-item]
    if "Evaluation" in data:
        import aws_sdk_connect.types.evaluation

        out["evaluation"] = aws_sdk_connect.types.evaluation.deserialize_json(
            data["Evaluation"]
        )
    else:
        raise DeserializationError(
            "DescribeContactEvaluationResponse.evaluation required"
        )
    if "EvaluationForm" in data:
        import aws_sdk_connect.types.evaluation_form_content

        out["evaluation_form"] = (
            aws_sdk_connect.types.evaluation_form_content.deserialize_json(
                data["EvaluationForm"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeContactEvaluationResponse.evaluation_form required"
        )
    return out
