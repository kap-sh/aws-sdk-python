"""Generated from Smithy shape ``com.amazonaws.autoscaling#PoliciesType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.scaling_policies
    import capo_auto_scaling.types.xml_string


class PoliciesType(TypedDict, closed=True):
    scaling_policies: NotRequired[
        "capo_auto_scaling.types.scaling_policies.ScalingPolicies"
    ]
    """<p>The scaling policies.</p>"""
    next_token: NotRequired["capo_auto_scaling.types.xml_string.XmlString"]
    """<p>A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the <code>NextToken</code> value when requesting the next set of items. This value is null when there are no more items to return.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PoliciesType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "scaling_policies" in value:
        import capo_auto_scaling.types.scaling_policies

        capo_auto_scaling.types.scaling_policies.serialize_query(
            value["scaling_policies"], pairs, f"{prefix}.ScalingPolicies"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> PoliciesType:
    out: PoliciesType = {}  # type: ignore[typeddict-item]
    child_scaling_policies = el.find("ScalingPolicies")
    if child_scaling_policies is not None:
        import capo_auto_scaling.types.scaling_policies

        out["scaling_policies"] = (
            capo_auto_scaling.types.scaling_policies.deserialize_query(
                child_scaling_policies
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
