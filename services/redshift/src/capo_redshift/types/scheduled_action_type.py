"""Generated from Smithy shape ``com.amazonaws.redshift#ScheduledActionType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.pause_cluster_message
    import capo_redshift.types.resize_cluster_message
    import capo_redshift.types.resume_cluster_message


class ScheduledActionType(TypedDict, closed=True):
    resize_cluster: NotRequired[
        "capo_redshift.types.resize_cluster_message.ResizeClusterMessage"
    ]
    """<p>An action that runs a <code>ResizeCluster</code> API operation. </p>"""
    pause_cluster: NotRequired[
        "capo_redshift.types.pause_cluster_message.PauseClusterMessage"
    ]
    """<p>An action that runs a <code>PauseCluster</code> API operation. </p>"""
    resume_cluster: NotRequired[
        "capo_redshift.types.resume_cluster_message.ResumeClusterMessage"
    ]
    """<p>An action that runs a <code>ResumeCluster</code> API operation. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ScheduledActionType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resize_cluster" in value:
        import capo_redshift.types.resize_cluster_message

        capo_redshift.types.resize_cluster_message.serialize_query(
            value["resize_cluster"], pairs, f"{key_prefix}ResizeCluster"
        )
    if "pause_cluster" in value:
        import capo_redshift.types.pause_cluster_message

        capo_redshift.types.pause_cluster_message.serialize_query(
            value["pause_cluster"], pairs, f"{key_prefix}PauseCluster"
        )
    if "resume_cluster" in value:
        import capo_redshift.types.resume_cluster_message

        capo_redshift.types.resume_cluster_message.serialize_query(
            value["resume_cluster"], pairs, f"{key_prefix}ResumeCluster"
        )


def deserialize_query(el: Element) -> ScheduledActionType:
    out: ScheduledActionType = {}  # type: ignore[typeddict-item]
    child_resize_cluster = el.find("ResizeCluster")
    if child_resize_cluster is not None:
        import capo_redshift.types.resize_cluster_message

        out["resize_cluster"] = (
            capo_redshift.types.resize_cluster_message.deserialize_query(
                child_resize_cluster
            )
        )
    child_pause_cluster = el.find("PauseCluster")
    if child_pause_cluster is not None:
        import capo_redshift.types.pause_cluster_message

        out["pause_cluster"] = (
            capo_redshift.types.pause_cluster_message.deserialize_query(
                child_pause_cluster
            )
        )
    child_resume_cluster = el.find("ResumeCluster")
    if child_resume_cluster is not None:
        import capo_redshift.types.resume_cluster_message

        out["resume_cluster"] = (
            capo_redshift.types.resume_cluster_message.deserialize_query(
                child_resume_cluster
            )
        )
    return out
