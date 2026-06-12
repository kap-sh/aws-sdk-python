"""Generated from Smithy shape ``com.amazonaws.cloudwatch#PutManagedInsightRulesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.batch_failures


class PutManagedInsightRulesOutput(TypedDict):
    failures: NotRequired["aws_sdk_cloudwatch.types.batch_failures.BatchFailures"]
    """<p> An array that lists the rules that could not be enabled. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutManagedInsightRulesOutput) -> dict:
    out: dict = {}
    if "failures" in value:
        import aws_sdk_cloudwatch.types.batch_failures

        out["Failures"] = (
            aws_sdk_cloudwatch.types.batch_failures.serialize_aws_json_1_0(
                value["failures"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PutManagedInsightRulesOutput:
    out: PutManagedInsightRulesOutput = {}  # type: ignore[typeddict-item]
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
    value: PutManagedInsightRulesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "failures" in value:
        import aws_sdk_cloudwatch.types.batch_failures

        aws_sdk_cloudwatch.types.batch_failures.serialize_query(
            value["failures"], pairs, f"{prefix}.Failures"
        )


def deserialize_query(el: Element) -> PutManagedInsightRulesOutput:
    out: PutManagedInsightRulesOutput = {}  # type: ignore[typeddict-item]
    child_failures = el.find("Failures")
    if child_failures is not None:
        import aws_sdk_cloudwatch.types.batch_failures

        out["failures"] = aws_sdk_cloudwatch.types.batch_failures.deserialize_query(
            child_failures
        )
    return out
