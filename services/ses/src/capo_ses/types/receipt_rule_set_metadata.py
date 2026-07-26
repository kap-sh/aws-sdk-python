"""Generated from Smithy shape ``com.amazonaws.ses#ReceiptRuleSetMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.receipt_rule_set_name
    import capo_ses.types.timestamp


class ReceiptRuleSetMetadata(TypedDict, closed=True):
    name: NotRequired["capo_ses.types.receipt_rule_set_name.ReceiptRuleSetName"]
    """<p>The name of the receipt rule set. The name must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).</p> </li> <li> <p>Start and end with a letter or number.</p> </li> <li> <p>Contain 64 characters or fewer.</p> </li> </ul>"""
    created_timestamp: NotRequired["capo_ses.types.timestamp.Timestamp"]
    """<p>The date and time the receipt rule set was created.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReceiptRuleSetMetadata, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "created_timestamp" in value:
        import capo_ses.types.timestamp

        capo_ses.types.timestamp.serialize_query(
            value["created_timestamp"], pairs, f"{prefix}.CreatedTimestamp"
        )


def deserialize_query(el: Element) -> ReceiptRuleSetMetadata:
    out: ReceiptRuleSetMetadata = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_created_timestamp = el.find("CreatedTimestamp")
    if child_created_timestamp is not None:
        import capo_ses.types.timestamp

        out["created_timestamp"] = capo_ses.types.timestamp.deserialize_query(
            child_created_timestamp
        )
    return out
