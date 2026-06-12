"""Generated from Smithy shape ``com.amazonaws.cloudwatch#PutManagedInsightRulesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.managed_rules


class PutManagedInsightRulesInput(TypedDict):
    managed_rules: NotRequired["aws_sdk_cloudwatch.types.managed_rules.ManagedRules"]
    """<p> A list of <code>ManagedRules</code> to enable. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutManagedInsightRulesInput) -> dict:
    out: dict = {}
    if "managed_rules" in value:
        import aws_sdk_cloudwatch.types.managed_rules

        out["ManagedRules"] = (
            aws_sdk_cloudwatch.types.managed_rules.serialize_aws_json_1_0(
                value["managed_rules"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PutManagedInsightRulesInput:
    out: PutManagedInsightRulesInput = {}  # type: ignore[typeddict-item]
    if "ManagedRules" in data:
        import aws_sdk_cloudwatch.types.managed_rules

        out["managed_rules"] = (
            aws_sdk_cloudwatch.types.managed_rules.deserialize_aws_json_1_0(
                data["ManagedRules"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: PutManagedInsightRulesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "managed_rules" in value:
        import aws_sdk_cloudwatch.types.managed_rules

        aws_sdk_cloudwatch.types.managed_rules.serialize_query(
            value["managed_rules"], pairs, f"{prefix}.ManagedRules"
        )


def deserialize_query(el: Element) -> PutManagedInsightRulesInput:
    out: PutManagedInsightRulesInput = {}  # type: ignore[typeddict-item]
    child_managed_rules = el.find("ManagedRules")
    if child_managed_rules is not None:
        import aws_sdk_cloudwatch.types.managed_rules

        out["managed_rules"] = aws_sdk_cloudwatch.types.managed_rules.deserialize_query(
            child_managed_rules
        )
    return out
