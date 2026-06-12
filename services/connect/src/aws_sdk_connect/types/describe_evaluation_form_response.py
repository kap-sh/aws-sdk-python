"""Generated from Smithy shape ``com.amazonaws.connect#DescribeEvaluationFormResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form


class DescribeEvaluationFormResponse(TypedDict):
    evaluation_form: "aws_sdk_connect.types.evaluation_form.EvaluationForm"
    """<p>Information about the evaluation form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEvaluationFormResponse) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.evaluation_form

    out["EvaluationForm"] = aws_sdk_connect.types.evaluation_form.serialize_json(
        value["evaluation_form"]
    )
    return out


def deserialize_json(data: dict) -> DescribeEvaluationFormResponse:
    out: DescribeEvaluationFormResponse = {}  # type: ignore[typeddict-item]
    if "EvaluationForm" in data:
        import aws_sdk_connect.types.evaluation_form

        out["evaluation_form"] = aws_sdk_connect.types.evaluation_form.deserialize_json(
            data["EvaluationForm"]
        )
    else:
        raise DeserializationError(
            "DescribeEvaluationFormResponse.evaluation_form required"
        )
    return out
