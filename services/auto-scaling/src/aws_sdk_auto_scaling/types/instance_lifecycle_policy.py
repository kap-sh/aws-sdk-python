"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceLifecyclePolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.retention_triggers


class InstanceLifecyclePolicy(TypedDict):
    retention_triggers: NotRequired[
        "aws_sdk_auto_scaling.types.retention_triggers.RetentionTriggers"
    ]
    """<p> Specifies the conditions that trigger instance retention behavior. These triggers determine when instances should move to a <code>Retained</code> state instead of automatic termination. This allows you to maintain control over instance management when lifecycles transition and operations fail. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceLifecyclePolicy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "retention_triggers" in value:
        import aws_sdk_auto_scaling.types.retention_triggers

        aws_sdk_auto_scaling.types.retention_triggers.serialize_query(
            value["retention_triggers"], pairs, f"{prefix}.RetentionTriggers"
        )


def deserialize_query(el: Element) -> InstanceLifecyclePolicy:
    out: InstanceLifecyclePolicy = {}  # type: ignore[typeddict-item]
    child_retention_triggers = el.find("RetentionTriggers")
    if child_retention_triggers is not None:
        import aws_sdk_auto_scaling.types.retention_triggers

        out["retention_triggers"] = (
            aws_sdk_auto_scaling.types.retention_triggers.deserialize_query(
                child_retention_triggers
            )
        )
    return out
