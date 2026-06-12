"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#AdministrativeOverride``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.description
    import aws_sdk_elastic_load_balancing_v2.types.target_administrative_override_reason_enum
    import aws_sdk_elastic_load_balancing_v2.types.target_administrative_override_state_enum


class AdministrativeOverride(TypedDict):
    state: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_administrative_override_state_enum.TargetAdministrativeOverrideStateEnum"
    ]
    """<p>The state of the override.</p>"""
    reason: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_administrative_override_reason_enum.TargetAdministrativeOverrideReasonEnum"
    ]
    """<p>The reason code for the state.</p>"""
    description: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.description.Description"
    ]
    """<p>A description of the override state that provides additional details.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AdministrativeOverride, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "state" in value:
        import aws_sdk_elastic_load_balancing_v2.types.target_administrative_override_state_enum

        aws_sdk_elastic_load_balancing_v2.types.target_administrative_override_state_enum.serialize_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "reason" in value:
        import aws_sdk_elastic_load_balancing_v2.types.target_administrative_override_reason_enum

        aws_sdk_elastic_load_balancing_v2.types.target_administrative_override_reason_enum.serialize_query(
            value["reason"], pairs, f"{prefix}.Reason"
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))


def deserialize_query(el: Element) -> AdministrativeOverride:
    out: AdministrativeOverride = {}  # type: ignore[typeddict-item]
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_elastic_load_balancing_v2.types.target_administrative_override_state_enum

        out["state"] = (
            aws_sdk_elastic_load_balancing_v2.types.target_administrative_override_state_enum.deserialize_query(
                child_state
            )
        )
    child_reason = el.find("Reason")
    if child_reason is not None:
        import aws_sdk_elastic_load_balancing_v2.types.target_administrative_override_reason_enum

        out["reason"] = (
            aws_sdk_elastic_load_balancing_v2.types.target_administrative_override_reason_enum.deserialize_query(
                child_reason
            )
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    return out
