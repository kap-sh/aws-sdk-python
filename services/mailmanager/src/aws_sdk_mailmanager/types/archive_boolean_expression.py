"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveBooleanExpression``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.archive_boolean_operator
    import aws_sdk_mailmanager.types.archive_boolean_to_evaluate


class ArchiveBooleanExpression(TypedDict):
    evaluate: (
        "aws_sdk_mailmanager.types.archive_boolean_to_evaluate.ArchiveBooleanToEvaluate"
    )
    """<p>The email attribute value to evaluate.</p>"""
    operator: (
        "aws_sdk_mailmanager.types.archive_boolean_operator.ArchiveBooleanOperator"
    )
    """<p>The boolean operator to use for evaluation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveBooleanExpression) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.archive_boolean_to_evaluate

    out["Evaluate"] = (
        aws_sdk_mailmanager.types.archive_boolean_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import aws_sdk_mailmanager.types.archive_boolean_operator

    out["Operator"] = (
        aws_sdk_mailmanager.types.archive_boolean_operator.serialize_aws_json_1_0(
            value["operator"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ArchiveBooleanExpression:
    out: ArchiveBooleanExpression = {}  # type: ignore[typeddict-item]
    if "Evaluate" in data:
        import aws_sdk_mailmanager.types.archive_boolean_to_evaluate

        out["evaluate"] = (
            aws_sdk_mailmanager.types.archive_boolean_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        raise DeserializationError("ArchiveBooleanExpression.evaluate required")
    if "Operator" in data:
        import aws_sdk_mailmanager.types.archive_boolean_operator

        out["operator"] = (
            aws_sdk_mailmanager.types.archive_boolean_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("ArchiveBooleanExpression.operator required")
    return out
