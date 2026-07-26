"""Generated from Smithy shape ``com.amazonaws.iam#Statement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.policy_identifier_type
    import capo_iam.types.policy_source_type
    import capo_iam.types.position


class Statement(TypedDict, closed=True):
    source_policy_id: NotRequired[
        "capo_iam.types.policy_identifier_type.PolicyIdentifierType"
    ]
    """<p>The identifier of the policy that was provided as an input.</p>"""
    source_policy_type: NotRequired[
        "capo_iam.types.policy_source_type.PolicySourceType"
    ]
    """<p>The type of the policy.</p>"""
    start_position: NotRequired["capo_iam.types.position.Position"]
    """<p>The row and column of the beginning of the <code>Statement</code> in an IAM policy.</p>"""
    end_position: NotRequired["capo_iam.types.position.Position"]
    """<p>The row and column of the end of a <code>Statement</code> in an IAM policy.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: Statement, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source_policy_id" in value:
        pairs.append((f"{prefix}.SourcePolicyId", str(value["source_policy_id"])))
    if "source_policy_type" in value:
        import capo_iam.types.policy_source_type

        capo_iam.types.policy_source_type.serialize_query(
            value["source_policy_type"], pairs, f"{prefix}.SourcePolicyType"
        )
    if "start_position" in value:
        import capo_iam.types.position

        capo_iam.types.position.serialize_query(
            value["start_position"], pairs, f"{prefix}.StartPosition"
        )
    if "end_position" in value:
        import capo_iam.types.position

        capo_iam.types.position.serialize_query(
            value["end_position"], pairs, f"{prefix}.EndPosition"
        )


def deserialize_query(el: Element) -> Statement:
    out: Statement = {}  # type: ignore[typeddict-item]
    child_source_policy_id = el.find("SourcePolicyId")
    if child_source_policy_id is not None:
        out["source_policy_id"] = str(child_source_policy_id.text or "")
    child_source_policy_type = el.find("SourcePolicyType")
    if child_source_policy_type is not None:
        import capo_iam.types.policy_source_type

        out["source_policy_type"] = capo_iam.types.policy_source_type.deserialize_query(
            child_source_policy_type
        )
    child_start_position = el.find("StartPosition")
    if child_start_position is not None:
        import capo_iam.types.position

        out["start_position"] = capo_iam.types.position.deserialize_query(
            child_start_position
        )
    child_end_position = el.find("EndPosition")
    if child_end_position is not None:
        import capo_iam.types.position

        out["end_position"] = capo_iam.types.position.deserialize_query(
            child_end_position
        )
    return out
