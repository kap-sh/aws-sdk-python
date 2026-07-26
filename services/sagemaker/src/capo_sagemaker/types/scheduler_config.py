"""Generated from Smithy shape ``com.amazonaws.sagemaker#SchedulerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.fair_share
    import capo_sagemaker.types.idle_resource_sharing
    import capo_sagemaker.types.priority_class_list


class SchedulerConfig(TypedDict, closed=True):
    priority_classes: NotRequired[
        "capo_sagemaker.types.priority_class_list.PriorityClassList"
    ]
    """<p>List of the priority classes, <code>PriorityClass</code>, of the cluster policy. When specified, these class configurations define how tasks are queued.</p>"""
    fair_share: NotRequired["capo_sagemaker.types.fair_share.FairShare"]
    """<p>When enabled, entities borrow idle compute based on their assigned <code>FairShareWeight</code>.</p> <p>When disabled, entities borrow idle compute based on a first-come first-serve basis.</p> <p>Default is <code>Enabled</code>.</p>"""
    idle_resource_sharing: NotRequired[
        "capo_sagemaker.types.idle_resource_sharing.IdleResourceSharing"
    ]
    """<p>Configuration for sharing idle compute resources across entities in the cluster. When enabled, unallocated resources are automatically calculated and made available for entities to borrow. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchedulerConfig) -> dict:
    out: dict = {}
    if "priority_classes" in value:
        import capo_sagemaker.types.priority_class_list

        out["PriorityClasses"] = (
            capo_sagemaker.types.priority_class_list.serialize_aws_json_1_1(
                value["priority_classes"]
            )
        )
    if "fair_share" in value:
        import capo_sagemaker.types.fair_share

        out["FairShare"] = capo_sagemaker.types.fair_share.serialize_aws_json_1_1(
            value["fair_share"]
        )
    if "idle_resource_sharing" in value:
        import capo_sagemaker.types.idle_resource_sharing

        out["IdleResourceSharing"] = (
            capo_sagemaker.types.idle_resource_sharing.serialize_aws_json_1_1(
                value["idle_resource_sharing"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SchedulerConfig:
    out: SchedulerConfig = {}  # type: ignore[typeddict-item]
    if "PriorityClasses" in data:
        import capo_sagemaker.types.priority_class_list

        out["priority_classes"] = (
            capo_sagemaker.types.priority_class_list.deserialize_aws_json_1_1(
                data["PriorityClasses"]
            )
        )
    if "FairShare" in data:
        import capo_sagemaker.types.fair_share

        out["fair_share"] = capo_sagemaker.types.fair_share.deserialize_aws_json_1_1(
            data["FairShare"]
        )
    if "IdleResourceSharing" in data:
        import capo_sagemaker.types.idle_resource_sharing

        out["idle_resource_sharing"] = (
            capo_sagemaker.types.idle_resource_sharing.deserialize_aws_json_1_1(
                data["IdleResourceSharing"]
            )
        )
    return out
