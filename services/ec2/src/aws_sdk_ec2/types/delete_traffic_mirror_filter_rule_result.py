"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTrafficMirrorFilterRuleResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class DeleteTrafficMirrorFilterRuleResult(TypedDict):
    traffic_mirror_filter_rule_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the deleted Traffic Mirror rule.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTrafficMirrorFilterRuleResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "traffic_mirror_filter_rule_id" in value:
        pairs.append(
            (
                f"{prefix}.TrafficMirrorFilterRuleId",
                str(value["traffic_mirror_filter_rule_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> DeleteTrafficMirrorFilterRuleResult:
    out: DeleteTrafficMirrorFilterRuleResult = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_filter_rule_id = el.find("TrafficMirrorFilterRuleId")
    if child_traffic_mirror_filter_rule_id is not None:
        out["traffic_mirror_filter_rule_id"] = str(
            child_traffic_mirror_filter_rule_id.text or ""
        )
    return out
