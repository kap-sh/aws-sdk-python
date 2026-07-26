"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveBooleanExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.archive_boolean_operator
    import capo_mailmanager.types.archive_boolean_to_evaluate


class ArchiveBooleanExpression(TypedDict, closed=True):
    evaluate: (
        "capo_mailmanager.types.archive_boolean_to_evaluate.ArchiveBooleanToEvaluate"
    )
    """<p>The email attribute value to evaluate.</p>"""
    operator: "capo_mailmanager.types.archive_boolean_operator.ArchiveBooleanOperator"
    """<p>The boolean operator to use for evaluation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveBooleanExpression) -> dict:
    out: dict = {}
    import capo_mailmanager.types.archive_boolean_to_evaluate

    out["Evaluate"] = (
        capo_mailmanager.types.archive_boolean_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import capo_mailmanager.types.archive_boolean_operator

    out["Operator"] = (
        capo_mailmanager.types.archive_boolean_operator.serialize_aws_json_1_0(
            value["operator"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ArchiveBooleanExpression:
    out: ArchiveBooleanExpression = {}  # type: ignore[typeddict-item]
    if "Evaluate" in data:
        import capo_mailmanager.types.archive_boolean_to_evaluate

        out["evaluate"] = (
            capo_mailmanager.types.archive_boolean_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        raise DeserializationError("ArchiveBooleanExpression.evaluate required")
    if "Operator" in data:
        import capo_mailmanager.types.archive_boolean_operator

        out["operator"] = (
            capo_mailmanager.types.archive_boolean_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("ArchiveBooleanExpression.operator required")
    return out
