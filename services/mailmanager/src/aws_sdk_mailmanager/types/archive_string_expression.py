"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveStringExpression``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.archive_string_operator
    import aws_sdk_mailmanager.types.archive_string_to_evaluate
    import aws_sdk_mailmanager.types.string_value_list


class ArchiveStringExpression(TypedDict):
    evaluate: (
        "aws_sdk_mailmanager.types.archive_string_to_evaluate.ArchiveStringToEvaluate"
    )
    """<p>The attribute of the email to evaluate.</p>"""
    operator: "aws_sdk_mailmanager.types.archive_string_operator.ArchiveStringOperator"
    """<p>The operator to use when evaluating the string values.</p>"""
    values: "aws_sdk_mailmanager.types.string_value_list.StringValueList"
    """<p>The list of string values to evaluate the email attribute against.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveStringExpression) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.archive_string_to_evaluate

    out["Evaluate"] = (
        aws_sdk_mailmanager.types.archive_string_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import aws_sdk_mailmanager.types.archive_string_operator

    out["Operator"] = (
        aws_sdk_mailmanager.types.archive_string_operator.serialize_aws_json_1_0(
            value["operator"]
        )
    )
    import aws_sdk_mailmanager.types.string_value_list

    out["Values"] = aws_sdk_mailmanager.types.string_value_list.serialize_aws_json_1_0(
        value["values"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ArchiveStringExpression:
    out: ArchiveStringExpression = {}  # type: ignore[typeddict-item]
    if "Evaluate" in data:
        import aws_sdk_mailmanager.types.archive_string_to_evaluate

        out["evaluate"] = (
            aws_sdk_mailmanager.types.archive_string_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        raise DeserializationError("ArchiveStringExpression.evaluate required")
    if "Operator" in data:
        import aws_sdk_mailmanager.types.archive_string_operator

        out["operator"] = (
            aws_sdk_mailmanager.types.archive_string_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("ArchiveStringExpression.operator required")
    if "Values" in data:
        import aws_sdk_mailmanager.types.string_value_list

        out["values"] = (
            aws_sdk_mailmanager.types.string_value_list.deserialize_aws_json_1_0(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("ArchiveStringExpression.values required")
    return out
