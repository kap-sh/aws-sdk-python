"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DeleteInsightRulesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.batch_failures


class DeleteInsightRulesOutput(TypedDict, closed=True):
    failures: NotRequired["aws_sdk_cloudwatch.types.batch_failures.BatchFailures"]
    """<p>An array listing the rules that could not be deleted. You cannot delete built-in rules.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteInsightRulesOutput) -> dict:
    out: dict = {}
    if "failures" in value:
        import aws_sdk_cloudwatch.types.batch_failures

        out["Failures"] = (
            aws_sdk_cloudwatch.types.batch_failures.serialize_aws_json_1_0(
                value["failures"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteInsightRulesOutput:
    out: DeleteInsightRulesOutput = {}  # type: ignore[typeddict-item]
    if "Failures" in data:
        import aws_sdk_cloudwatch.types.batch_failures

        out["failures"] = (
            aws_sdk_cloudwatch.types.batch_failures.deserialize_aws_json_1_0(
                data["Failures"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteInsightRulesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "failures" in value:
        import aws_sdk_cloudwatch.types.batch_failures

        aws_sdk_cloudwatch.types.batch_failures.serialize_query(
            value["failures"], pairs, f"{prefix}.Failures"
        )


def deserialize_query(el: Element) -> DeleteInsightRulesOutput:
    out: DeleteInsightRulesOutput = {}  # type: ignore[typeddict-item]
    child_failures = el.find("Failures")
    if child_failures is not None:
        import aws_sdk_cloudwatch.types.batch_failures

        out["failures"] = aws_sdk_cloudwatch.types.batch_failures.deserialize_query(
            child_failures
        )
    return out
