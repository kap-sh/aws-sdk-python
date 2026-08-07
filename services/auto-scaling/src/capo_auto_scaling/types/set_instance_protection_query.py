"""Generated from Smithy shape ``com.amazonaws.autoscaling#SetInstanceProtectionQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.instance_ids
    import capo_auto_scaling.types.protected_from_scale_in
    import capo_auto_scaling.types.xml_string_max_len255


class SetInstanceProtectionQuery(TypedDict, closed=True):
    instance_ids: NotRequired["capo_auto_scaling.types.instance_ids.InstanceIds"]
    """<p>One or more instance IDs. You can specify up to 50 instances.</p>"""
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    protected_from_scale_in: NotRequired[
        "capo_auto_scaling.types.protected_from_scale_in.ProtectedFromScaleIn"
    ]
    """<p>Indicates whether the instance is protected from termination by Amazon EC2 Auto Scaling when scaling in.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetInstanceProtectionQuery, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_ids" in value:
        import capo_auto_scaling.types.instance_ids

        capo_auto_scaling.types.instance_ids.serialize_query(
            value["instance_ids"], pairs, f"{key_prefix}InstanceIds"
        )
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{key_prefix}AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "protected_from_scale_in" in value:
        pairs.append(
            (
                f"{key_prefix}ProtectedFromScaleIn",
                "true" if value["protected_from_scale_in"] else "false",
            )
        )


def deserialize_query(el: Element) -> SetInstanceProtectionQuery:
    out: SetInstanceProtectionQuery = {}  # type: ignore[typeddict-item]
    child_instance_ids = el.find("InstanceIds")
    if child_instance_ids is not None:
        import capo_auto_scaling.types.instance_ids

        out["instance_ids"] = capo_auto_scaling.types.instance_ids.deserialize_query(
            child_instance_ids
        )
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_protected_from_scale_in = el.find("ProtectedFromScaleIn")
    if child_protected_from_scale_in is not None:
        out["protected_from_scale_in"] = (
            child_protected_from_scale_in.text or ""
        ).lower() == "true"
    return out
