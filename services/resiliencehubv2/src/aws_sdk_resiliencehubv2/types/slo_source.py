"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SloSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.entity_name
    import aws_sdk_resiliencehubv2.types.policy_value_source


class SloSource(TypedDict):
    value: NotRequired["float"]
    """<p>The availability SLO percentage value.</p>"""
    policy_name: NotRequired["aws_sdk_resiliencehubv2.types.entity_name.EntityName"]
    source: NotRequired[
        "aws_sdk_resiliencehubv2.types.policy_value_source.PolicyValueSource"
    ]
    """<p>Indicates whether the value comes from the service's own account or a cross-account policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SloSource) -> dict:
    out: dict = {}
    if "value" in value:
        out["value"] = value["value"]
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
    if "source" in value:
        import aws_sdk_resiliencehubv2.types.policy_value_source

        out["source"] = (
            aws_sdk_resiliencehubv2.types.policy_value_source.serialize_json(
                value["source"]
            )
        )
    return out


def deserialize_json(data: dict) -> SloSource:
    out: SloSource = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    if "policyName" in data:
        out["policy_name"] = data["policyName"]
    if "source" in data:
        import aws_sdk_resiliencehubv2.types.policy_value_source

        out["source"] = (
            aws_sdk_resiliencehubv2.types.policy_value_source.deserialize_json(
                data["source"]
            )
        )
    return out
