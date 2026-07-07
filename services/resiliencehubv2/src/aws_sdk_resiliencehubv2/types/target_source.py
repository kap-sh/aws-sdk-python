"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#TargetSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.entity_name
    import aws_sdk_resiliencehubv2.types.policy_value_source


class TargetSource(TypedDict, closed=True):
    value: NotRequired["int"]
    """<p>The RTO or RPO value in minutes.</p>"""
    policy_name: NotRequired["aws_sdk_resiliencehubv2.types.entity_name.EntityName"]
    source: NotRequired[
        "aws_sdk_resiliencehubv2.types.policy_value_source.PolicyValueSource"
    ]
    """<p>Indicates whether the value comes from the service's own account or a cross-account policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetSource) -> dict:
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


def deserialize_json(data: dict) -> TargetSource:
    out: TargetSource = {}  # type: ignore[typeddict-item]
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
