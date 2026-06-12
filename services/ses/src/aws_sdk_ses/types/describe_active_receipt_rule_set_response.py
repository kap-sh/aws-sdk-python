"""Generated from Smithy shape ``com.amazonaws.ses#DescribeActiveReceiptRuleSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.receipt_rule_set_metadata
    import aws_sdk_ses.types.receipt_rules_list


class DescribeActiveReceiptRuleSetResponse(TypedDict):
    metadata: NotRequired[
        "aws_sdk_ses.types.receipt_rule_set_metadata.ReceiptRuleSetMetadata"
    ]
    """<p>The metadata for the currently active receipt rule set. The metadata consists of the rule set name and a timestamp of when the rule set was created.</p>"""
    rules: NotRequired["aws_sdk_ses.types.receipt_rules_list.ReceiptRulesList"]
    """<p>The receipt rules that belong to the active rule set.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeActiveReceiptRuleSetResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "metadata" in value:
        import aws_sdk_ses.types.receipt_rule_set_metadata

        aws_sdk_ses.types.receipt_rule_set_metadata.serialize_query(
            value["metadata"], pairs, f"{prefix}.Metadata"
        )
    if "rules" in value:
        import aws_sdk_ses.types.receipt_rules_list

        aws_sdk_ses.types.receipt_rules_list.serialize_query(
            value["rules"], pairs, f"{prefix}.Rules"
        )


def deserialize_query(el: Element) -> DescribeActiveReceiptRuleSetResponse:
    out: DescribeActiveReceiptRuleSetResponse = {}  # type: ignore[typeddict-item]
    child_metadata = el.find("Metadata")
    if child_metadata is not None:
        import aws_sdk_ses.types.receipt_rule_set_metadata

        out["metadata"] = aws_sdk_ses.types.receipt_rule_set_metadata.deserialize_query(
            child_metadata
        )
    child_rules = el.find("Rules")
    if child_rules is not None:
        import aws_sdk_ses.types.receipt_rules_list

        out["rules"] = aws_sdk_ses.types.receipt_rules_list.deserialize_query(
            child_rules
        )
    return out
